#!/home/lciadm100/perl5/perlbrew/perls/perl-5.28.0/bin/perl
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
#   DATE         : 13/11/2017
#   Description  : This Script is to run EPFG script to generate file w.r.to GRIT CI.
#   REV          : A1
# --------------------------------------------------------------
#
#


use strict;
use warnings;
use lib '/home/lciadm100/perl5/perlbrew/perls/perl-5.28.0/lib/site_perl/5.28.0/';
use Expect;
use Getopt::Long;

my $help;
my $Release;
my $Shipment;
my $fdm_version;
my $epfg_version;
my $exp;
my $exp1;
my $timeout=30;
my $undef= undef;
my $def = 3600;
my $Machine;
my $TMP_FILE = "/tmp/CheckExitCode.txt";
my $PROMPT = "#: ";
my $DCUSER = "dcuser";
my $DCPASSWD = "Dcuser%12";
my $USER = "root";
my $PASSWD = "shroot12";
my $WORKSPACE;
my $rt_version;


my $get_epfg_rt_version_file = "/tmp/get_epfg_rt_version_file.txt";
my $get_epfg_ft_version_file = "/tmp/get_epfg_ft_version_file.txt";
my $get_inner_RT_Version_File = "/tmp/get_inner_RT_Version_File.txt";
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

sub Get_Epfg_RT_Latest_Version
{
        print "getting into server";
	if ( -e $get_epfg_rt_version_file )
	{
		`rm -rf $get_epfg_rt_version_file`;
	}
	$exp=Expect->spawn("/usr/bin/ssh dcuser\@eniqs ") or die "Can not SSH to $Machine  \n";
                if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                                             $exp->send('yes' . "\n");
                                         }
                                        $exp->expect($timeout,
                                        [ 'assword: $' => sub {
                                                                        $exp->send("Dcuser%12\r");
                                                                        exp_continue; }
                                                ],
                                                '-re', qr'[^.*->#] $' => sub {
                                                                        exp_continue; }
                        );
    	$exp->expect($undef, $PROMPT);
	my $cmd_latest_epfg_rt_version = "/usr/bin/wget --user=statsjenki --password=2020\#Jul -O - http://150.132.181.253/view/www_eniq/vobs/ossrc/del-mgt/html/eniqdel/$Release/$fdm_version/SOLARIS_baseline.html | grep epfg_rt | grep '.zip' ";
        #$exp->send("$cmd_latest_epfg_rt_version\r");
		$exp->send("ls /eniq/home/dcuser/ | grep epfg_ft\r");
        $exp->log_file("$get_epfg_rt_version_file", "w");
        $exp->expect(20);
        $exp->log_file(undef);
        `cat $get_epfg_rt_version_file`;
	#cat get_epfg_rt_version_file.txt  | grep 'epfg_rt'  | tail -1 | awk -F"\">" '{print $2}' | cut -d'"' -f2	
	$epfg_version = `cat $get_epfg_rt_version_file | grep 'epfg_ft' | tail -1 |awk -F'_' '{print \$3}'`; #| awk -F"=" '{print \$2}'| cut -d '"' -f2 | awk -F'/' '{print \$NF}'`;
	#$epfg_version = `cat $get_epfg_rt_version_file | grep 'epfg_ft' | tail -1 | awk -F'">' '{print \$1}' | awk -F'/' '{print \$NF}'`;
	#$epfg_version =~ s/\e\[\d+m//g;
	$epfg_version =~ s/\d;\d\dm//g;
	$epfg_version = "epfg_ft_".$epfg_version;
	print " $epfg_version";
	if(!$epfg_version)
	{
		print "\n\n EPFG RT Version is Empty !!!!!. So Exiting....!!!! \n\n";
		exit(55);
	}
	print "\n\n\nEPFG RT VERSION is : $epfg_version \n";
 #print "$cmd_latest_epfg_rt_version !!"	
}	 # Closed Get_Epfg_RT_Latest_Version () function.

##############################
sub Pre_Run_EPFG_RT
{
	
	my $epfg_download = "/usr/bin/wget --user=statsjenki --password=2020\#Jul -N http://150.132.181.253/view/www_eniq/vobs/ossrc/del-mgt/html/eniqdel/$Release/$fdm_version/$epfg_version -P /eniq/home/dcuser";
	#$exp->expect($undef, $PROMPT);
	#$exp->send("rm -rf /eniq/home/dcuser/epf* /eniq/home/dcuser/nohup* ;$epfg_download\r");
	#$exp->send("rm -rf /eniq/home/dcuser/nohup* ;$epfg_download\r");
	#$exp->expect($undef, $PROMPT);
	print " >>>>>>>>>>>>>>> Downloading Completed <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";
		
        print("unzipping the pkg");
		$exp->send("cd /eniq/home/dcuser/;unzip -o $epfg_version \r");
        #$exp->expect($undef, $PROMPT);
        $exp->log_file("$get_inner_RT_Version_File", "w");
        $exp->expect(5);
        $exp->log_file(undef);
        `cat $get_inner_RT_Version_File`;
        my $inner_RT_Version_Name = `cat $get_inner_RT_Version_File | grep inflating | cut -d ':' -f2`;
        $inner_RT_Version_Name =~ s/\s+//g;
        print "\n\nInner RT Version name is : $inner_RT_Version_Name \n\n";
                $exp->clear_accum();
                $exp->send("/usr/bin/unzip -o $inner_RT_Version_Name \r");
		#$exp->expect(40);
                #CheckExitCode();
                #$exp->expect(20);
                $exp->expect($undef, $PROMPT);
		$exp->send("/usr/bin/chmod -R 777 epfg\r");
		$exp->clear_accum();
		$exp->expect($undef, $PROMPT);
		print "\n\n\n\n ############################ Running Pre Config for EPFG to change the properties file.... ############## \n\n\n\n";
		$exp->send("cd /eniq/home/dcuser/epfg/;./epfg_preconfig_for_ft.sh\r");
		#CheckExitCode();
		#$exp->expect(15);
		#$exp->clear_accum();
		$exp->expect($undef, $PROMPT);
		print "\n\n\n\n ############################ Running Nodes.sh Script to enable Flags .... ############## \n\n\n\n";
		#$exp->send("cd /eniq/home/dcuser/epfg/;./nodes.sh\r");
		$exp->send("cd /eniq/home/dcuser/epfg/;\r");
		#CheckExitCode();
		$exp->expect(5);
		
		### Execution of EPFG is also added here 
		#$exp->clear_accum();
		$exp->expect($undef, $PROMPT);
		$exp->send("ls /eniq/home/dcuser/ | grep RT_KGB_Delivery\r");
		$exp->log_file("$get_rt_version_file", "w");
		$exp->expect(10);
		$exp->log_file(undef);
		`cat $get_rt_version_file`;
		$rt_version = `cat $get_rt_version_file | grep 'RT_KGB_Delivery' | tail -1 |awk -F'_' '{print \$4}'`; #| awk -F"=" '{print \$2}'| cut -d '"' -f2 | awk -F'/' '{print \$NF}'`;
		$rt_version =~ s/\d;\d\dm//g;
		$rt_version = "RT_KGB_Delivery_".$rt_version;
		if(!$rt_version)
		{
			print "\n\n RT Version is Empty !!!!!. So Exiting....!!!! \n\n";
			exit(55);
		}
		print "\n\n\ RT VERSION is : $rt_version \n";
		$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
		$exp->clear_accum();
		$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("cd /eniq/home/dcuser/\r");}]);
		$exp->clear_accum();
		#$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$rt_download \r");}]);
		CheckExitCode();
		#$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("cd /eniq/home/dcuser/\r");}]);
		$exp->clear_accum();
		$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("tar -xvf $rt_version\r");}]);
		$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
		$exp->expect($undef, $PROMPT);
		#$exp->send("\r");
                #print "\n\n\n +++++++++++++++++++++++++++++++++++++++++++++++ STARTING EPFGDATAGENERATION SCRIPT ++++++++++++++++++++++++++++++++++++++ \n\n\n";
		#$exp->send("cp /tmp/epfgdataGeneration.pl /tmp/epfgdataGenerations.pl;chmod 755 /tmp/epfgdataGenerations.pl;perl /tmp/epfgdataGenerations.pl \r");
                $exp->send("cd /eniq/home/dcuser/;/usr/bin/chmod 755 epfgdataGeneration.pl;perl epfgdataGeneration.pl\r");
		$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
		sleep 602;
		$exp->expect($undef, $PROMPT);
		print "\n\n\n +++++++++++++++++++++++++++++++++++++++++++++++ STARTING EPFG ++++++++++++++++++++++++++++++++++++++ \n\n\n";
		$exp->send("cd /eniq/home/dcuser/epfg; chmod +x start_epfg.sh; /eniq/home/dcuser/epfg/start_epfg.sh \r");
		#CheckExitCode();
		$exp->expect(5);
		$exp->expect($undef, $PROMPT);
		$exp->soft_close();
}	#Closed Pre_Run_EPFG_RT()

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

############################ MAIN FUNCTION #########################
{
	PARAMETERS();
	Get_Epfg_RT_Latest_Version();	### This is for downloading EPFG Rt pacakges.....
	Pre_Run_EPFG_RT();  			### This is call the code lgic w.r.to epft_rt pkg
}

