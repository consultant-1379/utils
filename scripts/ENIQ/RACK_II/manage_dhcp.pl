#!/vobs/cello/cade_A_tools_perl/SunOS/sparc/bin/perl -w
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
#   DATE         : 20/12/2018
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
my $linux_MWS = "10.45.192.153";
my $timeout = 20;
my $exp;
my $TEMP_FILE = "/tmp/RACK_II_Log.txt";
my @newShip = split("_", $SPRINT);
my $Shipment = $newShip[0];
my $breakLoop = 'No';

sub remove_dhcp_client
{
    $exp=Expect->spawn("/usr/bin/ssh root\@$linux_MWS") or die "Can not SSH $linux_MWS $! \n";
    if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
    if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
    $exp->expect(30, '#');
    
    print "\nRemoving the ieatrcx6575 DHCP client..!!\n";
    $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a remove -c ieatrcx6575 -N\r");
    $exp->expect(30, '#');
}

sub add_dhcp_client
{
    print "\nGetting needed info..!!\n";
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
    $exp->send("echo PATCH_MENU : \$patch_menu\r");
    $exp->expect(5, '#');
    $exp->send("echo KICK_MENU : \$kick_menu\r");
    $exp->expect(5, '#');
    $exp->send("echo APP_MEDIA : \$app_media\r");
    
    $exp->expect(15);
    $exp->log_file(undef);
    
    my $om_location = `cat $TEMP_FILE | grep OM_LOCATION | tail -1 | sed 's/OM_LOCATION ://g'`;
    my $patch_menu = `cat $TEMP_FILE | grep PATCH_MENU | tail -1 | sed 's/PATCH_MENU ://g'`;
    my $kick_menu = `cat $TEMP_FILE | grep KICK_MENU | tail -1 | sed 's/KICK_MENU ://g'`;
    my $app_media = `cat $TEMP_FILE | grep APP_MEDIA | tail -1 | sed 's/APP_MEDIA ://g'`;
    
	print "***app_media=$app_media, kick_menu=$kick_menu, om_location=$om_location, patch_menu=$patch_menu***";
    print "\nCreating the ieatrcx6575 DHCP client..!!\n";
    $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a add\r");
    if($exp->expect($timeout, 'Enter the client hostname')) {$exp->send("ieatrcx6575\r");}
    if($exp->expect($timeout, 'Enter the IP address of ieatrcx6575')){$exp->send("\r");}
    if($exp->expect($timeout, 'Enter the IP Netmask of ')){$exp->send("255.255.248.0\r");}
    if($exp->expect($timeout, 'Please enter the MAC address for ieatrcx6575')){$exp->send("1C:98:EC:1B:72:CC\r");}
    if($exp->expect($timeout, 'Do you want IPV6 enabled - YES/NO?')){$exp->send("NO\r");}
    
    if($exp->expect($timeout, 'Enter the Timezone to be set for ieatrcx6575')) {$exp->send("Eire\r");}
    if($exp->expect($timeout, 'Select the application type you wish to install on ieatrcx6575')){$exp->send("1\r");}
	while ( $breakLoop eq "No" ){
		if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
		elsif($exp->expect($timeout, 'Select number of the area you wish to use')){
		$exp->send("$app_media\r");
		$breakLoop = "Yes";
		}
	}
    # if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
	# if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
	# if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
    # if($exp->expect($timeout, 'Select number of the area you wish to use')){$exp->send("$app_media\r");}
    if($exp->expect($timeout, 'Select the kickstart you wish to use for ieatrcx6575')){$exp->send("$kick_menu\r");}
    
	$breakLoop = 'No';
	while ( $breakLoop eq "No" ){
		if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
		elsif($exp->expect($timeout, 'Select number of the O&M Linux media you wish to use')){
		$exp->send("$om_location\r");
		$breakLoop = "Yes";
		}
	}
    # if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
	# if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
	# if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
    # if($exp->expect($timeout, 'Select number of the O&M Linux media you wish to use')) {$exp->send("$om_location\r");}
	
	$breakLoop = 'No';
	while ( $breakLoop eq "No" ){
		if($exp->expect($timeout, "Press space to continue, 'q' to quit.")){$exp->send(" ");}
		elsif($exp->expect($timeout, 'Select the install patch kickstart you wish to use for ieatrcx6575')){
		$exp->send("$patch_menu\r");
		$breakLoop = "Yes";
		}
	}
	
    #if($exp->expect($timeout, 'Select the install patch kickstart you wish to use for ieatrcx6575')){$exp->send("$patch_menu\r");}
    if($exp->expect($timeout, 'Select the display type of ieatrcx6575')){$exp->send("1\r");}
    if($exp->expect($timeout, 'Enter the installation parameters for the client')){$exp->send("inst_type=eniq config=stats deployment=ft\r");}
    if($exp->expect($timeout, 'Are you sure you wish to add this kickstart client? (Yes|No)')){$exp->send("Yes\r");}

    print "\nAdding CLIENT_INSTALL_PARAMS value to ieatrcx6575_ks_cfg.txt..!!\n";
    $exp->expect(10, '#');
    $exp->send("echo \"CLIENT_INSTALL_PARAMS=inst_type=eniq config=stats deployment=ft\" >> /JUMP/LIN_MEDIA/1/kickstart/ieatrcx6575/ieatrcx6575_ks_cfg.txt\r");
    $exp->expect(5, '#');
    $exp->soft_close();
}

remove_dhcp_client();
add_dhcp_client();