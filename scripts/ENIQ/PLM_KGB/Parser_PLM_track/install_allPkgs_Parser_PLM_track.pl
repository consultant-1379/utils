#!/app/perl/5.16.2/RHEL6/bin/perl5.16.2
#
#-----------------------------------------------------------
# COPYRIGHT Ericsson Radio Systems  AB 2018
#
# The copyright to the computer program(s) herein is the
# property of ERICSSON RADIO SYSTEMS AB, Sweden. The
# programs may be usedand/or copied only with the written
# permission from ERICSSON RADIO SYSTEMS AB or in accordance
# with the terms and conditions stipulated in the agreement
# contract under which the program(s)have been supplied.
#-----------------------------------------------------------
#-----------------------------------------------------------
#
#   PRODUCT      : Delivery Management
#   RESP         : zsxxhem
#   DATE         : 4/8/2019
#   Description  : This Script is to install all Parsers and PF pkgs to vApp.

use strict;
use warnings;
no warnings 'uninitialized';
use POSIX qw(strftime);
use Expect;

my $exp;
my $timeout = 30;
my $def = 3600;
my $TMP_FILE = "/tmp/eniq_pf_kgb_log.txt";
my $max;
my $muck;


print "\nConnecting to eniqs..!!\n";
$exp=Expect->spawn("/usr/bin/ssh root\@eniqs") or die "Can not SSH and Clean eniqs $! \n";
if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
$exp->expect($timeout, '#:');

$exp->send("val=`cat /eniq/admin/version/eniq_status | grep Shipment | cut -d\" \" -f2 | cut -d\"_\" -f4`\r");
$exp->expect($timeout, '#:');
$exp->send("shipment=\$val\"_Linux\"\r");
$exp->expect($timeout, '#:');
$exp->send("tmpFolder=`echo \$shipment | sed 's/\\.//g'`\r");
$exp->expect($timeout, '#:');
$exp->send("num=`echo \$shipment | cut -d\".\" -f2`\r");
$exp->expect($timeout, '#:');
$exp->send("numToAlpha=( ['1']='A.1' ['2']='B' ['3']='B.1' ['4']='C')\r");
$exp->expect($timeout, '#:');
$exp->send("echo \"val - \$val, shipment - \$shipment, tmpFolder - \$tmpFolder, num - \$num\"\r");
$exp->expect($timeout, '#:');

print "\nExtracting the core package..!!\n";
$exp->send("cd /eniq/installation/core_install/bin\r");
$exp->expect($timeout, '#:');
$exp->send("bash ./unpack_core_sw.bsh -a create -d /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/\${shipment}/eniq_base_sw/ -p \${tmpFolder}\r");
$exp->expect($timeout, 'Enter [Yes | No] (case sensitive)');
$exp->send("Yes\r");
$exp->expect($timeout, '#:');

print "\nInstalling all Platform Packages..!!\n";
$exp->send("cd /var/tmp/upgrade/\${tmpFolder}/core_install/bin/\r");
$exp->expect($timeout, '#:');
$exp->send("bash ./upgrade_eniq_sw.bsh -A upgrade_platform_only -D /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/\${shipment}/eniq_base_sw/ -P \${tmpFolder} -O /net/10.45.192.153/JUMP/OM_LINUX_MEDIA/OM_LINUX_019_2/\${val} -q\r");
$exp->expect($def, '#:');

print "\nInstalling all Platform Packages..!!\n";
$exp->send("cd /var/tmp/upgrade/\${tmpFolder}/core_install/bin/\r");
$exp->expect($timeout, '#:');
$exp->send("bash /eniq/installation/core_install/bin/upgrade_eniq_sw.bsh  -A upgrade_feature_only -f  /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/Features_19\${numToAlpha[\$num]}_\${shipment} -q\r");

#Select the Features to be installed from the list.
$exp->log_file("$TMP_FILE", "w");
$exp->expect(300, "Select range of ENIQ Features to be upgraded");
$exp->expect(5);

$exp->log_file(undef);

my $entryfull = `cat ${TMP_FILE} | egrep "^\[[0-9]" | tail -1 | awk -F "]" '{print \$1}'`;
chomp($entryfull);
($max, $muck) = split (/ /, $entryfull);
$max =~ s/\[//;
$max =~ s/\]//;
chomp($max);
$max =~ s/\s+//g;
print "Total number of features is $max \n";

$exp->expect(300, "using the following format");
my $features="1-".$max;
chomp($features);

printf("Choosing features $features for upgrade\n");
$exp->send("$features\r");
$exp->expect(5);

if ($exp->expect(200, "Do you wish to continue to update the features above (Yy/Nn)")) {
$exp->send("Y\r");
}

$exp->expect(30, "Enter [Yes|No] (case sensitive) : ");
$exp->send("Yes\r");
$exp->expect(5);
$exp->expect($def, '#:');

$exp->soft_close();

