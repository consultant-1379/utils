#!/bin/bash
#Author : xjagset(jagadish.sethi@wipro.com)


#Initialisation
product="Simnet/Netsim"

#Usage function showing how to use the script
usage ()
{
  echo "Usage: $cmd [-p for packageName] [-d for drop] [-P for product]" 1>&2
  printf " -p package name eg: ERICurbcttest2_APR9019992\n"
  printf " -d drop name eg: 16.0.1\n"
  printf " -P Product name eg: Simnet/Netsim\n"


  exit 1
}

# Parse arguments

[ $# -gt 0 ] || usage
while getopts ":p:d:P:" opt; do
  case $opt in
    p)
      package=$OPTARG
      ;;
    d)
      drop=$OPTARG
      ;;
    P)
      product=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      usage
      exit 1
      ;;
  esac
done

fetch_packageLatestVersion()
{
	curl --request GET "https://cifwk-oss.lmera.ericsson.se/getDropContents/?drop=$drop&product=$product&pretty=true" > JSON_output.json
	listOfNames=$(cat JSON_output.json | grep -i name)
	versions=$(cat JSON_output.json | grep -i version)
	listOfVersions=($versions)
	packageName="\"$package\","
	i=0
	for name in $listOfNames
	do
#		echo "$name ${listOfVersions[$i]}"
		if [ $name == "$packageName" ]; then
			packageVersion=${listOfVersions[$i]}
		fi
		i=$((i+1))
	done
	packageVersion=$(echo $packageVersion | sed -e 's:"::g')
	echo $packageVersion
}




increment_version ()
{
	IN=${1}
	set -- "$IN"
	IFS="."; declare -a Array=($*)
	num=${Array[2]}

	num=`expr $num + 1`
	echo "${Array[0]}.${Array[1]}.$num"

}


packageInfo=$(curl --request GET "https://cifwk-oss.lmera.ericsson.se/dmt/getLatestPackageObj/?package=$package")
read version groupId <<<$(IFS="::"; echo $packageInfo)
#echo $version $groupId
echo $packageInfo | grep -i "ERROR" | wc -l >out.txt

value=$(cat out.txt)
if [ $value == "0" ]; then
incrementedVersion=$(increment_version $version)
else
#echo "ERROR Response means package doesn't exist so creating new version"
incrementedVersion=1.0.1
fi



echo $incrementedVersion

