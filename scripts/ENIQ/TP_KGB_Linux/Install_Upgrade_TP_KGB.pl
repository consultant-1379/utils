#!/app/perl/5.16.2/RHEL6/bin/perl5.16.2
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
#   DATE         : 08/02/2018
#   Description  : This Script is to install/upgrade the pacakges that are checked-in from design as pert of ENIQS KGB
#   REV          : A1
#
# --------------------------------------------------------------
#


use strict;
use warnings;
use Getopt::Long;
use Expect;

if (@ARGV < 2) {
        print STDERR "Usage: \n\t/app/perl/5.16.2/RHEL6/bin/perl5.16.2 Install_Upgrade.pl <IP_ADDRESS> <CHECKIN_JOB_CHECKIN_JOB_BUILD_NUMBER> \n\n";
        exit 1;
}

### Variables
my $def = 3600;
my @BO_TP;
my @KPI_TP;
my $KPI_TP;
my $BO_TP;
my @TP_NOT_BO;
my $TP_NOT_BO;
my $exp;
my $timeout;
my $user_root = "root";
my $user_root_password = "shroot12";
my $user_dcuser = "dcuser";
my $user_dcuser_password = "dcuser";
my $Machine_IP = $ARGV[0];
#### The below is the Build Number used in First job to create the required file in KGB area.
###  Same build is used to check and transfer required files to Server and install them.
my $CHECKIN_JOB_BUILD_NUMBER = $ARGV[1];
my $WorkSpace = $ARGV[2];
my $BIN_PATH = "/proj/eiffel004_config_fem156/eiffel_home/bin/";
#my $BIN_PATH = "/home/lciadm100/jenkins/workspace/TP_KGB_Install_Package/scripts/ENIQ/TP_KGB_Linux/";
#my $KGB_DATA_PATH = "/proj/eiffel004_config_fem160/eiffel_home/KGB_DATA/";
my $KGB_DATA_PATH = "/proj/eiffel004_config_fem156/eiffel_home/Linux_KGB_DATA/";
my $CHECK_IN_FILES_PATH = $KGB_DATA_PATH.$CHECKIN_JOB_BUILD_NUMBER."/CHECK_IN_FILES/";
my $KGB_DATA_CSV_PM_DIR = $KGB_DATA_PATH.$CHECKIN_JOB_BUILD_NUMBER."/CSV_PM/";
my $CURR_BUILD_KGB_DATA_PATH =$KGB_DATA_PATH."$CHECKIN_JOB_BUILD_NUMBER/";
my $TP_VAPP_DEST_PATH = "/eniq/sw/installer/";
my $KPI_VAPP_DEST_PATH = "/eniq/sw/installer/reporttest";
my $BO_VAPP_DEST_PATH = "/eniq/sw/installer/BO_package/";
my $HTML_REPORT = "/eniq/sw/installer/TP_BO_Installation_Status.html";
my $NODE_DIR_FILE = $BIN_PATH.".NODE_DIR_FILE.txt";
my $CSV_FILE_DEST_DIR = "/eniq/home/dcuser/epfg/CounterComparison/";

### Arrays



#############################################################
## Function to transfer all the required files to VApp server, which can be used later for execution.

sub SCP_Required_Files
{
        my $exp;
        my $timeout = 10;
        my @Files = ("pkg_inst_check.pl","BO_Install.sh","KGB_html_check.sh","Compare_CUID.pl","CUID_extractor.sh","CUID_LIST_18B.txt","install.sh","Generate_Install_Report.pl","epfgdataGeneration.pl");
        my $Files;
        foreach(@Files)
        {
                $Files.="$BIN_PATH$_ ";
        }

        print "======================================================\n";
        print " Transferring the Required Files to Vapp Server \n";
        print "======================================================\n";
        $exp=Expect->spawn("/usr/bin/scp -P 2251 $Files $user_root\@$Machine_IP:/tmp ") or die "Can not scp to $Machine_IP $! \n";
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
            #$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("bash\r");}]);
            $exp->soft_close();
} # SCP_Required_Files CLOSED


#############################################################
## Function to transfer data file to VApp server, which can be used later for execution.

sub SCP_Data_File
{
        my $exp;
        my $timeout = 10;
        my @Files = ("data");
        my $Files;
        foreach(@Files)
        {
                $Files.="$BIN_PATH$_ ";
        }

        print "======================================================\n";
        print " Transferring the Data File to Vapp Server \n";
        print "======================================================\n";
        $exp=Expect->spawn("/usr/bin/scp /home/lciadm100/jenkins/workspace/TP_KGB_Install_Package/data.txt root\@192.168.0.51:/eniq/home/dcuser ") or die "Can not scp to $Machine_IP $! \n";
                        if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                                                                         $exp->send('yes' . "\n");
                                                                        }
                                                                $exp->expect($timeout,
                                                                        [ 'assword: $' => sub {
                                                                                                         $exp->send("shroot12\r");
                                                                                                          exp_continue; }
                                                                                ],

                                                                                '-re', qr'[^.*->#] $' => sub {
                                                                                                        exp_continue; }
                                                                );
            #$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("bash\r");}]);
            $exp->soft_close();
} # SCP_Required_Files CLOSED



#############################################################
## Function to clean all the respective areas to make the install as a new/fresh one.
### Cleans up the Regression LOGS area and BO location area too. Make directories and Change permissions for execution.
sub PRECONDITIONS
{
        $timeout = 15;
	my $clean_command = "rm -rf /eniq/sw/installer/*.tpi rm -rf /eniq/sw/installer/reporttest/* /eniq/sw/installer/bouniverses/* rm -rf /eniq/sw/installer/report/* /eniq/home/dcuser/RegressionLogs* /eniq/home/dcuser/RegressionLogs/*.html /tmp/installation_failed.txt /eniq/sw/installer/BO_package /eniq/sw/installer/BO_package/* /eniq/sw/installer/boreports/BO_* /eniq/sw/installer/Tech_pack_order.txt /eniq/home/dcuser/data.txt";
        print "=================================================================================\n";
        print "   Cleaning the Directories,Logs,Making dir and giving permissions \n";
        print "=================================================================================\n";


        my $mkdir_command = "mkdir /eniq/sw/installer/BO_package";

	my $chmod_command = "/usr/bin/chmod 777 /eniq/sw/installer/BO_package;/usr/bin/chmod 777 /eniq/sw/installer/reporttest;/usr/bin/chown dcuser:dc5000 /eniq/sw/installer/reporttest;/usr/bin/chown dcuser:dc5000 /eniq/sw/installer/BO_package;/usr/bin/chmod 777 /tmp/Compare_CUID.pl /tmp/CUID_LIST_18B.txt /tmp/CUID_extractor.sh;/usr/bin/chown dcuser:dc5000 /tmp/Compare_CUID.pl /tmp/CUID_LIST_18B.txt /tmp/CUID_extractor.sh";
        $exp=Expect->spawn("/usr/bin/ssh -p 2251 $user_root\@$Machine_IP ") or die "Can not SSH and Clean $Machine_IP $! \n";
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
                        ### Clean all the required Directories
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$clean_command \r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        ## Make Directories
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$mkdir_command \r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        ## Change Permissions
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$chmod_command \r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        $exp->expect(3);
            $exp->soft_close();
} # PRECONDITIONS CLOSED


#########################################################################
##### Function to transfer the Tech_Packs to Vapp Server
sub Transfer_Packages
{
        print "\n======================================================\n";
        print "   Transferring Tech Packs to Vapp $Machine_IP \n";
        print "======================================================\n";


        my $Tech_Pack_Order_File = "$CURR_BUILD_KGB_DATA_PATH"."Tech_pack_order.txt";
        $timeout = 5 ;
        my $exp=Expect->spawn("/usr/bin/scp -P 2251 $Tech_Pack_Order_File $user_root\@$Machine_IP:/eniq/sw/installer/ ") or die "Can not scp to $Machine_IP $! \n";
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
        @KPI_TP = `ls $CHECK_IN_FILES_PATH | grep 'Report'`;
        @KPI_TP = grep { $_ ne '' } @KPI_TP;
        $KPI_TP;
        foreach(@KPI_TP)
        {
                chomp($_);
                $KPI_TP.="$CHECK_IN_FILES_PATH$_ ";
        }

        print "\n======================================================\n";
        print "   KPI Packages are : \n $KPI_TP \n";
        print "======================================================\n";

        if(@KPI_TP)
        {
                my $no_of_KPI = `ls $CHECK_IN_FILES_PATH | grep 'Report' | wc -l`;
                $timeout = 15 * $no_of_KPI;
                #print "Timeout of BO is $timeout : \n\n\n\n\n";
                chomp($KPI_TP);
                $KPI_TP =~ s/\s+$//;
                print "\n\n SCP\'ing $KPI_TP to $Machine_IP:$KPI_VAPP_DEST_PATH \n\n";
                my $exp=Expect->spawn("/usr/bin/scp -P 2251 $KPI_TP $user_root\@$Machine_IP:$KPI_VAPP_DEST_PATH ") or die "Can not scp to $Machine_IP $! \n";
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
        }

        @TP_NOT_BO = `ls $CHECK_IN_FILES_PATH | egrep -v 'BO|Report'`;
        $TP_NOT_BO;
        foreach(@TP_NOT_BO)
        {
                chomp($_);
                $TP_NOT_BO.="$CHECK_IN_FILES_PATH$_ ";
        }

        print "======================================================\n";
        print "  Tech Packs are : \n  $TP_NOT_BO \n";
        print "======================================================\n";

        ### SCP the Files
        if(@TP_NOT_BO)
        {
                foreach my $tp (@TP_NOT_BO)
                {
                        chomp($tp);
                        $timeout = 5;
                        print "Scp'ing the $CHECK_IN_FILES_PATH$tp to $Machine_IP path $TP_VAPP_DEST_PATH \n";
                        my $exp5=Expect->spawn("/usr/bin/scp -P 2251 $CHECK_IN_FILES_PATH$tp $user_root\@$Machine_IP:$TP_VAPP_DEST_PATH ") or die "Can not scp to $Machine_IP $! \n";
                                if ($exp5->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                                                                         $exp5->send('yes' . "\n");
                                                                        }
                                                                $exp5->expect($timeout,
                                                                        [ 'assword: $' => sub {
                                                                                                         $exp5->send("$user_root_password\r");
                                                                                                          exp_continue; }
                                                                                ],

                                                                                '-re', qr'[^.*->] $' => sub {
                                                                                                        exp_continue; }
                                                                );
                        $exp5->expect(50, '-re', '100%');
                        $exp5->soft_close();

                }
        }

        @BO_TP = `ls $CHECK_IN_FILES_PATH | grep 'BO'`;
        @BO_TP = grep { $_ ne '' } @BO_TP;
        $BO_TP;
        foreach(@BO_TP)
        {
                chomp($_);
                $BO_TP.="$CHECK_IN_FILES_PATH$_ ";
        }

        print "\n======================================================\n";
        print "   BO Packages are : \n $BO_TP \n";
        print "======================================================\n";

        if(@BO_TP)
        {
                my $no_of_BO = `ls $CHECK_IN_FILES_PATH | grep 'BO' | wc -l`;
                $timeout = 15 * $no_of_BO;
                #print "Timeout of BO is $timeout : \n\n\n\n\n";
                chomp($BO_TP);
                $BO_TP =~ s/\s+$//;
                print "\n\n SCP\'ing $BO_TP to $Machine_IP:$BO_VAPP_DEST_PATH \n\n";
                my $exp=Expect->spawn("/usr/bin/scp -P 2251 $BO_TP $user_root\@$Machine_IP:$BO_VAPP_DEST_PATH ") or die "Can not scp to $Machine_IP $! \n";
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
        }
}

################################################################
### Function to trigger installtion of TP and BO tranferred to Vapp
sub Trigger_Installation
{
        $timeout = 30;

        my $chmod_command="/usr/bin/chmod 777 /eniq/sw/installer/reporttest/*.zip;/usr/bin/chown dcuser:dc5000 /eniq/sw/installer/reporttest/*.zip;chmod 777 /eniq/sw/installer/BO_package/*.tpi;/usr/bin/chmod 777 /eniq/sw/installer/*.tpi;/usr/bin/chown dcuser:dc5000 /eniq/sw/installer/*.tpi";
                        $exp=Expect->spawn("/usr/bin/ssh -p 2251 $user_root\@$Machine_IP ") or die "Can not SSH and Clean $Machine_IP $! \n";
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
                        ## Change Permissions
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$chmod_command\r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);

                        ### Trigger Tech Pack Installation that Got Transferred
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);

                        if(@KPI_TP)
                        {
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("/usr/bin/bash /tmp/KPI_Install.sh \r");}]);
                                #$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("perl /tmp/BO_Install_bkup.pl \r");}]);
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        }
                        if(@TP_NOT_BO)
                        {
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("su - dcuser \r");}]);
                                #$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("/usr/bin/sh /tmp/install.sh\r");}]);
				#$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("/usr/bin/perl /tmp/install_bkup.pl\r");}]);
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("exit\r");}]);
                        }

                        ## Trigger BO Extraction that Got Transferred
                        print "BO pacakges list is/are : @BO_TP \n";
                        if(@BO_TP)
                        {
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("/usr/bin/bash /tmp/BO_Install.sh \r");}]);
				#$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("perl /tmp/BO_Install_bkup.pl \r");}]);
                                $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        }


                        ### Trigger the Installtion check script
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("chmod 777  /tmp/pkg_inst_check.pl;/usr/bin/perl /tmp/pkg_inst_check.pl \r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        #### Trigger the Installation Status Report Generator script
                        $exp->expect($def, ['#:',sub{$exp = shift; $exp->send("chmod 755  /tmp/Generate_Install_Report.pl;/usr/bin/perl /tmp/Generate_Install_Report.pl\r");}]);
                        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
                        $exp->expect(3);
            $exp->soft_close();
} #Trigger_Installation CLOSED

##############################################################################
##### Function to get the installtion Failed TP list file to KGB Current Build area
sub Get_Installation_Failed_File
{

        chdir($CURR_BUILD_KGB_DATA_PATH) or die " unable to switch to directory $CURR_BUILD_KGB_DATA_PATH $!\n";
        $timeout = 5 ;
        $exp=Expect->spawn("/usr/bin/scp -P 2251 $user_root\@$Machine_IP:/tmp/installation_failed.txt . ") or die "Can not scp to $Machine_IP $! \n";
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
         #$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("bash\r");}]);
        $exp->soft_close();
}

#############################################################################
#### Funtion to get the HTML Rport of TP installation Status from the server
sub Get_Installation_Status_Report
{

        chdir($CURR_BUILD_KGB_DATA_PATH) or die " unable to switch to directory $CURR_BUILD_KGB_DATA_PATH $!\n";
        $timeout = 5 ;
        print " Getting the $HTML_REPORT to $CURR_BUILD_KGB_DATA_PATH area \n";
        $exp=Expect->spawn("/usr/bin/scp -P 2251 $user_root\@$Machine_IP:$HTML_REPORT . ") or die "Can not scp to $Machine_IP $! \n";
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
} # Get_Installation_Status_Report Closed

#### Main Function
{
        #SCP_Required_Files();
        #SCP_Data_File();
        PRECONDITIONS();
        Transfer_Packages();
        Trigger_Installation();
        Get_Installation_Failed_File();
        Get_Installation_Status_Report();
}

