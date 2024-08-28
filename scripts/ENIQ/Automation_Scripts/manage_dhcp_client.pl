#!/usr/bin/perl -w
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
#   RESP         : zpunvai
#   DATE         : 28/04/2021
#   Description  : This Script is remove and add the DHCP client
#   REV          : A1
# --------------------------------------------------------------


use strict;
use Getopt::Long;
use Expect;
use File::Basename;
use File::Copy;

# ********************************
#
# CONFIGURATION SECTION
#
# ********************************

my $SPRINT = $ARGV[0];
my $server = $ARGV[1];
my $ipAddress = $ARGV[2];
my $netmask = $ARGV[3];
my $macAddress = $ARGV[4];
my $ipv6 = $ARGV[5];
my $timeZone = $ARGV[6];
my $Rhel = $ARGV[7];
my $Patch = $ARGV[8];
my $mws = $ARGV[9];
my $len=@ARGV;
my @param = @ARGV[10..$len];
my $install_params = join(' ', @param);

#my $linux_MWS = "10.45.192.153";
my $timeout = 20;
my $exp;
my $TEMP_FILE = "/tmp/dhcp_client_Log.txt";
my @newShip = split("_", $SPRINT);
my $Shipment = $newShip[0];
my $breakLoop = 'No';
my $kick_menu;
my $patch_menu;
sub remove_dhcp_client
{
    $exp=Expect->spawn("/usr/bin/ssh root\@$mws") or die "Can not SSH $mws $! \n";
    if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
    if ($exp->expect($timeout, 'assword:')){$exp->send('DmCiMws@2020' . "\n");}
    $exp->expect(30, '#');

    print "\n\nRemoving the ${server} DHCP client..!!\n\n";
    $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a remove -c ${server} -N\r");

        if ($exp->expect($timeout, 'Removed kickstart client')) {
                print "*" x 70;
                print "\n    REMOVED THE CLIENT $server FROM MWS $mws ..!!\n";
                print "*" x 70;
                print "\n\n";
        }
        else{
                print "*" x 70;
                print "\n    CLIENT $server IS NOT ADDED IN $mws MWS..!!\n";
                print "*" x 70;
                print "\n\n";
                }
    $exp->expect(60, '#');
}

sub add_dhcp_client
{
    print "\n\nGetting needed info..!!\n\n";
    $exp->log_file("$TEMP_FILE", "w");
    $exp->send("find /JUMP/ENIQ_STATS/ENIQ_STATS/ -name \".eniq_stats_identity\" | sort > /tmp/app_media\r");
    $exp->expect(5, '#');
    $exp->send("find /JUMP/LIN_MEDIA/ -name \".linux_boot_media\" | sort > /tmp/kick_menu\r");
    $exp->expect(5, '#');
    $exp->send("find /JUMP/INSTALL_PATCH_MEDIA/ -name \".patch_boot_media\" | sort > /tmp/patch_menu\r");
    $exp->expect(5, '#');
    $exp->send("find /JUMP/OM_LINUX_MEDIA/ -name \".om_linux_identity\" | sort > /tmp/om_location\r");
    $exp->expect(5, '#');
    $exp->send("app_media=`grep -rn \"$SPRINT/\" /tmp/app_media | cut -d\":\" -f1 | xargs`\r");
    $exp->expect(5, '#');
    $exp->send("kick_menu=`grep -rn \"LIN_MEDIA\" /tmp/kick_menu | tail -1 | cut -d\":\" -f1 | xargs`\r");
    $exp->expect(5, '#');
    $exp->send("patch_menu=`grep -rn \"INSTALL_PATCH\" /tmp/patch_menu | tail -1 | cut -d\":\" -f1 | xargs`\r");
    $exp->expect(5, '#');
    $exp->send("om_location=`grep -rn \"$Shipment/\" /tmp/om_location | cut -d\":\" -f1 | xargs`\r");
    $exp->expect(5, '#');
    $exp->send("echo OM_LOCATION : \$om_location\r");
    $exp->expect(5, '#');
    #$exp->send("echo PATCH_MENU : \$patch_menu\r");
    #$exp->expect(5, '#');
    #$exp->send("echo KICK_MENU : \$kick_menu\r");
    #$exp->expect(5, '#');
    $exp->send("echo APP_MEDIA : \$app_media\r");
    if ($Rhel eq "7.9"){
        $kick_menu = "1";}
    if ($Patch eq "3.0.8"){
        $patch_menu = "1";}
    elsif ($Patch eq "3.0.7"){
        $patch_menu = "3"}
    elsif ($Patch eq "3.0.9"){
        $patch_menu = "5"}
    elsif ($Patch eq "3.0.10"){
        $patch_menu = "2"} 

    $exp->expect(30);
    $exp->log_file(undef);

    my $om_location = `cat $TEMP_FILE | grep OM_LOCATION | tail -1 | sed 's/OM_LOCATION ://g'`;
    #my $patch_menu = `cat $TEMP_FILE | grep PATCH_MENU | tail -1 | sed 's/PATCH_MENU ://g'`;
    #my $kick_menu = `cat $TEMP_FILE | grep KICK_MENU | tail -1 | sed 's/KICK_MENU ://g'`;
    my $app_media = `cat $TEMP_FILE | grep APP_MEDIA | tail -1 | sed 's/APP_MEDIA ://g'`;

        print "\n***\napp_media=$app_media kick_menu=$kick_menu om_location=$om_location patch_menu=$patch_menu***\n";

    print "\n\nCreating the ${server} DHCP client..!!\n\n";
    $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a add\r");
    if($exp->expect($timeout, 'Enter the client hostname')) {$exp->send("$server\r");}
    if($exp->expect($timeout, 'Enter the IP address of')){$exp->send("$ipAddress\r");}
    if($exp->expect($timeout, 'Enter the IP Netmask of')){$exp->send("$netmask\r");}
    if($exp->expect($timeout, 'Please enter the MAC address for')){$exp->send("$macAddress\r");}
    if($exp->expect($timeout, 'Do you want IPV6 enabled - YES/NO?')){$exp->send("$ipv6\r");}

    if($exp->expect($timeout, 'Enter the Timezone to be set for')) {$exp->send("$timeZone\r");}
        if($exp->expect($timeout, 'ERROR: Script aborted')){
                print "*" x 70;
                print "\n    PLEASE ADD THE CLIENT $server TO NETWORK..!!\n";
                print "*" x 70;
                print "\n\n";
                exit 3;
        }
    if($exp->expect($timeout, 'Select the application type you wish to install on')){$exp->send("1\r");}
    # if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
    # if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
    # if($exp->expect($timeout, 'Select number of the area you wish to use')){$exp->send("$app_media\r");}
    # if($exp->expect($timeout, 'Select the kickstart you wish to use for')){$exp->send("$kick_menu\r");}

    # if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
    # if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
    # if($exp->expect($timeout, 'Select number of the O&M Linux media you wish to use')) {$exp->send("$om_location\r");}
    # if($exp->expect($timeout, 'Select the install patch kickstart you wish to use for')){$exp->send("$patch_menu\r");}

        while ( $breakLoop eq "No" ){
                if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
                elsif($exp->expect($timeout, 'Select number of the area you wish to use')){
                        $exp->send("$app_media\r");
                        $breakLoop = "Yes";
                }
        }

        if($exp->expect($timeout, 'Select the kickstart you wish to use for')){$exp->send("$kick_menu\r");}

        $breakLoop = 'No';
        while ( $breakLoop eq "No" ){
                if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
                elsif($exp->expect($timeout, 'Select number of the O&M Linux media you wish to use')){
                        $exp->send("$om_location\r");
                        $breakLoop = "Yes";
                }
        }
         $breakLoop = 'No';
        while ( $breakLoop eq "No" ){
                if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
                elsif($exp->expect($timeout, 'Select the install patch kickstart you wish to use for')){
                        $exp->send("$patch_menu\r");
                        $breakLoop = "Yes";
                }
        }
    #if($exp->expect($timeout, 'Select the install patch kickstart you wish to use for')){$exp->send("$patch_menu\r");}
    if($exp->expect($timeout, 'Select the display type of')){$exp->send("1\r");}
    if($exp->expect($timeout, 'Enter the installation parameters for the client')){$exp->send("$install_params\r");}
    if($exp->expect($timeout, 'Are you sure you wish to add this kickstart client? (Yes|No)')){$exp->send("Yes\r");}

        if ($exp->expect($timeout, 'Added kickstart client')) {
                print "*" x 70;
                print "\n    ADDED THE CLIENT $server TO MWS $mws ..!!\n";
                print "*" x 70;
                print "\n\n";
        }
        else{
                print "*" x 70;
                print "\n    NOT ABLE TO ADD THE CLIENT $server TO $mws MWS..!!\n";
                print "\n    PLEASE REFER THE LOG FOR ERRORS..!!\n";
                print "*" x 70;
                print "\n\n";
        }

    $exp->expect(5, '#');
    $exp->soft_close();
}
if ($mws ne "10.45.192.153"){
                print "*" x 70;
                print "\n    NEED TO IMPLEMENT THIS FEATURE FOR $mws..!\n";
                print "\n    KINDLY PLEASE WAIT..!!\n";
                print "*" x 70;
                print "\n\n";
                exit 4;
        }
else{
        remove_dhcp_client();
        add_dhcp_client();
}
