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
#   Description  : This Script is to Install CPAN before Executing RT. 
#   REV          : A1 
#   
# --------------------------------------------------------------
#   


use strict;
use warnings;
use Getopt::Long;
use Expect;


### Variables
my $help;
my $WORKSPACE;
my $Machine;
my $undef= undef;
my $TMP_FILE = "/tmp/CheckExitCode.txt";

my $def = 3600;
my $exp;
my $timeout;
my $PROMPT = "#: ";
my $user_root = "root";
my $user_root_password = "shroot12";
my $user_dcuser = "dcuser";
my $user_dcuser_password = "dcuser";

#################################################
sub usage{
        print "Unknown option: @_\n" if ( @_ );
        print "usage: program [-m Machine] [-w Workspace] [-help|-?]\n";
        exit;
}


#################################################
sub PARAMETERS
{
        usage() if ( @ARGV < 1 or ! GetOptions('help|?' => \$help, 'machine|m=s' => \$Machine, 'workspace|w=s' => \$WORKSPACE) or defined $help );
		print "==================================================================================\n";
		print "Machine is : $Machine \n";
		if (!$WORKSPACE)
		{
			print "Please provide the WORKSPACE...... \n";
			exit(55);
		}

        print "==========================================================================\n";
	print "\n";


} # Closed PARAMETER Function

##############################################################
### Function to SCP the required CPAN Files to Machine....

sub SCP_CPAN
{
	chdir($WORKSPACE) or die "Unable to Switch to $WORKSPACE directory \n";
	$timeout=15;
	$exp=Expect->spawn("/usr/bin/scp CPAN_Modules.zip cpanInstallerScript.pl $user_root\@eniqs:/eniq/home/dcuser/ ") or die "Can not SCP to $Machine  \n";
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
	
}	 # Closed SCP_CPAN function.


##################################################################################
### Function to Install the CPAN Module
sub CPAN_Install
{
	$timeout = 15;
        print "==============================================================================\n";
        print "   Installting the CPAN Module on the $Machine \n";
        print "==============================================================================\n";

	$exp=Expect->spawn("/usr/bin/ssh $user_root\@eniqs ") or die "Can not SSH and Clean $Machine $! \n";
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
	$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
	$exp->expect($undef, $PROMPT);
        $exp->send("\r");
	$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);

	my $chmod_command = "chmod 777 CPAN_Modules.zip cpanInstallerScript.pl ";
	## Change Permissions
	$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("cd /eniq/home/dcuser/ \r");}]);
	$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("$chmod_command \r");}]);
	### Install CPAN
	$exp->clear_accum();
    $exp->expect($def, ['#:', sub {$exp = shift; $exp->send("perl /eniq/home/dcuser/cpanInstallerScript.pl CPAN_Modules.zip \r");}]);
	CheckExitCode();
	$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("\r");}]);
	$exp->expect(3);
    $exp->soft_close();

} #CPAN_Install Closed

##################################################################################
### Function to check exit codes of the scripts executed on Machine
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


#### Main Function
{
	PARAMETERS();
	SCP_CPAN();
	CPAN_Install();
}

