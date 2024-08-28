#!/usr/bin/perl -w
#
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
#   DATE         : 12/02/2018
#   Description  : This Script is get the Tech packs and its related info according to SCM polling.
#   REV          : A1
# --------------------------------------------------------------
#
#
use strict;
use warnings;
no warnings 'uninitialized';

my $JENKINS_HOME = $ARGV[0];
my $JOB_URL = $ARGV[1];
my $BUILD_NUMBER = $ARGV[2];
my $WORKSPACE = $ARGV[3];

my $comment;
my $fd_TP_Name;
my $fd_check;
my $fd_check_val;

my $jenkin_job_dir = ${JENKINS_HOME}."/jobs/";
my $KGB_DATA_DIR = ${JENKINS_HOME}."/Linux_KGB_DATA/";
my $KGB_PACK_DIR = ${JENKINS_HOME}."/Linux_KGB_DATA/Pack/";
my $KGB_PROP_DIR = ${JENKINS_HOME}."/Linux_KGB_DATA/Prop/";
my $KGB_DATA_CURRENT_DIR = $KGB_DATA_DIR."$BUILD_NUMBER";
my $KGB_DATA_CSV_PM_DIR = $KGB_DATA_DIR."$BUILD_NUMBER"."/CSV_PM/";
my $CHECK_IN_FILES = $KGB_DATA_DIR."$BUILD_NUMBER"."/CHECK_IN_FILES/";
my $CHECK_IN_ALL = $KGB_DATA_DIR."$BUILD_NUMBER"."/CHECKIN_FILES_ALL/";
my $Delivering_Dir = $KGB_DATA_DIR."$BUILD_NUMBER"."/Delivering_techpacks/";
my $output_file = $KGB_DATA_DIR."$BUILD_NUMBER"."/xid_comment_tech.txt";
my $KGB_DATA_FILE = $KGB_DATA_CURRENT_DIR."/Tech_pack_order.txt";

my $jobname= (split /\//,$JOB_URL)[-1];
my $job_build_dir = $jenkin_job_dir."$jobname"."/builds/"."$BUILD_NUMBER/";
my $WRKSPC_BUILD_DIR = $WORKSPACE."/workspace/".$jobname."/".$BUILD_NUMBER."/";
my $HTML_Report = $WRKSPC_BUILD_DIR."HTML_REPORT.html";

my $CLEARCASE_VIEWTAG = "tp_kgb_linux_jenkin_view";


my @fd_check_fail_tpi;
my @tech_pack_checked_in;
my @fd_pass_fail;
my @tp_comment_failed;

my $Polling_log_file= $job_build_dir."polling.log";
my $change_log_xml= $job_build_dir."changelog.xml";

#if ( ! -e $Polling_log_file)
#{
#        print " The Polling log for the Build $job_build_dir doesn't Exists. So Exiting..... \n";
#        exit(6);
#}

print "===================================================================\n";
print "JOB URL is $JOB_URL \n";
print "Build Number is $BUILD_NUMBER \n";
print "Job Name is $jobname \n";
print "Job Build Dir is $job_build_dir \n";
print "Work Space is $WORKSPACE \n";
print "Work Space Current Build directory is $WRKSPC_BUILD_DIR \n";
print "===================================================================\n";

#my @all_tpi=`grep /vobs/eniq $Polling_log_file | sort | uniq | sed s'/"//g'| awk '{print \$2 \$3}'| awk '!seen[\$0]++' | egrep '(Report|tpi)' | awk -F '/' '{print \$1","\$NF}' `;

#my @tpi_full_paths = `grep /vobs/eniq $Polling_log_file | sort | uniq | sed s'/"//g' | awk '{print  \$3}' | awk '!seen[\$0]++' | egrep '(Report|tpi)' | cut -d'/' -f4- | awk '{print "/"\$0}'`;

#my @NODE_NAMES_FOR_CSV_PM_FILES = `grep /vobs/eniq $Polling_log_file | grep 'xml\\|csv' | awk '{FS="\" \"";print \$3}' | sed 's/"//g' | awk -F "/" '{print \$8}' | sort | uniq | grep -v Feature`;

#`grep /vobs/eniq $Polling_log_file | grep 'xml\\|csv' | awk -F " " '{print \$3}' | uniq | grep -v /vobs/eniq/delivery/tp/Feature`;

#print "\n\n CSV and PM Files Nodes are below : \n @NODE_NAMES_FOR_CSV_PM_FILES \n";
my @all_tpi=`ls $KGB_PACK_DIR | egrep '(Report|tpi)'`;

sub uniq {
    my %seen;
    grep !$seen{$_}++, @_;
}

@all_tpi=uniq(@all_tpi);


############################################################
###### Below code gives the info about TPI, XID and Comments and writes to a file
sub GET_ALL_TP_INFO
{
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n";
        chdir("$job_build_dir") or die "Unable to Switch to Build dir $job_build_dir $!\n";

        if (@all_tpi)
        {
                print "*******************************************************************\n";
                print "We have these Tech Packs Checked In \n @all_tpi \n\n\n";
                print "********************************************************************\n";
                foreach (@all_tpi)
                {
                        chomp($_);
                        #print "The TPI value is : $_ \n\n\n";
                        #my $xid = (split /,/ , $_)[0];
			my $tp_name = $_;
						my $xid =`cat ${KGB_PROP_DIR}/${tp_name}_properties | grep Created`;
						$xid = (split /:/ , $xid)[1];
                        $xid =~ s/\s+//g;
			print "Xid is $xid";
                        #my $tp_name = (split /,/ , $_)[1];
						my $tp_name = $_;
                        $tp_name =~ s/\s+//g;
                        my $only_tp_name = (split /_R[0-9]/, $tp_name)[0];
                        $only_tp_name =~ s/\s+//g;
                        #print "The Only TP name is : $only_tp_name \n\n\n";
                        if ("$tp_name" !~ /^EVENT/ )
                        {
                                #my ($tp_full_path) = grep { /$tp_name/ } @tpi_full_paths;
                                #print "The full Path for the tp $tp_name is : $tp_full_path \n";
                                #chomp($tp_full_path);
                                #$tp_full_path =~ s/ //g;
                                #$comment = `cat $change_log_xml | egrep -B 4 "\/\${tp_name}" | grep  "<comment>" | grep "</comment>" |uniq|awk -F "<comment>" '{print \$2}' | cut -d "<" -f1`;
                                #my $cleartool_cmd = "/usr/atria/bin/cleartool desc ".$tp_full_path;
                                #$comment =`/usr/atria/bin/cleartool setview -exec '/proj/jkadm100/bin/lxb sol10u10x86 "setenv OS x86;$cleartool_cmd"' ${CLEARCASE_VIEWTAG} | sed -n '10p' | sed 's/\"//g'`;
                                #$comment =`/usr/atria/bin/cleartool setview -exec "$cleartool_cmd" ${CLEARCASE_VIEWTAG} | grep ENIQSTATS`;
                                #my $res=`echo $?`;
                                #print "\n\n\n\n\n\n\n Result Value is $res \n\n\n\n\n\n";
                                #$comment = "ENIQSTATS-WP00000";
                                #chomp($comment);
                                $comment = `cat ${KGB_PROP_DIR}/${tp_name}_properties | grep Reason`;
				$comment = (split /:/ , $comment)[1];
                                $comment =~ s/ //g;
                                print "----------------------------------------------------------\n";
                                print "The comment for this $tp_name is $comment \n";
                                print "-----------------------------------------------------------\n";
                                if( "$comment" =~ /^E/ )
                                {

                                        $fd_TP_Name = (split /_R[0-9]/,$tp_name)[0];
                                        $fd_TP_Name =~ s/\s+//g;
					print "fd_TP_Name is $fd_TP_Name";

                                        if ( "$fd_TP_Name" !~ /^BO/ )
                                        {
                                                if($fd_TP_Name =~ /^INTF_/)
                                                {
                                                        $fd_TP_Name = (split /INTF_/,$fd_TP_Name)[1];
                                                }
                                                print "The FD Tech Pack Name is $fd_TP_Name \n";

                                                $fd_check = `ls $KGB_PACK_DIR | grep $fd_TP_Name | grep xls`;

                                                chomp($fd_check);
                                                $fd_check =~ s/ //g;
                                                print "FD_TP_CHECK value is $fd_check \n";
                                                if ( "$fd_check" =~ "$fd_TP_Name" && "$fd_check" )
                                                {
                                                        $fd_check_val = "PASSED";
                                                }

                                                else
                                                {
                                                        $fd_check_val = "FAIL";
                                                        push (@fd_check_fail_tpi,$fd_TP_Name);
                                                }
                                        }
                                        else
                                        {
                                                $fd_check_val = "NOT Applicable";
                                        }
                                        chomp($xid);
                                        chomp($tp_name);
                                        chomp($comment);
                                        chomp($fd_check_val);
                                        print "\n=====================================================================";
                                        print "\nThe XID is $xid, Tech Pack Name is $tp_name, Comment is $comment,FD Check Status is $fd_check_val\n";
                                        print "\n=====================================================================\n";
                                        open (Outputfile , ">> $output_file");
                                        print Outputfile "$xid===$tp_name===$comment===$fd_check_val\n";
                                                #print "\n\n\n\n\n\n\n\n $xid===$tp_name===$comm===$fd_check_val\n\n\n\n\n\n";
                                        close Outputfile;
                                        push(@tech_pack_checked_in,$tp_name);
                                        push(@fd_pass_fail,$fd_check_val);              # This array is to fail the job if all the FD values are failed....

                                }               #if( "$comment" =~ /^ENIQSTATS/ ) CLOSED
                                else
                                {

                                        push(@tp_comment_failed,$only_tp_name); # Push if it is not a valid comment which doesnt start with ENIQSTATS
                                }

                        }               #if ("$tp_name" !~ /^EVENT/ ) CLOSED
                }               ###foreach (@all_tpi) CLOSED
        }
        else
        {
                print "Oops!! No DIM/DC/INTF/BO tech packs are checked in during this SCM Poll.\n";
                exit(5);
        }
        print "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";
        print "The Packages which Failed with Comments are: \n @tp_comment_failed \n";
}       # GET_ALL_TP_INFO CLOSED


##### GET HTML Head
sub getHtmlHead{
return qq{
            <html><head><title>Tech Pack Details Table</title></head>
            <body><table border="2"><tr><th><b> XID </th><th><b>Tech Pack Name</th><th><b>Comments</th><th><b>Model-T Check</th></tr>
         };
}

###########################################################
### Function to copy the TP to respective areas.
sub Copy_TP
{
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";
        print "\nIn the Copy_TP Function";

        foreach (@all_tpi)
        {
                        chomp($_);
                        my $tp_full_path= $_;
                        #my $tp_val = (split /\//,$_)[-1];
                        my $tp_value = (split /_R[0-9]/,$tp_full_path)[0];
                        #chomp($tp_val);
                        chomp($tp_value);
                        $tp_value =~ s/ //g;
			if ( $tp_value !~ /^EVENT/ )
			{
                                print " The tp_value is $tp_value \n";
                                print " The Tech Pack Full path is $tp_full_path \n\n\n";
				#if (!grep( /^$tp_value$/,@fd_check_fail_tpi ))
				#{
                                        print "Coping the Tech Pack $tp_value to $CHECK_IN_ALL path \n\n";
                                        `cp -rf ${KGB_PACK_DIR}/${tp_full_path} $CHECK_IN_ALL`;
                                        `cp -rf ${KGB_PACK_DIR}/${tp_full_path} $Delivering_Dir`;
                                        #`echo "$tp_value" | tee -a $KGB_DATA_FILE`;
					#}
					#else
					#{
					#print "The Tech Pack $tp_val has FAILED the FD Check so not copying into the $CHECK_IN_ALL directory \n";
					#}
                        }
                        else
                        {
                                print " $tp_value is not a STATS pkg\n";
                        }
        } # for closed
                        print "\nCalling Move Tech Pack script to copy packages to CHECK_IN_FILES directory \n";
                        #system("perl /proj/eiffel004_config_fem160/eiffel_home/bin/Move_Tech_Pack.pl $CHECK_IN_ALL $CHECK_IN_FILES");
		`cp -rf ${CHECK_IN_ALL}/* $CHECK_IN_FILES`;

                `chmod 777 $CHECK_IN_ALL/*;chmod 777 $Delivering_Dir/*;chmod 777 $CHECK_IN_FILES/*`;

                print "The Tech_pack_checked_in array is @tech_pack_checked_in \n";
                if(@fd_check_fail_tpi)
                {
                        print "The FD Check Failed Packages are @fd_check_fail_tpi \n";
                }
        print "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";
}       #Copy_TP CLOSED

############################################################
# GET HTML TAIL
sub getHtmlTail{
return qq{
                        </table></body></html>
        };
}

###########################################################
# This is to generate the HTML page
sub HTML_REPORT
{
        chdir($KGB_DATA_DIR)or die "Unable to Switch to dir $KGB_DATA_DIR $! \n";
        `touch  $HTML_Report;chmod 755 $HTML_Report`;
        print "Creating the HTML_REPORT....\n";

        my $report = getHtmlHead();

        if ( -e $output_file && !-z $output_file )
        {
                open(my $INPUT, $output_file) or die "There is no output file $! \n";
                while (<$INPUT>)
                {

                        chomp($_);
                        my @temp_array = split /\===/,$_;
                        my $xid = $temp_array[0];
                        my $tp_name = $temp_array[1];
                        my $comment = $temp_array[2];
                        my $FD_Check = $temp_array[3];
                        if ($FD_Check =~ "PASSED" )
                        {
                        $report.="<tr><td>$xid</td><td>$tp_name</td><td>$comment</td><td align=\"center\"><font color=\"green\"><b>PASS</font></td></tr>";
                        }
                        elsif($FD_Check =~ "FAIL")
                        {
                        if(!index($tp_name, "Report"))
                        {
                        $report.="<tr><td>$xid</td><td>$tp_name</td><td>$comment</td><td align=\"center\"><font color=\"red\"><b>NOT APPLICABLE</font></td></tr>";
                        }
                        elsif(!index($tp_name, "BO_"))
                        {
                        $report.="<tr><td>$xid</td><td>$tp_name</td><td>$comment</td><td align=\"center\"><font color=\"red\"><b>NOT APPLICABLE</font></td></tr>";
                        }
                        elsif(!index($tp_name, "INTF_"))
                        {
                        $report.="<tr><td>$xid</td><td>$tp_name</td><td>$comment</td><td align=\"center\"><font color=\"red\"><b>NOT APPLICABLE</font></td></tr>";
                        }
                        elsif($FD_Check =~ "FAIL")
                        {
                        $report.="<tr><td>$xid</td><td>$tp_name</td><td>$comment</td><td align=\"center\"><font color=\"red\"><b>FAILED</font></td></tr>";
                        }
                        #else
                        #{
                        #$report.="<tr><td>$xid</td><td>$tp_name</td><td>$comment</td><td align=\"center\"><font color=\"maroon\"><b> NOT APPLICABLE </font></td></tr>";
                        }
                }
        }
        $report.=getHtmlTail();
        print "The html page is $report \n";
        #my $report_page = "$WRKSPC_BUILD_DIR"."/".$HTML_Page;
        my $report_page = $HTML_Report  ;
        print " The Report Page value is $report_page \n";
        open( OUT , " > $report_page ");
        print OUT "$report" ;
        close OUT;
}


#################################################
# Creating all the Required Files for execution...
sub CREATE_FILES_AND_DIR
{
        print "CREATE_FILES_AND_DIR is being called.... \n";
        chdir($KGB_DATA_DIR)or die "Unable to Switch to dir $KGB_DATA_DIR $! \n";
        # Creating the Worspace Build number dir for reports and pkgs....
        `mkdir -p $WRKSPC_BUILD_DIR;chmod 777 $WRKSPC_BUILD_DIR`;
        `mkdir -p $KGB_DATA_CURRENT_DIR;chmod 777 $KGB_DATA_CURRENT_DIR`;
        #`mkdir -p $KGB_DATA_CSV_PM_DIR;chmod 777 $KGB_DATA_CSV_PM_DIR`;
        `mkdir -p $CHECK_IN_FILES;chmod 777 $CHECK_IN_FILES`;
        `mkdir -p $CHECK_IN_ALL;chmod 777 $CHECK_IN_ALL `;
        `mkdir -p $Delivering_Dir;chmod 777 $Delivering_Dir` ;
        `touch  $output_file;touch $KGB_DATA_FILE`;
        `chmod 755 $output_file $KGB_DATA_FILE`;
		`touch $job_build_dir/data.txt`; `chmod 755 $job_build_dir/data.txt`;
}

#################################################
# Copy all the Required Files to WorkSpace
sub COPY_TO_WORKSPACE
{
        chdir ($CHECK_IN_FILES)or die "Unable to Switch to dir $CHECK_IN_FILES $! \n";
        `cp \*.tpi $WRKSPC_BUILD_DIR`;
		`cp \*Report* $WRKSPC_BUILD_DIR`;
        `chmod 777 $WRKSPC_BUILD_DIR/*`;
        #`cp $HTML_Report $WRKSPC_BUILD_DIR`;
}
#############################################
# This is to check if the FD values are Failed
sub FD_PASS_FAIL
{
        print "\n\n Module FD_PASS_FAIL called...... \n\n";
    my $pass ="PASSED";
        my $NA = "NOT Applicable";
    if ( grep( /$pass/,@fd_pass_fail) || grep( /$NA/,@fd_pass_fail) )
        {
                print "\n\nThe FD PASS or FAIL module has PASSED \n\n";
        }
        else
        {
                print "\n\nAll the FD Check's are Failed... \n\n";
        exit(55);
    }
}

###########################################################
### Function to remove the TP which faile with comments
sub Remove_TP_Failed
{
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";
        print "\nIn the Remove_TP_Failed Function";
        if(@tp_comment_failed)
        {
                foreach (@all_tpi)
                {
                        chomp($_);
                        my $tp_full_path= $_;
                        #my $tp_val = (split /\//,$_)[-1];
                        my $tp_value = (split /_R[0-9]/,$_)[0];
                        #chomp($tp_val);
                        chomp($tp_value);
                        $tp_value =~ s/ //g;
                        if(grep( /^$tp_value$/,@tp_comment_failed ))
                        {
                                print "\n\nRemoving the Tech Pack $CHECK_IN_FILES$_ as it failed to validate Comments \n\n";
                                `rm -rf $CHECK_IN_FILES$_`;
                        }

                }
        }
        print "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";
}       #Remove_TP_Failed CLOSED

sub Create_TP_Order_File
{
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";
        print "\n Creating the Tech Pack Order Text File \n";
                # Copying the Final list file to text file
                my @TP_CHECK_INFILES = `ls $CHECK_IN_FILES`;
                #print "\n\n LIST of Files in $CHECK_IN_FILES are \n : @TP_CHECK_INFILES \n";
                foreach(@TP_CHECK_INFILES)
                {
                        chomp($_);
                        `echo "$_" | tee -a $KGB_DATA_FILE`;
                }
        print "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";


}

########################################
### function to store changed TPI Files
sub Create_Data_File
{
		print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";
		print "\n Checking TPI Files \n";
				# Checking changed TPI files
				#`cd builds/${BUILD_NUMBER}`;
				my @TP_CHECK_INFILES = `ls $KGB_PACK_DIR | egrep '(Report|tpi)'`;
				#print "\n\n LIST of TPI Files in $CHECK_IN_FILES are \n : @TP_CHECK_INFILES \n";
				my $var ;
				my $filename = "${job_build_dir}/data.txt";
				open(FH, '>>', ${filename}) or die $!;
				foreach(@TP_CHECK_INFILES)
				{
						chomp($_);
						$var = $_;
						#$var  = substr($_,20,-2);
						print FH $var."\n";
				}
				close(FH);
		print "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";


}

########################################
### function to Copy the CSV and PM files
sub COPY_CSV_PM
{
        #foreach (@NODE_NAMES_FOR_CSV_PM_FILES)
        #{
                #`mkdir -p $KGB_DATA_CSV_PM_DIR;
                chomp($_);
                $_ =~ s/\s+//g;
                if ($_)
                {
                        my $Node_Name = $_;
                        print "\n The Node Name is : $Node_Name \n";


                        #grep /vobs/eniq polling.log | grep 'xml\|csv' | grep erbsg2_etl | awk -F " " '{print $3}' | sed 's/"//g' | uniq
                        #grep /vobs/eniq $Polling_log_file | grep 'xml\\|csv' | grep '$Node_Name' | awk '{FS="\" \""; print \$3}' |sed 's/\"//g' | sort | uni
                        my @CSV_PM_FILES = `grep /vobs/eniq $Polling_log_file | grep 'xml\\|csv' | grep '$Node_Name' | awk -F " " '{print \$3}' |sed 's/\"//g' | sort | uniq `;
                        print " The Node $Node_Name has got this CSV and PM Files : \n @CSV_PM_FILES \n";
                        if ( $Node_Name =~ m/_/ )
                        {
                                $Node_Name = (split/_/,$Node_Name)[0];
                                $Node_Name = uc($Node_Name);
                        }

                        my $NODE_DIR = "$KGB_DATA_CSV_PM_DIR/$Node_Name";

                        `mkdir -p $NODE_DIR`;

                        for my $File (@CSV_PM_FILES)
                        {
                                $File =~ s/\s+//g;
                                $File =~ s/\/view\/tp_kgb_linux_jenkin_view//g;
                                chomp $File;
                                print "Copying the $File to $NODE_DIR \n";
                                `/usr/atria/bin/cleartool setview -exec 'cp -rf $File $NODE_DIR' ${CLEARCASE_VIEWTAG}`;
                        }
                } # if($_) closed

        #}


}

########## Main Function

{
        CREATE_FILES_AND_DIR();
        GET_ALL_TP_INFO();
        Copy_TP();
        #Remove_TP_Failed();
        Create_TP_Order_File();
        COPY_TO_WORKSPACE();
        Create_Data_File();
        #if (@NODE_NAMES_FOR_CSV_PM_FILES)
        #{
        #       COPY_CSV_PM();
        #}
        #else
        #{
        #       print "\n There are No CSV or PM Files \n";
        #}
        if (@all_tpi)
        {
                HTML_REPORT();
        }

	#FD_PASS_FAIL();
}


