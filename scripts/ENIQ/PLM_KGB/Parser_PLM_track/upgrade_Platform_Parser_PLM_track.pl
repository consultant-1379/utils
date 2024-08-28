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
#   DATE         : 1/10/2019
#   Description  : This Script is get the Platform packages and its related info according to SCM polling.
#   REV          : A1
# --------------------------------------------------------------

use strict;
use warnings;
no warnings 'uninitialized';
use POSIX qw(strftime);
use Expect;
my $run_time=strftime "%Y%m%d-%H_%M_%S", localtime;

my $def = 3600;
my $timeout = 30;
#### The below is the Build Number used in First job to create the required file in KGB area. 
###  Same build is used to check and transfer required files to Server and install them.
my $CHECKIN_JOB_BUILD_NUMBER = $ARGV[0]; 
my $BUILD_NO = $ARGV[1]; 

my $BIN_PATH = "/proj/eiffel004_config_fem156/eiffel_home/bin/";
my $KGB_DATA_PATH = "/proj/eiffel004_config_fem156/eiffel_home/FULL_PF_KGB_DATA/";
my $CHECK_IN_FILES = $KGB_DATA_PATH.$CHECKIN_JOB_BUILD_NUMBER."/CHECK_IN_FILES/";
my $KGB_DATA_CSV_PM_DIR = $KGB_DATA_PATH.$CHECKIN_JOB_BUILD_NUMBER."/CSV_PM/";
my $CURR_BUILD_KGB_DATA_PATH =$KGB_DATA_PATH."$CHECKIN_JOB_BUILD_NUMBER/";
my $exp;
my $CLEARCASE_VIEWTAG = "platformjenkins_view";
#my $confignfs = "/net/$Machine_IP";
my $vAppPW = 'shroot12';

my $hubAddress = "150.132.34.120";
my $hubPassword = "EStAts(iDec\$2()18";
my $logfile="/var/tmp/PF_KGB_CONSOLE_LOG.txt";
my $PLATFORM_DEST_PATH = "/tmp/PF_KGB/";

print "===================================================================\n";
print "Checkin Build Number : $CHECKIN_JOB_BUILD_NUMBER \n";
print "Build Number : $BUILD_NO \n";
print "Checked in files available in the jenkins directory : $CHECK_IN_FILES \n";
print "===================================================================\n";


########################################################################
##### Function to transfer the Tech_Packs to Vapp Server
sub Transfer_Packages
{
	print "\n======================================================\n";
	print "   Transferring Tech Packs to Vapp\n";
	print "======================================================\n";

	print "Creating the folder or cleaning the folder for packages transfer!\n";
	$exp=Expect->spawn("/usr/bin/ssh root\@eniqs -C '/usr/bin/mkdir -p /tmp/PF_KGB/;/usr/bin/rm -rf /tmp/PF_KGB/*'") or die "Can not SSH and Clean $PLATFORM_DEST_PATH $! \n";
	if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
	if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
	$exp->expect($timeout, '#:');
	$exp->soft_close();
	
    #Coping the install_PF_eniq.sh file to vApp
    print "Coping the install_PF_eniq.sh file to vApp!\n";
    $exp=Expect->spawn("/usr/bin/scp install_PF_eniq.sh getPkgs_list.py root\@eniqs:/tmp/PF_KGB/ ") or die "Can not scp to eniqs $! \n";
    if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
    $exp->expect($timeout, '#:');
    $exp->soft_close();

	## Creating the folder or cleaning the folder for packages transfer
	print "Loging into eniqs!\n";
	$exp=Expect->spawn("/usr/bin/ssh root\@eniqs") or die "Can not SSH\n";
	if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
	if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
	$exp->expect(30, '#:');
	$exp->send("cd $PLATFORM_DEST_PATH\r");
    $exp->expect(1);
	
	#Coping all checked-in packages to vApp
    print "Coping all checked-in packages to vApp!\n";
    $exp->send("/usr/bin/scp eniqdmt\@${hubAddress}:/proj/eiffel004_config_fem156/eiffel_home/FULL_PF_KGB_DATA/${CHECKIN_JOB_BUILD_NUMBER}/CHECK_IN_FILES/* /tmp/PF_KGB/\r");
    if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
    if($exp->expect($timeout, 'assword:')){$exp->send($hubPassword . "\n");}
    $exp->expect($def, '#:');
	
	print "\n======================================================\n";
	print "  Platform packages are : \n";
	$exp->send("ls | grep zip\r");
	$exp->expect(1);
	print "======================================================\n";
}

sub Install_Packages
{	
	print "\n======================================================\n";
	print "  Installing the Platform packagein Vapp\n";
	print "======================================================\n";
	
	my $chown_command="chown dcuser:dc5000 ${PLATFORM_DEST_PATH}*";
	## Change Permissions
	print "Changing the Permissions\n";
	$exp->send("\r");
	$exp->send("${chown_command}\r");
	$exp->expect($timeout, '#:');
	$exp->send("chmod 755 ${PLATFORM_DEST_PATH}*\r");
	$exp->expect($timeout, '#:');
	$exp->send("chown dcuser:dc5000 /eniq/sw/installer/*\r");
	$exp->expect($timeout, '#:');
	$exp->send("chown -R root:root /eniq/sw/installer/temp_invalid_views\r");
	$exp->expect($timeout, '#:');
	$exp->expect(1);
	$exp->send("\r");
	
	print "\nGenerating the latest_packages.txt for TAF\n";
	$exp->send("val=`cat /eniq/admin/version/eniq_status | grep Shipment | cut -d\" \" -f2 | cut -d\"_\" -f4`\r");
	$exp->expect($timeout, '#:');
	$exp->send("shipment=\$val\"_Linux\"\r");
	$exp->expect($timeout, '#:');
	$exp->send("/usr/bin/python ${PLATFORM_DEST_PATH}getPkgs_list.py \$shipment\r");
	$exp->expect(10);

	print "Running the install_PF_eniq.sh script!\n";
	$exp->log_file("$logfile", "w");
	$exp->send("su - dcuser \r");
	$exp->expect($timeout, '#:');
	$exp->send("/usr/bin/sh ${PLATFORM_DEST_PATH}install_PF_eniq.sh ${PLATFORM_DEST_PATH} > /var/tmp/log\r");
	$exp->expect($def, '#:');
	$exp->send("exit\r");
	$exp->expect($timeout, '#:');
	$exp->expect(10);
    $exp->log_file(undef);
    $exp->expect(30);
	$exp->soft_close();
	
	print "SCP'ing the log file to gateway..!!\n";
	$exp=Expect->spawn("/usr/bin/scp root\@eniqs:/var/tmp/log /tmp/") or die "Can not SSH and Clean $PLATFORM_DEST_PATH $! \n";
	if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {$exp->send('yes' . "\n");}
	if($exp->expect($timeout, 'assword:')){$exp->send('shroot12' . "\n");}
	$exp->expect($timeout, '#:');
	$exp->soft_close();
}

#### Main Function
{
	Transfer_Packages();
	Install_Packages();
}

