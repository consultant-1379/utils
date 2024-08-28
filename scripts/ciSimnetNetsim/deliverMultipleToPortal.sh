#!/bin/bash
#Author : xjagset(jagadish.sethi@wipro.com)

#Usage function showing how to use the script
usage ()
{
  echo "Usage: $cmd [-D for Debug] [-l datafile] [-g groupId] [-a artifactId] [-r Rstate_version] [-P product][-i intendedDrop] [-p filePath] [-f fileName] [-t packageType] [-u user] [-e email] [-o Task options either 1,2 or 3 ] " 1>&2
  printf " -l Absolute path of the datafile \n"
  printf " -D To run the script in DEBUG mode \n"
  printf " -P product eg: Netsim/Simnet\n"
  printf " -i Intended Drop eg: 16.0.1\n"
  printf " -p Absolute path or location of the package in the server eg: /home/ossrcdm/jagan\n"
  printf " -t packageType or type of the file eg: zip\n"
  printf " -u signum ID of the user eg: xjagset\n"
  printf " -e email ID of the user eg: jagadish.sethi@wipro.com\n"
  printf " -o Task Options either 1,2,or 3. Where \n"
  printf " 1 represents deliver to nexus and portal only\n"
  printf " 2 represents deliver to drop\n"
  printf " 3 represents deliver to nexus and drop\n"
  exit 1
}

# Parse arguments

[ $# -gt 0 ] || usage
while getopts ":l:P:i:p:t:u:e:o:D" opt; do
  case $opt in
    l)
      datafile=$OPTARG
      ;;
    P)
      product=$OPTARG
      ;;
    i)
      intendedDrop=$OPTARG
      ;;
    p)
      filePath=$OPTARG
      ;;
    t)
      packageType=$OPTARG
      ;;
    u)
      userId=$OPTARG
      ;;
    e)
      email=$OPTARG
      ;;
    o)
      taskOptions=$OPTARG
      ;;
    D)
      echo "Script is running in DEBUG mode."
      set -xv
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


deployPackage=""
GAVs=""
cat $datafile | while read line
do
   
    IN=${line##*:}
	set -- "$IN"
	IFS=" "; declare -a Array=($*)
	echo "< ${Array[@]}"
	echo "< ${Array[0]}"
	echo "< ${Array[1]}"
	echo "< ${Array[2]}"
        
	groupId=${Array[0]}
	artifactId=${Array[1]}
	fileName=${Array[2]}
	
	rstate=$(sh generatePackageVersion_copy.sh -p ${Array[1]})
	
	echo "Rstate is $rstate"
	
	
	if [[ "$deployPackage" == "" ]];then
		deployPackage+="$artifactId::$rstate"
	else
		deployPackage+="||$artifactId::$rstate"
	fi
	GAVs+="#$artifactId::$rstate::$groupId"

	echo $deployPackage
	echo $GAVs


    echo "Task option is $taskOptions"

    sh deliverToPortal_copy.sh -g $groupId -a $artifactId -r $rstate -P $product -i $intendedDrop -p $filePath -f $fileName -t $packageType -u $userId -e $email -o $taskOptions
	if [ $? -ne 0 ]; then
    echo "ERROR"
    exit 1;
	fi
	echo "SUCCESS"

        echo "GAVs=${GAVs}"  > /tmp/${BUILD_TAG}
cat /tmp/${BUILD_TAG}	
done
