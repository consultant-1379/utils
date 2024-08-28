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
#   DATE         : 4/23/2019
#   Description  : This Script is to install all Parsers and PF pkgs to vApp.

use strict;
use warnings;
no warnings 'uninitialized';
use POSIX qw(strftime);
use Expect;

my $exp;
my $timeout = 30;
my $def = 54800;
my $TMP_FILE = "/tmp/eniq_nmi_log.txt";
my $max;
my $muck;

print "\nConnecting to eniqs..!!\n";
$exp=Expect->spawn("/usr/bin/ssh root\@eniqs") or die "Can not SSH and Clean eniqs $! \n";
if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
$exp->expect($timeout, '#:');

#print "\nCommenting the Stagelist stages..!!\n";
#$exp->send("sed -i 's/install_ENIQ_platform/#install_ENIQ_platform/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
#$exp->send("sed -i 's/install_ENIQ_features/#install_ENIQ_features/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
#$exp->send("sed -i 's/activate_ENIQ_features/#activate_ENIQ_features/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
#$exp->send("sed -i 's/setup_SMF_scripts/#setup_SMF_scripts/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
#$exp->send("sed -i 's/install_extra_fs/#install_extra_fs/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
#$exp->send("sed -i 's/install_rolling_snapshot/#install_rolling_snapshot/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
#$exp->send("sed -i 's/validate_SMF_contracts/#validate_SMF_contracts/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
#$exp->send("sed -i 's/add_alias_details_to_service_names/#add_alias_details_to_service_names/g' /eniq/installation/core_install/etc/stats_eniq_stats_stagelist\r");
#$exp->expect($timeout, '#:');
$exp->send("\r");

#print "\nConnecting to eniqs..!!\n";
#$exp=Expect->spawn("/usr/bin/ssh root\@eniqs") or die "Can not SSH and Clean eniqs $! \n";
#if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
#if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
$exp->expect($timeout, '#:');
print "\nQuestion and Answers..!!\n";
$exp->send("bash /eniq/installation/core_install/bin/eniq_core_install.bsh\r");
$exp->expect($def, 'Select the server type you wish to install');
$exp->send("1\r");

$exp->expect($timeout, 'Select the storage that the ENIQ system will be installed on');
$exp->send("1\r");
$exp->expect($def, '[2] IPv6');
$exp->send("1\r");
$exp->expect($timeout, 'Hit enter for (unity)');
$exp->send("local\r");

$exp->expect($timeout, 'Enter the location of the licence file');
$exp->send("/net/10.45.192.153/JUMP/LICENE\r");
#$exp->send("/net/159.107.177.74/eniq/eniq_build/license/LICENE\r");

$exp->expect($timeout, 'Hit enter for (192.168.0.0:255.255.0.0)');
$exp->send("\r");

$exp->expect($timeout, 'Select two group interfaces from the list above separated by a space (Example :<Interface_1> <Interface_2>)');
$exp->send("ens192 ens256\r");

$exp->expect($timeout, 'Enter the IP address of the PM Services Group (Example :10.25.46.130)');
$exp->send("192.168.0.51\r");

$exp->expect($timeout, 'Enter the netmask address for the PM Services Group (Example :255.255.249.0)');
$exp->send("255.255.0.0\r");

$exp->expect($timeout, 'Enter the Gateway IP address of the PM Services Group (Example :10.0.0.1)');
$exp->send("192.168.0.1\r");

$exp->expect($timeout, 'Enter the IP address of at least two highly available servers in the same subnet as PM Services Group (separated by comma)');
$exp->send("10.45.192.134,172.16.30.1\r");

$exp->expect($timeout, 'Do you want to configure Backup Group (Y|N)?');
$exp->send("N\r");

$exp->expect($timeout, 'Is the information above correct (Yes|No)');
$exp->send("Yes\r");

if ($exp->expect($timeout, 'Successfully configured storage API')) {$exp->expect(5);}
if ($exp->expect($timeout, 'Connection to eniqs closed.')) {$exp->expect(5);}

$exp->soft_close();

`sleep 300`;

print "\nConnecting to eniqs..!!\n";
$exp=Expect->spawn("/usr/bin/ssh root\@eniqs") or die "Can not SSH and Clean eniqs $! \n";
if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
$exp->expect($timeout, '#:');

#print "\nQuestion and Answers..!!\n";
$exp->send("bash /eniq/installation/core_install/bin/eniq_core_install.bsh\r");
$exp->expect($timeout, 'Enter the console IP address of the NAS');
$exp->send("172.16.30.18\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas1 (1 of 8)');
$exp->send("172.16.30.14\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas2 (2 of 8)');
$exp->send("172.16.30.16\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas3 (3 of 8)');
$exp->send("172.16.30.14\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas4 (4 of 8)');
$exp->send("172.16.30.16\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas5 (5 of 8)');
$exp->send("172.16.30.14\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas6 (6 of 8)');
$exp->send("172.16.30.16\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas7 (7 of 8)');
$exp->send("172.16.30.14\r");

$exp->expect($timeout, 'Enter the virtual IP address for nas8 (8 of 8)');
$exp->send("172.16.30.16\r");

$exp->expect($timeout, 'Enter the name of the primary NAS storage pool (max. 7 characters)');
$exp->send("eniqs\r");

$exp->expect($timeout, "Enter the password for user 'master' in the NAS system");
$exp->send("master\r");

if ($exp->expect($timeout, "Re-Enter the password for user 'master' in the NAS system")) {$exp->send("master\r");}

$exp->expect($timeout, "Enter the password for user 'support' in the NAS system");
$exp->send("symantec\r");

if ($exp->expect($timeout, "Re-Enter the password for user 'support' in the NAS system")) {$exp->send("symantec\r");}

$exp->expect($timeout, 'Are the values above correct (Yes/No)');
$exp->send("Yes\r");

$exp->expect($timeout, 'Select Range of disks you want to allocate to the eniq_stats_pool FS Storage Pool');
$exp->send("7\r");

$exp->expect($timeout, 'Select the disk you want to allocate for IQ SYS MAIN database usage');
$exp->send("2\r");

$exp->expect($timeout, 'Select Range of disks you want to allocate for MainDB database usage');
$exp->send("3,4\r");

$exp->expect($timeout, 'Select Range of disks you want to allocate for TempDB database usage');
$exp->send("1\r");

$exp->expect($timeout, 'Are the disk allocations above correct (Yy/Nn)');
$exp->send("Y\r");

$exp->expect($timeout, "Enter IP address of Defaultrouter");
$exp->send("\r");

$exp->expect($timeout, "Enter IP address of DNS SERVER(s)");
$exp->send("192.168.0.1\r");

$exp->expect($timeout, 'Enter DNS domain name');
$exp->send("athtem.eei.ericsson.se\r");

$exp->expect($timeout, 'Enter TIMEZONE');
$exp->send("\r");

$exp->expect($timeout, "Enter Amount of Shared Memory to Allocate to IQ in Mbytes");
$exp->send("\r");

$exp->expect($timeout, "Select the partition plan you wish to install");
$exp->send("2\r");

$exp->expect($timeout, 'Please enter the IP address of the OSS Server');
$exp->send("1.1.1.1\r");

$exp->expect($timeout, 'Please enter the ENIQ feature software path');
$exp->send("/net/10.45.192.134/JUMP/ENIQ_STATS/ENIQ_STATS/FEATURE/\r");

$exp->log_file("$TMP_FILE", "w");
$exp->expect($timeout, "Select the ENIQ Features numbers you wish to");
$exp->log_file(undef);

my $entryfull = `cat ${TMP_FILE} | egrep "^\[[0-9]" | tail -1 | awk -F "]" '{print \$1}'`;
chomp($entryfull);
($max, $muck) = split (/ /, $entryfull);
$max =~ s/\[//;
$max =~ s/\]//;
chomp($max);
$max =~ s/\s+//g;
print "Total number of features is $max \n";
my $features="1-".$max;
chomp($features);

printf("Choosing features $features for upgrade\n");

$exp->send("$features\r");

$exp->expect($timeout, "Are the values above correct (Yes/No)");
$exp->send("Yes\r");

if ($exp->expect($timeout, 'Enter password for DBA')) {$exp->send("\r");}
#if ($exp->expect($timeout, 'Re-Enter password for DBA')) {$exp->send("Dba12#\r");}
if ($exp->expect($timeout, 'Enter password for DC')) {$exp->send("\r");}
#if ($exp->expect($timeout, 'Re-Enter password for DC')) {$exp->send("Dc12#\r");}
if ($exp->expect($timeout, 'Enter password for DCBO')) {$exp->send("\r");}
#if ($exp->expect($timeout, 'Re-Enter password for DCBO')) {$exp->send("Dcbo12#\r");}
if ($exp->expect($timeout, 'Enter password for DCPUBLIC')) {$exp->send("\r");}
#if ($exp->expect($timeout, 'Re-Enter password for DCPUBLIC')) {$exp->send("Dcpublic12#\r");}
if ($exp->expect($timeout, 'Are the values above correct (Yes/No)')) {$exp->send("Yes\r");}
if ($exp->expect($timeout, 'Are the above values correct? (Yes/No)')) {$exp->send("Yes\r");}

if ($exp->expect($timeout, 'Windows Server is Configured or not? [y/n]')) {$exp->send('n' . "\n");}

$exp->expect($def, 'ENIQ SW successfully installed');
$exp->expect(5);
$exp->soft_close();

`sleep 60`;
print "==============>NMI Installed Successfully<==============";
