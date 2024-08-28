#!/usr/bin/perl
use lib '/home/esjkadm100/perl5/lib/perl5/';
use strict;
use Getopt::Long;
use Expect;
my $serv_conn = $ARGV[0];
my $pack = $ARGV[1];
my $paths = $ARGV[2];
print "\n###############################\n";
print "About to Connect to UG server $serv_conn...\n";
print "###############################\n";
#####################################
# Calling Expect Module
#####################################
my $timeout = 20;
my $undef = undef;
my $exp = Expect->spawn("/usr/bin/ssh -l root ${serv_conn}.athtem.eei.ericsson.se" ) or die "Unable to spawn ssh to ${serv_conn}.\n";
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
#$exp->expect(100, ['#:', sub {$exp = shift; $exp->send("cd $paths\r");}]);
if($pack eq "all"){
$exp->expect(100, ['#:', sub {$exp = shift; $exp->send("scp $paths/* esjkadm100\@10.120.176.102:/proj/eniqdmt/procus\r");}]);
}
else{
$exp->expect(100, ['#:', sub {$exp = shift; $exp->send("scp $paths/$pack esjkadm100\@10.120.176.102:/proj/eniqdmt/procus\r");}]);
}
if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)')){
        $exp->send("yes\r");
}
$exp->expect(100, ['assword:', sub {$exp = shift; $exp->send("Naples\!0512\r");}]);
if($exp->expect($timeout, 'No such file or directory')){
                print("\n\nFile doesn't exist!!! Kindly check\n");
        $exp->send("exit (-1)\n");
                exit (-1);
}
$exp->expect(100, ['#:', sub {$exp = shift; $exp->send("\r");}]);
$exp->soft_close();

