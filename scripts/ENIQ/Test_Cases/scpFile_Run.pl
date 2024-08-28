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
#   DATE         : 3/14/2019
#   Description  : This Script is get the Platform packages and its related info according to SCM polling.
#   REV          : A1
# --------------------------------------------------------------

use strict;
use warnings;
no warnings 'uninitialized';
use POSIX qw(strftime);
use Expect;
my $run_time=strftime "%Y%m%d-%H_%M_%S", localtime;

my $def = 360;
my $timeout = 30;
my $exp;
my $selix069 = "selix069.lmera.ericsson.se";
my $selixPW = "EStAts(iDec\$2()18";

#Coping the runSanityTestCases.py file to selix069
print "\nCoping the runSanityTestCases.py file to selix069...!\n\n";
$exp=Expect->spawn("/usr/bin/scp runSanityTestCases.py eniqdmt\@$selix069:/tmp/TestCases/ ") or die "Can not scp to $selix069 $! \n";
if ($exp->expect($timeout, 'assword:')){$exp->send($selixPW . "\n");}
$exp->expect(5);
$exp->soft_close();

#Scp runSanityTestCases.py file to server
print "\nScp runSanityTestCases.py file to server...!\n\n";
$exp=Expect->spawn("/usr/bin/ssh eniqdmt\@$selix069") or die "Can not SSH $selix069 $! \n";
if ($exp->expect($timeout, 'assword:')){$exp->send($selixPW . "\n");}
$exp->expect(10);

$exp->expect($timeout, ['eniqdmt', sub {$exp = shift; $exp->send("/usr/bin/rm /tmp/TestCases/TestCaseLog.txt\r");}]);
$exp->expect($timeout, ['eniqdmt', sub {$exp = shift; $exp->send("/usr/bin/scp /tmp/TestCases/runSanityTestCases.py root\@ieatrcx6575:/tmp/runSanityTestCases.py\r");}]);
$exp->expect($timeout, ['assword:', sub {$exp = shift; $exp->send("shroot12\r");}]);
$exp->expect(15);

$exp->expect($timeout, ['eniqdmt', sub {$exp = shift; $exp->send("/usr/bin/ssh root\@ieatrcx6575 -C 'python /tmp/runSanityTestCases.py' > /tmp/TestCases/TestCaseLog.txt\r");}]);
$exp->expect($timeout, ['assword:', sub {$exp = shift; $exp->send("shroot12\r");}]);
$exp->expect(180);

$exp->expect($timeout, ['eniqdmt', sub {$exp = shift; $exp->send("cat /tmp/TestCases/TestCaseLog.txt\r");}]);
$exp->expect($timeout, ['eniqdmt', sub {$exp = shift; $exp->send("exit\r");}]);
$exp->soft_close();

print "\n\nEnd of the TestCases Excecution!!\n";