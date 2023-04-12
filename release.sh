#!/bin/bash

projectroot=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $projectroot
source .venv/bin/activate
CurVersion="$(cat cohesivenet/version.py | grep ^VERSION\ \= | cut -d' ' -f3 | sed 's/\"//g')"
BuildCommit=$(git log --pretty=tformat:"%h" -n1 cohesivenet) # commit for src directory
useTestRepo=false

echo "= Release version $CurVersion to pypi"
gitTag="v$CurVersion"

for i in "$@"
do
case $i in
    -t|--test)
    useTestRepo=true
    shift # past argument=value
    ;;
    *)
    	echo "Unknown Option $i"
    ;;
esac
done

make test

if [ $? == 1 ] ; then
    echo "Failed tests. Exiting."
    exit 1
fi

function createTag {
    git tag -a $gitTag -m "Release version $CurVersion. Build:$BuildCommit"
    git push origin $gitTag
}

function retag {
    git tag -d $gitTag
    git push --delete origin $gitTag
    createTag
}

if [ "$useTestRepo" = false ] ; then
    if git tag | grep -q $gitTag
    then 
        while true; do
            read -p "= Git tag for version $CurVersion already exists \
meaning this version may have been distributed already. \
Continue with release? D will delete and retag latest commit [Y/N/D]: " yn
            case $yn in
                [Yy]* ) break;;
                [Dd]* )
                    retag
                    break;;
                [Nn]* ) exit;;
                * ) echo "Please answer Y or N for yes or no.";;
            esac
        done
        echo "= Continuing with release git tag:"
        git log -1  v$CurVersion
    else
        echo "= Git tag does not exist for version $CurVersion. Creating."
        createTag
    fi
fi

make clean
make build

if [ "$useTestRepo" = true ] ; then
    twine upload --repository testpypi dist/*
else
    twine upload dist/*
fi

# make clean