#!/bin/bash

#RUN_ARCHETYPE="taf"
#GROUP_ID="com.ericsson.eniq"
#ARTIFACT_ID="eniq_infra_taf"
#declare -a DELIVERABLE=("ERICtest_CXP1234567" "ERICtest_CXP9999999");
#PARENT="ENIQ"

function runArchetype(){
	local temp=$1
	printf '========================================\n'
	echo ===== Running TAF Archetype for $temp =====
	printf '========================================\n'

	len=${#temp}-18
	len2=${#temp}-10
	deliver="${temp:7:$len}"
	cxp="${temp:$len2}"

	echo $deliver
	echo 'CXP: '$cxp

	remove='-testware'
	ARTIFACT_ID_wo_testware=${ARTIFACT_ID%$remove}
	ARTIFACT_ID_wo_dashes=${ARTIFACT_ID_wo_testware//[-]/}
	ARTIFACT_ID_testware="${ARTIFACT_ID_wo_dashes}-testware"

	echo 'Artifact ID without -testware: '$ARTIFACT_ID_wo_testware
	echo 'Artifact ID without dashes: '$ARTIFACT_ID_wo_dashes
	echo 'Artifact ID + -testware: '${ARTIFACT_ID_testware}

	case "$PARENT" in
			ENIQ)
				parentGroupId="com.ericsson.eniq.stats"
				parentVersion="1.0.1"
			  ;;
			cds)
				parentGroupId="com.ericsson.cds"
				parentVersion="1.0.83"
			  ;;
	esac

	mvn -B com.ericsson.cifwk.taf:taf-maven-plugin:archetype -DarchetypeGroupId=com.ericsson.cifwk -DarchetypeArtifactId=taf-archetype -DarchetypeVersion=3.0.5 -DgroupId="$GROUP_ID" -DartifactId=$ARTIFACT_ID_wo_dashes -Dversion=1.0.1-SNAPSHOT -DparentGroupId="$parentGroupId" -DparentArtifactId="integration" -DparentVersion=$parentVersion -DcxpNumber=$cxp -Dtaf_sdk=all -DinteractiveMode=false || { echo 'Maven Archetype Generate Failed' ; exit 1; }

	echo "${ARTIFACT_ID_wo_testware}" | grep -q '[-]'
	if [ $? = 0 ]; then
		find . -name "pom.xml" -exec sed -i "s/>${ARTIFACT_ID_testware}</>${ARTIFACT_ID}</g" {} \;
	fi


	mv "ERICTAF${ARTIFACT_ID_wo_dashes}_$cxp" ${temp}
	mv "ERICTAF${ARTIFACT_ID_wo_dashes}_operators" "ERICTAF${deliver}"_operators
	find . -name "pom.xml" -exec sed -i "s/>ERICTAF${ARTIFACT_ID_wo_dashes}_$cxp</>${temp}</g" {} \;
	find . -name "pom.xml" -exec sed -i "s/>ERICTAF${ARTIFACT_ID_wo_dashes}_operators</>ERICTAF${deliver}_operators</g" {} \;

	printf '===================================================\n'
	printf '== Updating parent to latest OSSRC integration pom ==\n'
	printf '===================================================\n'

	mvn versions:update-parent -B -V -N -DgenerateBackupPoms=false "-DparentVersion=[15.2.0,15.2.1)"

} 	


printf '========================================\n'
printf '=========== Cloning New Repo ===========\n'
printf '========================================\n'

git clone ssh://gerrit.ericsson.se:29418/OSS/$GROUP_ID/$ARTIFACT_ID || { echo 'Clone Failed: Check repo details' ; exit 1; }
cd $ARTIFACT_ID
git checkout master
ls
git remote set-url origin --push ssh://gerrit.ericsson.se:29418/OSS/$GROUP_ID/$ARTIFACT_ID
git remote -v

LISTA=( $DELIVERABLE )
listLeng=${#LISTA[@]}

for j in ${LISTA[@]};
do        
	runArchetype $j
	TEXT_CXP=$TEXT_CXP"<module>$j</module>"
done

LAST_PART=${LISTA[${#LISTA[@]} - 1]}


if (($listLeng>1)); then
	sed -i "s@<module>$LAST_PART</module>@$TEXT_CXP@" "./pom.xml"
fi
	
printf '=============================================\n'
printf '============== Repo created =================\n'
printf '=============================================\n'

ls

git add .
git commit -m "Ran TAF Archetype"
git push origin master || { echo 'Git Push Failed' ; exit 1; }

cd ..
rm -r $ARTIFACT_ID

