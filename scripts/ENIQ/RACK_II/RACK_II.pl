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
#   RESP         : zsampri
#   DATE         : 09/10/2019
#   Description  : This Script is to install ENIQ on RACK server.

use strict;
use warnings;
no warnings 'uninitialized';
use POSIX qw(strftime);
use Expect;

my $exp;
my $timeout = 60;
my $def = 4800;
my $TMP_FILE = "/tmp/eniq_nmi_log.txt";
my $max;
my $muck;

$exp=Expect->spawn("/usr/bin/ssh root\@10.45.192.153") or die "Can not SSH $! \n";
if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
if($exp->expect($timeout, 'assword:')){$exp->send('DmMws@sept' . "\n");}

print "\nConnecting to ILO..!!\n";
$exp->expect($timeout, ']#');
$exp->send("ssh 10.82.16.107\r");
if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}

$exp->expect($timeout, '</>hpiLO->');
$exp->send("onetimeboot netdev1\r");

$exp->expect($timeout, '</>hpiLO->');
$exp->send("stop /system1/oemhp_vsp1\r");

$exp->expect($timeout, '</>hpiLO->');
$exp->send("reset /system1\r");

$exp->expect($timeout, '</>hpiLO->');
$exp->send("vsp\r");

$exp->expect($def, 'Select the server type you wish to install');
$exp->send("1\r");

$exp->expect($timeout, 'Available storage options:');
$exp->send("2\r");

$exp->expect($timeout, 'Enter the location of the licence file');
$exp->send("/net/159.107.177.74/eniq/eniq_build/license/LICENSE\r");

$exp->expect($timeout, 'Hit enter for (10.45.192.0:255.255.248.0)');
$exp->send("\r");

$exp->expect($timeout, 'Do you want to configure Backup Group (Y|N)?');
$exp->send("N\r");

$exp->expect($timeout, 'Select Range of disks you want to allocate to the FS Storage Pool');
$exp->send("\r");

$exp->expect($timeout, 'Enter IP address of Defaultrouter');
$exp->send("\r");

$exp->expect($timeout, 'Enter IP address of DNS SERVER(s)');
$exp->send("\r");

$exp->expect($timeout, 'Enter DNS domain name');
$exp->send("\r");

$exp->expect($timeout, 'Enter TIMEZONE');
$exp->send("\r");

$exp->expect($timeout, 'Select the partition plan you wish to install');
$exp->send("2\r");

$exp->expect($timeout, 'Please enter the IP address of the OSS Server');
$exp->send("1.1.1.1\r");

$exp->expect($timeout, 'Please enter the ENIQ feature software path');
$exp->send("/net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/FEATURE/\r");

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

$exp->expect($timeout, 'Enter password for DBA');
$exp->send("\r");

$exp->expect($timeout, 'Enter password for DC');
$exp->send("\r");

$exp->expect($timeout, 'Enter password for DCBO');
$exp->send("\r");

$exp->expect($timeout, 'Enter password for DCPUBLIC');
$exp->send("\r");

$exp->expect($timeout, "Are the values above correct (Yes/No)");
$exp->send("Yes\r");

if ($exp->expect($timeout, 'Successfully configured storage API')) {$exp->expect(5);}
if ($exp->expect($timeout, 'Connection to eniqs closed.')) {$exp->expect(5);}

$exp->soft_close();

`sleep 25200`;


`sleep 60`;
