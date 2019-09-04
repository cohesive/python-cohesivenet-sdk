
# #!/bin/bash

# #$SecLinkInstanceId = Instance ID and intial password
# #$SecLinkPassword = Password to set SecLink controller to
# #$FedNetPassword = FedNet controller password
# #$SecLinkap = SecLink primary private IP 
# #$SecLinkas = SecLink secondary private IP
# #$TopologyName = Name of SecLink VPC
# #$SecLinkTopoPassword = Password for SecLink topology
# #$SecLinkCIDR = CIDR of SecLink VPC
# #$SecLinkSN = Subnet that SecLink controller is in
# #$VPC = Name of the VPC (set SecLink topology name to)
# #$ContainerNetwork
# #$secretPSK = PSK for IPsec connections
# #$FedNeta1p = FedNet controller 1 primary private address
# #$FedNeta2p = FedNet controller 2 primary private address
# #$FedNet1Cidr = FedNet controller 1 subnet
# #$FedNet2Cidr = FedNet controller 2 subnet
# #$FedNeta1s = FedNet controller 1 secondary private address
# #$FedNeta2s = FedNet controller 2 secondary private address
# #$FedNet1asn = ASN of FedNet1
# #$FedNet2asn =  ASN of FedNet2
# #$OnpremAccessCIDR = On prem cidr for firewall rule. (Optional)


# echo "Running configure.sh v 4.8"

# ## Calculate subnet gateway for SecLink controller route rule
# SECLINK_NET=$(echo $SecLinkSN | sed 's/\/.*//'| sed 's/\.[^.]*$//')
# SECLINK_MASK=$(echo $SecLinkSN | sed 's/.*\///')
# SECLINK_=$(echo $SecLinkSN | sed 's/\/.*//'| sed 's/.*\.//')
# SECLINK_A=$((SECLINK_ + 1))
# SECLINK_GW=$SECLINK_NET.$SECLINK_A

# ## Calculate VTI primary inner and outer addresses 
# PRIMARY_VTI_NET=$(echo $PrimaryVTICidr | sed 's/\/.*//'| sed 's/\.[^.]*$//')
# PRIMARY_VTI=$(echo $PrimaryVTICidr | sed 's/\/.*//'| sed 's/.*\.//')
# PRIMARY_VTI_I=$((PRIMARY_VTI))
# PRIMARY_VTI_O=$((PRIMARY_VTI + 1))
# PRIMARY_VTI_INNER=$PRIMARY_VTI_NET.$PRIMARY_VTI_I/31
# PRIMARY_VTI_OUTER=$PRIMARY_VTI_NET.$PRIMARY_VTI_O/31
# PRIMARY_VTI_INNER_ADDRESS=$PRIMARY_VTI_NET.$PRIMARY_VTI_I
# PRIMARY_VTI_OUTER_ADDRESS=$PRIMARY_VTI_NET.$PRIMARY_VTI_O

# ## Calculate VTI secondary inner and outer addresses 
# SECONDARY_VTI_NET=$(echo $SecondaryVTICidr | sed 's/\/.*//'| sed 's/\.[^.]*$//')
# SECONDARY_VTI=$(echo $SecondaryVTICidr | sed 's/\/.*//'| sed 's/.*\.//')
# SECONDARY_VTI_I=$((SECONDARY_VTI))
# SECONDARY_VTI_O=$((SECONDARY_VTI + 1))
# SECONDARY_VTI_INNER=$SECONDARY_VTI_NET.$SECONDARY_VTI_I/31
# SECONDARY_VTI_OUTER=$SECONDARY_VTI_NET.$SECONDARY_VTI_O/31
# SECONDARY_VTI_INNER_ADDRESS=$SECONDARY_VTI_NET.$SECONDARY_VTI_I
# SECONDARY_VTI_OUTER_ADDRESS=$SECONDARY_VTI_NET.$SECONDARY_VTI_O

# ## Calculate gateways for fednet controllers
# PRIMARY_FEDNET_CIDR_NET=$(echo $FedNet1Cidr | sed 's/\/.*//'| sed 's/\.[^.]*$//')
# PRIMARY_FEDNET_CIDR_NET_FINAL=$(echo $FedNet1Cidr | sed 's/\/.*//'| sed 's/.*\.//')
# PRIMARY_FEDNET_NET_NEXT=$((PRIMARY_FEDNET_CIDR_NET_FINAL + 1))
# PRIMARY_FEDNET_GW=$PRIMARY_FEDNET_CIDR_NET.$PRIMARY_FEDNET_NET_NEXT

# SECONDARY_FEDNET_CIDR_NET=$(echo $FedNet2Cidr | sed 's/\/.*//'| sed 's/\.[^.]*$//')
# SECONDARY_FEDNET_CIDR_NET_FINAL=$(echo $FedNet2Cidr | sed 's/\/.*//'| sed 's/.*\.//')
# SECONDARY_FEDNET_NET_NEXT=$((SECONDARY_FEDNET_CIDR_NET_FINAL + 1))
# SECONDARY_FEDNET_GW=$SECONDARY_FEDNET_CIDR_NET.$SECONDARY_FEDNET_NET_NEXT

# PRIME=_Primary
# SECOND=_Secondary
# VPCNAME=$(echo $VPC | sed 's/-/_/g')
# NAME_PRIMARY=$VPCNAME$PRIME
# NAME_SECONDARY=$VPCNAME$SECOND

# echo "Building seclink $VPC"

# wait_for_api () {
#     local apipassword=$1
#     local host=$2
#     while :
#         do
#             apistatus=`curl -k -X GET -u api:$apipassword https://$host:8000/api/config 2>&1`
#             echo $apistatus | grep "error\|refused"
#             if [ $? != 0 ] ; then
#                 break
#             fi
            
#             echo "Waiting for VNS3 API"
#             sleep 5
#         done
# }

# wait_for_keyset() {
#     local apipassword=$1
#     local host=$2
#     while :
#         do
#         apistatus=`curl -k -X GET -u api:$apipassword https://$host:8000/api/keyset 2>&1`
#             echo $apistatus | grep '"keyset_present":false'
#             if [ $? != 0 ] ; then
#                 break
#             fi
            
#             echo "Waiting for keyset"
#             sleep 1
#         done
# }

# set_container_network () {
#   echo "Setting the container plugin network cidr on $2"
#   ./vnscubed.rb -K api -S $1 -H $2 stop_container_system
#   while :
#     do
#     apistatus=`./vnscubed.rb -K api -S $1 -H $2 desc_container_system 2>&1`
#        echo $apistatus | grep "false"
#          if [ $? = 0 ] ; then
#            break
#          fi
#          echo "Waiting for container system to stop on $2"
#          sleep 1
#     done
#   ./vnscubed.rb -K api -S $1 -H $2 setup_container_system --network $3
#   sleep 10
#   ./vnscubed.rb -K api -S $1 -H $2 start_container_system
#   while :
#     do
#     apistatus=`./vnscubed.rb -K api -S $1 -H $2 desc_container_system 2>&1`
#        echo $apistatus | grep "true"
#          if [ $? = 0 ] ; then
#            break
#          fi
#          echo "Waiting for container system to start on $2"
#          sleep 1
#     done
# }

# set_firewall() {
#   local onPremCidrs=$1
#   local incloudCidr=$2
#   local host=$3
#   local apipassword=$4

#   PolicyNameOnPrem="NETS_seclink_onprem"
#   PolicyNameInCloud="NETS_seclink_incloud"
#   OnPremFWSet=""
#   InCloudFWSet="$PolicyNameInCloud $incloudCidr\n"

#   for cidr in $(echo $onPremCidrs | sed "s/,/ /g")
#   do
#       OnPremFWSet="$OnPremFWSet $PolicyNameOnPrem $cidr\n"
#   done

#   OnPremFWSet="$(echo "${OnPremFWSet}" | sed -e 's/^[[:space:]]*//')"
#   echo "Creating onprem FW Set: '$OnPremFWSet'"
#   curl -k -X POST -u api:$apipassword \
#     -d "{\"rules\":\"$OnPremFWSet\", \"flush\":\"true\"}" \
#     -H 'Content-Type: application/json' \
#     https://$host:8000/api/firewall/fwsets

#   echo "Creating incloud FW Set: '$InCloudFWSet'"
#   curl -k -X POST -u api:$apipassword \
#     -d "{\"rules\":\"$InCloudFWSet\", \"flush\":\"true\"}" \
#     -H 'Content-Type: application/json' \
#     https://$host:8000/api/firewall/fwsets

#   # Now allowing traffic routed to/from the on prem group and the cloud group
#   echo "Creating rule FORWARD CUST $PolicyNameOnPrem -> $PolicyNameInCloud"
#   curl -k -X POST -u api:$apipassword \
#     -d "{\"rule\":\"FORWARD_CUST -m set --set $PolicyNameOnPrem src -m set --set $PolicyNameInCloud dst -j ACCEPT\"}" \
#     -H 'Content-Type: application/json' \
#     https://$host:8000/api/firewall/rules

#   echo "Creating rule FORWARD CUST $PolicyNameInCloud -> $PolicyNameOnPrem"
#   curl -k -X POST -u api:$apipassword \
#     -d "{\"rule\":\"FORWARD_CUST -m set --set $PolicyNameOnPrem dst -m set --set $PolicyNameInCloud src -j ACCEPT\"}" \
#     -H 'Content-Type: application/json' \
#     https://$host:8000/api/firewall/rules

#   # Now dropping routing any other traffic in/out of VPC
#   echo "Creating rule FORWARD CUST DROP ALL ELSE"
#   curl -k -X POST -u api:$apipassword \
#     -d '{"rule":"FORWARD_CUST -j DROP", "position":"-1"}' \
#     -H 'Content-Type: application/json' \
#     https://$host:8000/api/firewall/rules
# }


# wait for api apistatus=`curl -k -X GET -u api:$apipassword https://$host:8000/api/config 2>&1`
# ./vnscubed.rb -K api -S $1 -H $2 reset_password --password "$3"
# ./vnscubed.rb -K api -S $3 -H $2 setup_admin_ui --enabled true --admin-username vnscubed --admin-password "$3"

# echo "Upload license"
# curl -v -k -X PUT -u api:$SecLinkPassword --data-binary @/tmp/Seclinklicense.txt -H 'Content-Type: text/plain' https://$SecLinkap:8000/api/license

# ## Settting licesne parameters on SecLink
# echo "Setting License Parameters"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap set_license_parameters \
#   --subnet 10.251.127.224/28 \
#   --managers 	10.251.127.237 \
#   --my-manager-vip 10.251.127.238 \
#   --clients 10.251.127.225 \
#   --asns "$ASN" \
#   --default false

# echo "Describe config:"
# curl -k -X GET -u api:$SecLinkPassword https://$SecLinkap:8000/api/config

# ## Generate keyset on SecLink
# echo "Generating Keyset on SecLink"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap setup_keyset --topology_name "$VPC" --token "$SecLinkTopoPassword"

# ## Wait for keyset generation to complete
# apistatus=`curl -k -X GET -u api:$apipassword https://$host:8000/api/keyset 2>&1`
#     echo $apistatus | grep '"keyset_present":false'

# ## Set peering on SecLink
# echo "Setting peering on SecLink"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap set_manager_id --id 1

# ## Create interface route on SecLink
# echo "Creating interface route on SecLink"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap add_route \
#   --cidr $SecLinkCIDR \
#   --interface "eth0" \
#   --gateway "$SECLINK_GW" \
#   --metric "0" \
#   --advertise "false"

# echo "Creating advertisement for seclink routes"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap add_route \
#   --cidr $SecLinkCIDR \
#   --interface "" \
#   --gateway "" \
#   --advertise "true"

# echo "Creating seclink route to fednet controller 1 SIP"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap add_route \
#   --cidr "$FedNeta1s/32" \
#   --interface "eth0" \
#   --gateway "$SECLINK_GW" \
#   --metric "0" \
#   --advertise "false"

# echo "Creating seclink route to fednet controller 2 SIP"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap add_route \
#   --cidr "$FedNeta2s/32" \
#   --interface "eth0" \
#   --gateway "$SECLINK_GW" \
#   --metric "0" \
#   --advertise "false"

# echo "Creating fednet ctr 1 route to seclink SIP"
# ./vnscubed.rb -K api -S $FedNetPassword -H $FedNeta1p add_route \
#   --cidr "$SecLinkas/32" \
#   --interface "eth0" \
#   --gateway "$PRIMARY_FEDNET_GW" \
#   --metric "0" \
#   --advertise "false"

# echo "Creating fednet ctr 2 route to seclink SIP"
# ./vnscubed.rb -K api -S $FedNetPassword -H $FedNeta2p add_route \
#   --cidr "$SecLinkas/32" \
#   --interface "eth0" \
#   --gateway "$SECONDARY_FEDNET_GW" \
#   --metric "0" \
#   --advertise "false"

# # Set topology names on SecLink
# echo "Setting Topology name on SecLink"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap edit_config --topology-name "$VPC"

# ## Set the container plugin network cidr for SecLink
# set_container_network $SecLinkPassword $SecLinkap $ContainerNetwork

# ## Set local private IP to secondary prive IP on SecLink
# echo "Setting private IP to secondary prive IP on SecLink"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap edit_ipsec_config --ipsec-local-ipaddress "$SecLinkas"

# echo "Sleeping 30 - waiting for ipsec subsystem to restart"
# sleep 30

# ## Create IPSec connection between SecLink and FedNet1
# echo "Creating seclink tunnel: Primary"
# SeclinkPrimaryTunnelResponse=`./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap create_ipsec_endpoint --name "$NAME_PRIMARY" --ipaddress "$FedNeta1s" --secret "$secretPSK" --pfs "false" --ike-version "2" --nat-t-enabled "true" --vpn-type "vti" --route-based-int-address "$PRIMARY_VTI_OUTER" --route-based-local "0.0.0.0/0" --route-based-remote "0.0.0.0/0" --extra_config "phase1=aes256_gcm-sha2_256-dh14 phase2=aes256_gcm mtu=8892"`
# echo "RESPONSE: $SeclinkPrimaryTunnelResponse"
# SecLinkTunnelIDprimary="$(echo "$SeclinkPrimaryTunnelResponse" | grep -w '^id\:' | cut -d " " -f2 | head -1)"
# echo "Creating seclink tunnel: Primary [created] [$SecLinkTunnelIDprimary]"

# echo "Creating Fednet tunnel: Primary"
# FedNetPrimaryTunnelResponse=`./vnscubed.rb -K api -S $FedNetPassword -H $FedNeta1p create_ipsec_endpoint --name "$NAME_PRIMARY" --ipaddress "$SecLinkas" --secret "$secretPSK" --pfs "false" --ike-version "2" --nat-t-enabled "true" --vpn-type "vti" --route-based-int-address "$PRIMARY_VTI_INNER" --route-based-local "0.0.0.0/0" --route-based-remote "0.0.0.0/0" --extra_config "phase1=aes256_gcm-sha2_256-dh14 phase2=aes256_gcm mtu=8892"`
# echo "RESPONSE: $FedNetPrimaryTunnelResponse"
# FedNetTunnelIDprimary="$(echo "$FedNetPrimaryTunnelResponse" | grep -w '^id\:' | cut -d " " -f2 | head -1)"
# echo "Creating fednet tunnel: Primary [created] [$FedNetTunnelIDprimary]"

# ## Create IPSec connection between SecLink and FedNet2
# echo "Creating seclink tunnel: Secondary"
# SeclinkSecondaryTunnelResponse=`./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap create_ipsec_endpoint --name "$NAME_SECONDARY" --ipaddress "$FedNeta2s" --secret "$secretPSK" --pfs "false" --ike-version "2" --nat-t-enabled "true" --vpn-type "vti" --route-based-int-address "$SECONDARY_VTI_OUTER" --route-based-local "0.0.0.0/0" --route-based-remote "0.0.0.0/0" --extra_config "phase1=aes256_gcm-sha2_256-dh14 phase2=aes256_gcm mtu=8892"`
# echo "RESPONSE: $SeclinkSecondaryTunnelResponse"
# SecLinkTunnelIDsecondary="$(echo "$SeclinkSecondaryTunnelResponse" | grep -w '^id\:' | cut -d " " -f2 | head -1)"
# echo "Creating seclink tunnel: Secondary [created] [$SecLinkTunnelIDsecondary]"

# echo "Creating Fednet tunnel: Secondary"
# FednetSecondaryTunnelResponse=`./vnscubed.rb -K api -S $FedNetPassword -H $FedNeta2p create_ipsec_endpoint --name "$NAME_SECONDARY" --ipaddress "$SecLinkas" --secret "$secretPSK" --pfs "false" --ike-version "2" --nat-t-enabled "true" --vpn-type "vti" --route-based-int-address "$SECONDARY_VTI_INNER" --route-based-local "0.0.0.0/0" --route-based-remote "0.0.0.0/0" --extra_config "phase1=aes256_gcm-sha2_256-dh14 phase2=aes256_gcm mtu=8892"`
# echo "RESPONSE: $FednetSecondaryTunnelResponse"
# FedNetTunnelIDsecondary="$(echo "$FednetSecondaryTunnelResponse" | grep -w '^id\:' | cut -d " " -f2 | head -1)"
# echo "Creating fednet tunnel: Secondary [created] [$FedNetTunnelIDsecondary]"

# ## Setup BGP peering on primary tunnels
# echo "Creating BGP Peering on primary tunnel: seclink side [ip=$PRIMARY_VTI_INNER_ADDRESS]"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap create_ebgp_peer \
#   --endpoint $SecLinkTunnelIDprimary \
#   --ipaddress $PRIMARY_VTI_INNER_ADDRESS \
#   --asn $FedNet1asn \
#   --add-network-distance "true" \
#   --add-network-distance-direction "out" \
#   --add-network-distance-hops "1" \
#   --access-list "in permit 10.0.0.0/8
# out permit $SecLinkCIDR"

# echo "Creating BGP Peering on primary tunnel: fednet side [ip=$PRIMARY_VTI_OUTER_ADDRESS]"
# ./vnscubed.rb -K api -S $FedNetPassword -H $FedNeta1p create_ebgp_peer \
#   --endpoint $FedNetTunnelIDprimary \
#   --ipaddress $PRIMARY_VTI_OUTER_ADDRESS \
#   --asn $ASN \
#   --add-network-distance "true" \
#   --add-network-distance-direction "in" \
#   --add-network-distance-hops "1" \
#   --access-list "out permit 10.0.0.0/8
# in permit $SecLinkCIDR"


# ## Setup BGP peering on secondary tunnels
# echo "Creating BGP Peering on secondary tunnel: seclink side [ip=$SECONDARY_VTI_INNER_ADDRESS]"
# ./vnscubed.rb -K api -S $SecLinkPassword -H $SecLinkap create_ebgp_peer \
#   --endpoint $SecLinkTunnelIDsecondary \
#   --ipaddress $SECONDARY_VTI_INNER_ADDRESS \
#   --asn $FedNet2asn \
#   --add-network-distance "true" \
#   --add-network-distance-direction "out" \
#   --add-network-distance-hops "2" \
#   --access-list "in permit 10.0.0.0/8
# out permit $SecLinkCIDR"


# echo "Creating BGP Peering on secondary tunnel: fednet side [ip=$SECONDARY_VTI_OUTER_ADDRESS]"
# ./vnscubed.rb -K api -S $FedNetPassword -H $FedNeta2p create_ebgp_peer \
#   --endpoint $FedNetTunnelIDsecondary \
#   --ipaddress $SECONDARY_VTI_OUTER_ADDRESS \
#   --asn $ASN \
#   --add-network-distance "true" \
#   --add-network-distance-direction "in" \
#   --add-network-distance-hops "2" \
#   --access-list "out permit 10.0.0.0/8
# in permit $SecLinkCIDR"


# if [ -z "${OnPremCIDRAccess+set}" ]; then
#   echo  "No onprem access requested"
# else
#   echo "Setting Firewall for onprem cidrs: $OnPremCIDRAccess"
#   set_firewall $OnPremCIDRAccess $SecLinkCIDR $SecLinkap $SecLinkPassword
# fi


azure_host = '52.173.16.57:8000'
aws_host = '3.223.172.217:8000'
api_password = '0q923jrojefn932'
aws_id = 'i-0319472c58e48d4cb'
azure_password = 'vnscubed'

import cohesivenet

azure_config = cohesivenet.Configuration()
azure_config.username = 'api'
azure_config.password = azure_password
azure_config.host = azure_host
azure_config.verify_ssl = False

aws_config = cohesivenet.Configuration()
aws_config.username = 'api'
aws_config.password = aws_id
aws_config.host = aws_host
aws_config.verify_ssl = False

vns3_aws = cohesivenet.VNS3Client(aws_config)
vns3_azure = cohesivenet.VNS3Client(azure_config)


def run():
    pass


# aws: wait for api
# aws: reset passwords
# aws: upload license
# aws: wait for api
# aws: set license parameters
# aws: generate keyset
# aws: wait for keyset
# aws: set controller id 
# aws: add route to azure controller
# aws: set topology name
# aws: set local ipsec address to secondary ip (if applicable)
# aws: Create ipsec endpoint to azure
# azure: wait for api
# azure: reset passwords
# azure: upload license
# azure: wait for api
# azure: set license parameters
# azure: wait for api
# azure: generate keyset
# azure: wait for keyset
# azure: set controller id 
# azure: add route to aws controller
# azure: set topology name
# azure: set local ipsec address to secondary ip (if applicable)
# azure: Create ipsec endpoint to aws
