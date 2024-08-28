#!/usr/bin/perl -w

use strict;
use Getopt::Long;							 
use Expect;
use File::Basename;
use File::Copy;

my $timeout = 20;
my $exp;
my $hostname = $ARGV[0];
my $Shipment = $ARGV[1];
my $mws = $ARGV[2];
my $pwd = "";

my @shp = split('\.', $Shipment);
my $Release = $shp[0]."_".$shp[1]; 
my $TEMP_FILE = "/JUMP/OM_LINUX_MEDIA/OM_LINUX_0".$Release."/".$Shipment."/om_linux/patch/bin/nfs_patch_osbackup";

sub server_connection
{
	if ($mws eq "10.45.192.153")
		{$pwd="DmCiMws\@2020";}
	elsif($mws eq "10.45.192.134")
		{$pwd="Assure5CI";}
	$exp=Expect->spawn("/usr/bin/ssh root\@$mws") or die "Can not SSH $mws $! \n";
    	if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
   	if ($exp->expect($timeout, 'password:')){$exp->send($pwd."\r");}
}

sub remove
{

    $exp->expect(20, '#');
    print "*****Removing directory for $hostname if already exist*****\r";
    $exp->send("$TEMP_FILE remove \r");
	if ($exp->expect(10, 'Enter client hostname :')){$exp->send($hostname."\r");}
    $exp->expect(20, '#');
	
}
sub add
{
    $exp->expect(20, '#');
    print "*****Adding directory for $hostname*****\r";
    $exp->send("$TEMP_FILE add \r");
	if ($exp->expect(10, 'Enter client hostname :')){$exp->send($hostname."\r");}
    $exp->expect(20, '#');
}

server_connection();
remove();
add();
