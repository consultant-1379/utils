#!/bin/bash


createGroup="create-group"

echo "**********************************************************************************"
echo "******************* Checking if a new guard group is required ********************"
echo "**********************************************************************************"

if [ "$New_Guard_Group" = "true" ]; then
	for i in $Guard_Group_Members; do     members+=" -m"" "$i; done
    echo "**********************   Required  ********************************"
    echo "******************* list of members"$members "**********************"
    echo "********************************************************************"
    echo "********************Creating the new guard group"$Guard_group_name"********************"
    ssh -p 29418 gerrit.ericsson.se gerrit $createGroup $Guard_group_name -g ENIQ_CI_Execution $members
else 
	printf 'N/A\n'
fi


echo "*******************Creating the repository in Gerrit*****************"

echo "*******************Creating repository "$Repo" with required branches********************"

if [ "$Acceptance" = "None" ]; then
 	ssh -p 29418 gerrit.ericsson.se self-service create-project --parent OSS/ENIQ-Parent $Repo -b master -b Release --empty-commit -o ENIQ_CI_Execution
else
        ssh -p 29418 gerrit.ericsson.se self-service create-project --parent OSS/ENIQ-Parent $Repo -b master -b Acceptance -b Release --empty-commit -o ENIQ_CI_Execution
fi

echo "*******************Adding access rights for "$Guard_group_name"*******************" 

#module add git
#mkdir test
#cd test
#git init

git pull ssh://gerrit.ericsson.se:29418/$Repo refs/meta/config
ssh -p 29418 gerrit.ericsson.se gerrit ls-groups -v | grep $Guard_group_name > output.txt
GroupID_Sub=$(grep ^$Guard_group_name output.txt | cut -f 2)
rm output.txt
echo -e "$GroupID_Sub\t$Guard_group_name" >> groups

git add .
git commit -m "Added new group"
git push ssh://gerrit.ericsson.se:29418/$Repo HEAD:refs/meta/config

echo "************* groups file pushed **************"
echo "*************config file push******************"

echo -e "[access]
	inheritFrom = OSS/ENIQ-Parent
[access \"refs/*\"]
	owner = group ENIQ_CI_Execution
	create = group $Guard_group_name
	forgeCommitter = group $Guard_group_name
	pushTag = group $Guard_group_name
	label-Code-Review = -2..+2 group $Guard_group_name
	label-Verified = -1..+1 group $Guard_group_name
	rebase = group $Guard_group_name
	submit = group $Guard_group_name
[project]
	description = $Deliverable
[receive]
	requireChangeId = true
[submit]
	action = fast forward only
	mergeContent = false
[access \"refs/for/refs/heads/master\"]
	pushMerge = group $Guard_group_name
[access \"refs/heads/master\"]
	push = group $Guard_group_name
[plugin \"eiffel\"]
	enabled = true
	rmq-domain = eiffel004.camo.gerrit
	rmq-exchange = mb401-eiffel004
	rmq-server = amqp://mb401-eiffel004.mo.ca.am.ericsson.se:5672" > project.config

git add .
git commit -m "Added access controls"
git push ssh://gerrit.ericsson.se:29418/$Repo HEAD:refs/meta/config
cd ..
rm -rf test/

echo "************* end ******************"


#!/bin/bash


createGroup="create-group"

echo "**********************************************************************************"
echo "******************* Checking if a new guard group is required ********************"
echo "**********************************************************************************"

if [ "$New_Guard_Group" = "true" ]; then
	for i in $Guard_Group_Members; do     members+=" -m"" "$i; done
    echo "**********************   Required  ********************************"
    echo "******************* list of members"$members "**********************"
    echo "********************************************************************"
    echo "********************Creating the new guard group"$Guard_group_name"********************"
    ssh -p 29418 gerrit.ericsson.se gerrit $createGroup $Guard_group_name -g ENIQ_CI_Execution $members
else 
	printf 'N/A\n'
fi


echo "*******************Creating the repository in Gerrit*****************"

echo "*******************Creating repository "$Repo" with required branches********************"

if [ "$Acceptance" = "None" ]; then
 	ssh -p 29418 gerrit.ericsson.se self-service create-project --parent OSS/ENIQ-Parent $Repo -b master -b Release --empty-commit -o ENIQ_CI_Execution
else
        ssh -p 29418 gerrit.ericsson.se self-service create-project --parent OSS/ENIQ-Parent $Repo -b master -b Acceptance -b Release --empty-commit -o ENIQ_CI_Execution
fi

echo "*******************Adding access rights for "$Guard_group_name"*******************" 

#module add git
#mkdir test
#cd test
#git init

git pull ssh://gerrit.ericsson.se:29418/$Repo refs/meta/config
ssh -p 29418 gerrit.ericsson.se gerrit ls-groups -v | grep $Guard_group_name > output.txt
GroupID_Sub=$(grep ^$Guard_group_name output.txt | cut -f 2)
rm output.txt
echo -e "$GroupID_Sub\t$Guard_group_name" >> groups

git add .
git commit -m "Added new group"
git push ssh://gerrit.ericsson.se:29418/$Repo HEAD:refs/meta/config

echo "************* groups file pushed **************"
echo "*************config file push******************"

echo -e "[access]
	inheritFrom = OSS/ENIQ-Parent
[access \"refs/*\"]
	owner = group ENIQ_CI_Execution
	create = group $Guard_group_name
	forgeCommitter = group $Guard_group_name
	pushTag = group $Guard_group_name
	label-Code-Review = -2..+2 group $Guard_group_name
	label-Verified = -1..+1 group $Guard_group_name
	rebase = group $Guard_group_name
	submit = group $Guard_group_name
[project]
	description = $Deliverable
[receive]
	requireChangeId = true
[submit]
	action = fast forward only
	mergeContent = false
[access \"refs/for/refs/heads/master\"]
	pushMerge = group $Guard_group_name
[access \"refs/heads/master\"]
	push = group $Guard_group_name
[plugin \"eiffel\"]
	enabled = true
	rmq-domain = eiffel004.camo.gerrit
	rmq-exchange = mb401-eiffel004
	rmq-server = amqp://mb401-eiffel004.mo.ca.am.ericsson.se:5672" > project.config

git add .
git commit -m "Added access controls"
git push ssh://gerrit.ericsson.se:29418/$Repo HEAD:refs/meta/config
cd ..
rm -rf test/

echo "************* end ******************"



