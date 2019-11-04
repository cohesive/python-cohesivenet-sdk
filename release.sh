#!/bin/bash

projectroot=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $projectroot
source .venv/bin/activate
CurVersion="$(cat cohesivenet/version.py | cut -d' ' -f3 | sed 's/\"//g')"

echo "= Release version $CurVersion to pypi"

if git tag | grep -q $CurVersion
then 
    while true; do
        read -p "= Git tag for version $CurVersion already exists \
meaning this version may have been distributed already. \
Continue with release? [Y/N]: " yn
        case $yn in
            [Yy]* ) break;;
            [Nn]* ) exit;;
            * ) echo "Please answer Y or N for yes or no.";;
        esac
    done
    echo "= Continuing with release git tag:"
    git log -1  v$CurVersion
else
   echo "= Git tag does not exist for version $CurVersion. Creating."
   gitTagVersion="v$CurVersion"
   git tag -a $gitTagVersion -m "Release version $CurVersion"
   git push origin $gitTagVersion
fi

make
twine upload dist/*