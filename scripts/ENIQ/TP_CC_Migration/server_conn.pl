#!/usr/bin/perl

use lib '/home/esjkadm100/perl5/lib/perl5/';
use strict;
use Getopt::Long;
use Expect;


my $serv_conn = $ARGV[0];
my $pack = $ARGV[1];
print "\n###############################\n";
print "About to Connect to UG server $serv_conn...\n";
print "###############################\n";

#####################################
# Calling Expect Module
#####################################
my $timeout = 20;
my $undef = undef;
#$exp = Expect->spawn("/usr/bin/ssh -p 2251 root\@$ip_addr" ) or die "Unable to spawn ssh  to ${serv_conn}.\n";
my $exp = Expect->spawn("/usr/bin/ssh -p 2251 -l root ${serv_conn}.athtem.eei.ericsson.se" ) or die "Unable to spawn ssh to ${serv_conn}.\n";
if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')){
        $exp->send('yes' . "\n");
}

if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)')){
        $exp->send('yes' . "\n");
}

$exp->expect($timeout,
    [ 'assword: ' => sub {
        $exp->send("shroot12\r");
        exp_continue; }
    ],

'-re', qr'[^.*->#] $' => sub {
    exp_continue; }
);

#$exp->expect(2);
$exp->expect(100, ['#:', sub {$exp = shift; $exp->send("cd /eniq/home/dcuser/\r");}]);
$exp->expect(100, ['#:', sub {$exp = shift; $exp->send("scp $pack eniqdmt\@10.120.176.102:/home/eniqdmt/zsampri\r");}]);
if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)')){
        $exp->send("yes\r");
}
$exp->expect(100, ['assword:', sub {$exp = shift; $exp->send("EStAts\(iDec\$2\(\)18\r");}]);
if($exp->expect($timeout, 'No such file or directory')){
                print("\n\nFile doesn't exist!!! Kindly check\n");
        $exp->send("exit (-1)\n");
                exit (-1);
}
$exp->expect(100, ['#:', sub {$exp = shift; $exp->send("\r");}]);
$exp->soft_close();
my $exp = Expect->spawn("/usr/bin/ssh -l eniqdmt 10.120.176.102" ) or die "Unable to spawn ssh to ${serv_conn}.\n";
if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')){
        $exp->send('yes' . "\n");
}

if($exp->expect($timeout, 'assword')){
        $exp->send("EStAts\(iDec\$2\(\)18\r");
}

#$exp->expect(2);
$exp->expect(60, ['$', sub {$exp = shift; $exp->send("cd /home/eniqdmt/zsampri/\r");}]);
$exp->expect(60, ['$', sub {$exp = shift; $exp->send("chmod 777 $pack\r");}]);
$exp->expect(60, ['$', sub {$exp = shift; $exp->send("scp $pack esjkadm100\@fem6s11-eiffel013.eiffel.gic.ericsson.se:/proj/eiffel013_config_fem6s11/slaves/RHEL_ENIQ_STATS/git_work/locks\r");}]);
if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')){
        $exp->send('yes' . "\n");
}

if($exp->expect($timeout, 'assword')){
        $exp->send("Naples\!0512\r");
}
if($exp->expect($timeout, 'No such file or directory')){
                print("\n\nFile doesn't exist!!! Kindly check\n");
        $exp->send("exit (-1)\n");
                exit (-1);
}
$exp->expect(100, ['$', sub {$exp = shift; $exp->send("rm $pack\r");}]);
if($exp->expect($timeout, '?')){
        $exp->send('yes' . "\n");
}
$exp->expect(100, ['$', sub {$exp = shift; $exp->send("\r");}]);
$exp->soft_close();

#UpgradeServerConnection($mach);