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
#   DATE         : 11/04/2018
#   Description  : This Script is to the installation html report to workspace. 
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
my $TP_BO_HTML_REPORT = "/eniq/sw/installer/TP_BO_Installation_Status.html";


#################################################
sub usage{
        print "Unknown option: @_\n" if ( @_ );
        print "usage: program [-w Workspace] [-help|-?]\n";
        exit;
}


#################################################
sub PARAMETERS
{
        
	usage() if ( @ARGV < 1 or ! GetOptions('help|?' => \$help, 'workspace|w=s' => \$WORKSPACE) or defined $help );


	if (!$WORKSPACE)
	{
		print "Please provide the WORKSPACE...... \n";
		exit(55);
	}


    print "##########################################################################################################################################\n";

} # Closed PARAMETER Function


#############################################################################
### Function to get the output html file to Workspace Area.
sub Get_HTML_to_WorkSpace
{
	chdir($WORKSPACE) or die "Unable to Switch to $WORKSPACE directory \n";
	$timeout=20;
	$exp=Expect->spawn("/usr/bin/scp $user_root\@eniqs:$TP_BO_HTML_REPORT . ") or die "Can not SCP to $Machine  \n";
                if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                                             $exp->send('yes' . "\n");
                                         }
                                        $exp->expect($timeout,
                                        [ 'Password: $' => sub {
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
	Get_HTML_to_WorkSpace();
}

