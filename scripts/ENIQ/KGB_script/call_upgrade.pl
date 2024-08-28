#!/usr/bin/perl

use lib '/home/esjkadm100/perl5/lib/perl5/';
use strict;
use Getopt::Long;
use Expect;


my $IPADDRESS = $ARGV[0];
my $CHECKIN_BUILD_NUMBER = $ARGV[1];
my $WORKSPACE = $ARGV[2];
print "\n###############################\n";
#print "About to Connect to UG server $serv_conn...\n";
print "###############################\n";

#####################################
# Calling Expect Module
#####################################
my $timeout = 60;
my $undef = undef;
#my $exp = Expect->spawn("/usr/bin/ssh -l eniqdmt 10.120.176.102" ) or die "Unable to spawn ssh to ${serv_conn}.\n";
my $exp = Expect->spawn("/usr/bin/ssh -l statsjenki seliius28403.seli.gic.ericsson.se" ) or die "Unable to spawn ssh to seliius28403.seli.gic.ericsson.se.\n";
if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')){
        $exp->send('yes' . "\n");
}

if($exp->expect($timeout, 'assword')){
        #$exp->send("EStAts\(iDec\$2\(\)18\r");
        $exp->send("2020\#Jul\r");
}

#$exp->expect(2);
$exp->expect(50, ['seliius28403', sub {$exp = shift; $exp->send("\r");}]);
$exp->expect(60, ['seliius28403', sub {$exp = shift; $exp->send("cd /proj/eiffel013_config_fem5s11/eiffel_home/bin;module load perl/5.16.2\r");}]);
$exp->expect(60, ['seliius28403', sub {$exp = shift; $exp->send("/app/perl/5.16.2/RHEL6/bin/perl /proj/eiffel013_config_fem5s11/eiffel_home/bin/Install_Upgrade_TP_KGB.pl $IPADDRESS $CHECKIN_BUILD_NUMBER $WORKSPACE\r");}]);
$exp->expect(1500, ['seliius28403', sub {$exp = shift; $exp->send("\r");}]);
print "\n###############################\n";
$exp->soft_close();

#UpgradeServerConnection($mach);
