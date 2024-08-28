#!/home/lciadm100/perl5/perlbrew/perls/perl-5.28.0/bin/perl


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
my $def = 3600;
my $timeout=30;
my $undef= undef;
my $Machine;
my $TMP_FILE = "/tmp/CheckExitCode.txt";
my $PROMPT = "#: ";
my $DCUSER = "dcuser";
my $DCPASSWD = "dcuser";
my $USER = "root";
my $PASSWD = "shroot12";
my $WORKSPACE;

my $get_epfg_rt_version_file = "/tmp/get_epfg_rt_version_file.txt";
my $get_epfg_ft_version_file = "/tmp/get_epfg_ft_version_file.txt";
my $get_inner_RT_Version_File = "/tmp/get_inner_RT_Version_File.txt";


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

sub cleaning_directories
{

        print("login to the server \n");
        $exp=Expect->spawn("/usr/bin/ssh root\@eniqs ") or die "Can not SSH to $Machine  \n";
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
        $exp->expect($undef, $PROMPT);
        print("login to the server successfull..! \n");
        $exp->send("\r");
        print("Starting to  Clean the directories \n");
        my $clean_command = "rm -rf /eniq/home/dcuser/RT_delivery_* /eniq/home/dcuser/RT_* /eniq/home/dcuser/nohup* /eniq/home/dcuser/epfg_* /eniq/home/dcuser/KGB_RT_Reports.zip /eniq/home/dcuser/ResultFiles/* /eniq/home/dcuser/epfg*";
        $exp->send("\r");
        $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$clean_command \r");}]);
        print("cleaned all the directories \n");
        #$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
        $exp->send("\r");
        print(" Completing the process..!  \n");
        $exp->expect(5);
        $exp->send("\r");
        print(" Closing the connection. \n");
        $exp->soft_close();
        print(" Connection closed..! \n");
}       #Closed cleaning_directories


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
	cleaning_directories();			###This is for cleaning the folders before downloading the EPFG Rt packages.
}
