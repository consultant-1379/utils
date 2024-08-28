#!/usr/bin/perl
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
#   DATE         : 07/07/2016
#       Description      : This Script is to validate the CUID of the BO_reports pacakges w.r.to ENIQ-STATS KGB
#   REV          : A1 
# --------------------------------------------------------------
#   
#  
use strict;
use warnings;
no warnings 'uninitialized';
use File::Copy;

my $BO_KGB_DIR = "/eniq/sw/installer/BO_package/";
my $BO_report_dir = "/eniq/sw/installer/boreports/";
my $CUID_Script_tmp = "/tmp/CUID_extractor.sh";
my $CUID_LIST_18B_tmp = "/tmp/CUID_LIST_18B.txt";
my $COM_FILE_REPORT = "/tmp/cuid_comparision_report.txt";
my $BO_Name;
my $BO_Name_Full;
my $BO_dir_name;
my $fh;
my $BO_ORG_Name;
my $BO_UNV_Name;
my $BO_UNV_Nam;
my @BO_UNV_CUID_EXT;
my $BO_UNV_CUID_VALUE;
my $BO_UNV_CUID_VALUE_EXT;
my $BO_UNV_CUID_VALUE_EX;
my @BO_UNV_CUID_18B;
my $BO_UNV_CUID_VALUE_18B;
my $input;

if ( ! -d $BO_KGB_DIR )
        {
                print "$BO_KGB_DIR doesn't exists so Exiting......!!!!! Might be There are not BO_Pacakge to be extracted....\n";

        }
else
        {
		print "In CUID comparator\n\n";
                if ( -f $COM_FILE_REPORT)
                        {
                                system("cd /tmp;/usr/bin/rm -rf $COM_FILE_REPORT");
                        }
                        system("cd /tmp; touch $COM_FILE_REPORT ; chmod 777 $COM_FILE_REPORT;chown dcuser:dc5000 $COM_FILE_REPORT");
                        
                        chomp($BO_report_dir);
                        chdir($BO_report_dir) or die "Can not switch to BO reports directory $! \n";

                        chomp($CUID_Script_tmp);
                        chomp($CUID_LIST_18B_tmp);
                        copy($CUID_Script_tmp,$BO_report_dir);
                        if ( -f "CUID_LIST.csv")
                                {
                                        system("/usr/bin/rm -rf CUID_LIST.csv");
                                }

			print "Executing CUID extractor\n\n";
                        system("/usr/bin/bash CUID_extractor.sh");
                        if (! -f "CUID_LIST.csv")
                        {
                                print "The CUID_LIST.csv file doesn't EXISTS After running CUID_extractor.sh\n";
                        }

                        open( $input , "$BO_report_dir/CUID_LIST.csv" ) or die "Unable to open $BO_report_dir/CUID_LIST.csv file $! \n";
                        while(<$input>) 
                        {
			print " the values is $_";
                        $BO_Name_Full=(split /\,/, "$_")[0];
                        $BO_Name=(split /_R[0-9]/,"$BO_Name_Full")[0];
                        print "BO Name is $BO_Name \n";
                        $BO_UNV_Nam=(split /\,/, "$_")[2];
			$BO_UNV_Name = substr((split '\#%', "$BO_UNV_Nam")[0],0,-2);
			#$BO_UNV_Name = (split '\#%', "$BO_UNV_Nam")[0];
                        print "BO Universe name is $BO_UNV_Name \n";
                
                        $BO_UNV_CUID_VALUE_EX = (split /\,/, "$_")[2];
                        $BO_UNV_CUID_VALUE_EX =~ 's/\s//g';
			$BO_UNV_CUID_VALUE_EX = (split '\#%', $BO_UNV_Nam)[1];
			#$BO_UNV_CUID_VALUE_EXT = "TP".$BO_UNV_CUID_VALUE_EX;
			$BO_UNV_CUID_VALUE_EXT = substr($BO_UNV_CUID_VALUE_EX,1,-2);
                        print "The CUID value for $BO_Name is $BO_UNV_CUID_VALUE_EXT \n";

                        @BO_UNV_CUID_18B = `grep "$BO_UNV_Name" $CUID_LIST_18B_tmp`;
                        $BO_UNV_CUID_VALUE_18B = (split /\,/, "@BO_UNV_CUID_18B")[2];
                        $BO_UNV_CUID_VALUE_18B =~ 's\s//g';
                        print "The CUID value for $BO_Name from $CUID_LIST_18B_tmp file is $BO_UNV_CUID_VALUE_18B \n";
                
                        chomp($BO_UNV_CUID_VALUE_EXT);
                        chomp($BO_UNV_CUID_VALUE_18B);  
                        if ($BO_UNV_Name =~ /$BO_UNV_CUID_VALUE_18B/)
                        {
                                open(my $fh, '>>', $COM_FILE_REPORT) or die "Could not open file '$COM_FILE_REPORT' $!";
                                print $fh "CUID check for $BO_Name with Universe name $BO_UNV_Name is PASSED\n";
                                close $fh;              
                        }
                        else
                        {
                                open($fh, '>>', $COM_FILE_REPORT) or die "Could not open file '$COM_FILE_REPORT' $!";
                                print $fh "CUID check for $BO_Name with Universe name $BO_UNV_Name is FAILED\n";
                                close $fh;
                                
                                # Writing the Packge name to installation Failed file so that failure packages will not get delivered.....

                                if ( ! -e "/tmp/installation_failed.txt")
                                        {
                                		system("touch /tmp/installation_failed.txt");
                                		system("chmod 777 /tmp/installation_failed.txt");
                                		system("chown dcuser:dc5000 /tmp/installation_failed.txt");
                                        }
                                open($fh, '>>', '/tmp/installation_failed.txt');
                                print $fh "$BO_Name\n";
                                close $fh;
                        }       
                }
        }
print " #################### The CUID Check Report is ################ \n";
open (Report_file, $COM_FILE_REPORT);
 while (<Report_file>) {
    chomp;
    print "$_\n";
 }
print " #################### ################ ################\n";
