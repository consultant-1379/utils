#!/app/perl/5.8.4/bin/perl -w
#-----------------------------------------------------------
# COPYRIGHT Ericsson Radio Systems  AB 2016
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
#   RESP         : xgirred
#   DATE         : 10/02/2018
#   Description  : This Script is to trigger RT Execution based on the packages delivered. 
#   REV          : A1 
#   
# --------------------------------------------------------------


use strict;
use warnings;
use Getopt::Long;
use Expect;


### Variables
my $help;
my $Shipment;
my $Release;
my $WORKSPACE;
my $Machine;
my $fdm_version;
my $undef= undef;
my $TMP_FILE = "/tmp/CheckExitCode.txt";
my $rt_version;
my $def = 3600;
my $exp;
my $timeout;
my $PROMPT = "#: ";
my $user_root = "root";
my $user_root_password = "shroot12";
my $user_dcuser = "dcuser";
my $user_dcuser_password = "dcuser";
my $Build_Number;
my $BIN_PATH = "/proj/eiffel004_config_fem160/eiffel_home/bin/";
my $KGB_DATA_PATH = "/proj/eiffel004_config_fem160/eiffel_home/KGB_DATA/";
my $CHECK_IN_FILES_PATH = $KGB_DATA_PATH.$Build_Number."/CHECK_IN_FILES/";
my $CURR_BUILD_KGB_DATA_PATH =$KGB_DATA_PATH."$Build_Number/";
my $HTML_REPORT = "/eniq/sw/installer/TP_BO_Installation_Status.html";

my $get_rt_version_file = "/tmp/get_rt_version_file.txt";




#################################################
sub usage{
        print "Unknown option: @_\n" if ( @_ );
        print "usage: program [-r RELEASE] [-s SHIPMENT] [-m Machine] [-w Workspace] [-help|-?]\n";
        exit;
}


#################################################
sub PARAMETERS
{
        usage() if ( @ARGV < 1 or ! GetOptions('help|?' => \$help, 'rel|r=s' => \$Release, 'ship|s=s' => \$Shipment,'machine|m=s' => \$Machine, 'workspace|w=s' => \$WORKSPACE) or defined $help );


                if($Release)
                {
                        if ($Release !~ /^ENIQ_S[0-9][0-9].[0-9]$/)
                        {
                                print "The Release entered is $Release Wrong, Please check it \n";
                                exit(4);
                        }
        print "##########################################################################################################################################\n";
        print  "Release is: $Release\n";
        }
        if($Shipment)
        {
		if ($Shipment !~ /^[0-9][0-9].[0-9].[0-9]$/)
		{
                                if ($Shipment !~ /^[0-9][0-9].[0-9].[0-9].EU[0-9]$/)
                                {
                                        print "The Shipment entered is $Shipment Wrong, Please check it \n";
                                        exit(5);
                                }
                        }
		print  "Shipment is : $Shipment\n";
		$fdm_version = substr($Shipment,0,4);
		$fdm_version = $fdm_version.".FDM";
		#$fdm_version = $fdm_version.".DMTEST";			
        	print  "FDM_VERSION is : $fdm_version\n";
        }
	print "Machine IP Address is : $Machine \n";
	if (!$WORKSPACE)
	{
		print "Please provide the WORKSPACE...... \n";
		exit(55);
	}


                print "##########################################################################################################################################\n";


} # Closed PARAMETER Function

##############################################################
### Function to download EPFG RT pacakge....

sub Get_RT_Latest_Version
{
	if ( -e $get_rt_version_file )
	{
		`rm -rf $get_rt_version_file`;
	}
	$timeout=15;
	$exp=Expect->spawn("/usr/bin/ssh $user_root\@eniqs ") or die "Can not SSH to $Machine  \n";
                if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                                             $exp->send('yes' . "\n");
                                         }
                                        $exp->expect($timeout,
                                        [ 'assword: $' => sub {
                                                                        $exp->send("$user_root_password\r");
                                                                        exp_continue; }
                                                ],
                                                '-re', qr'[^.*->#] $' => sub {
                                                                        exp_continue; }
                        );
    	$exp->expect($undef, $PROMPT);
		my $cmd_latest_rt_version = "/usr/sfw/bin/wget --user=statsjenki --password=2020\#Apr -O - http://clearcase-oss.lmera.ericsson.se/view/www_eniq/vobs/ossrc/del-mgt/html/eniqdel/$Release/$fdm_version/SOLARIS_baseline.html | grep 'RT_KGB_Delivery' | grep clearcase | grep '.tar' ";
        $exp->send("$cmd_latest_rt_version\r");
        $exp->log_file("$get_rt_version_file", "w");
        $exp->expect(10);
        $exp->log_file(undef);
		`cat $get_rt_version_file`;
	
		$rt_version = `cat $get_rt_version_file | grep 'RT_KGB_Delivery' | tail -1 | awk -F'">' '{print \$1}' | awk -F'/' '{print \$NF}'`;
		$rt_version =~ s/\s+//g;
		if(!$rt_version)
		{
			print "\n\n RT Version is Empty !!!!!. So Exiting....!!!! \n\n";
			exit(55);
		}
		print "\n\n\ RT VERSION is : $rt_version \n";
	#$exp->expect($def, ['$PROMPT', sub {$exp = shift; $exp->send("\r");}]);
	
}	 # Closed Get_Epfg_RT_Latest_Version () function.


##################################################################################
### Function to download latest and trigger RT
sub Get_RT_And_Execute
{
	$timeout = 15;
	print "======================================================\n";
	print "   Cleaning the RT logs and downloading the latest RT \n";
	print "======================================================\n";
	#$exp->expect($undef, $PROMPT);
	#$exp->send("\r");

	my $clean_command = "rm -rf /eniq/home/dcuser/RT_delivery_* /eniq/home/dcuser/RT_* /eniq/home/dcuser/nohup*";	
	
	my $rt_download = "/usr/sfw/bin/wget --user=statsjenki --password=2020\#Apr -N http://clearcase-oss.lmera.ericsson.se/view/www_eniq/vobs/ossrc/del-mgt/html/eniqdel/$Release/$fdm_version/$rt_version -P /eniq/home/dcuser";

			### Clean all the required Directories
			#$exp->expect($def, ['$PROMPT', sub {$exp = shift; $exp->send("\r");}]);
            		$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$clean_command \r");}]);
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);	
			
			## Download the RT from the version which we got.	
			$exp->clear_accum();
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$rt_download \r");}]);
			CheckExitCode();
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("cd /eniq/home/dcuser/\r");}]);
			$exp->clear_accum();
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("tar -xvf $rt_version\r");}]);
			CheckExitCode();
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
			my $chmod_command = "chmod 777 /eniq/home/dcuser/RT_batch_kgb.sh";
			## Change Permissions
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$chmod_command \r");}]);
			## Source the env file
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("source /eniq/sql_anywhere/bin64/sa_config.sh \r");}]);
			$exp->clear_accum();
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("bash /eniq/home/dcuser/RT_batch_kgb.sh\r");}]);
			CheckExitCode();
			$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("cat $HTML_REPORT \r");}]);
			$exp->expect(3);
            	$exp->soft_close();
		#$exp->clear_accum();
		#$exp->send("/usr/bin/unzip -o $epfg_file \r");
		#CheckExitCode();


} #Get_RT_And_Execute Closed


######################################################################
### Function to Check if the command executed is succesful or not
sub CheckExitCode
{
        $exp->expect(undef, ['#:', sub {$exp = shift; $exp->send("\r");}]);
        $exp->expect(undef, ['#:', sub {$exp = shift; $exp->send("\r");}]);
        $exp->expect(undef, ['#:', sub {$exp = shift; $exp->send("\r");}]);
		$exp->log_file(undef);
        $exp->log_file("$TMP_FILE", "w");
        $exp->expect(undef, ['#:', sub {$exp = shift; $exp->send("echo \$\?\r");}]);
        $exp->expect(undef, ['#:', sub {$exp = shift; $exp->send("\r");}]);
        $exp->log_file(undef);

        open(LOG_FILE,"<$TMP_FILE");
        my @log=<LOG_FILE>;
        close(LOG_FILE);

        my $result=join("",@log);
        chomp($result);
        $result =~ s%\s%%g;
        $result =~ s%.*echo\$\?(\d).*%$1%;

        if($result ne 0){
                print "\n\nERROR: Exit code for the last Script/Command call was $result.\n\tExiting now..";
                exit(-1);
        }else{
                print "\n\nINFO: Exit code for the last Script/Command call was $result.\n";
        }

        $exp->expect(undef, ['#', sub {$exp = shift; $exp->send("\r");}]);

}	#Closed CheckExitCode()

#############################################################################
### Function to get the output html file to Workspace Area.
sub Get_Results
{
	chdir($WORKSPACE) or die "Unable to Switch to $WORKSPACE directory \n";
	$timeout=20;
	$exp=Expect->spawn("/usr/bin/scp $user_root\@eniqs:/eniq/home/dcuser/RegressionLogs/*.html . ") or die "Can not SCP to $Machine  \n";
                if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                                             $exp->send('yes' . "\n");
                                         }
                                        $exp->expect($timeout,
                                        [ 'assword: $' => sub {
                                                                        $exp->send("$user_root_password\r");
                                                                        exp_continue; }
                                                ],
                                                '-re', qr'[^.*->#] $' => sub {
                                                                        exp_continue; }
                        );
    $exp->soft_close();
	
} # Get_Results closed

#### Main Function
{
	PARAMETERS();
	Get_RT_Latest_Version();
	Get_RT_And_Execute();
	Get_Results();
}

