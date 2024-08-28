#!/view/eniq_view/vobs/cello/cade_A_tools_perl/SunOS/sparc/bin/perl -w
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
#   Description  : This Script is get the Platform packages and its related info according to SCM polling.
#   REV          : A1
# --------------------------------------------------------------

use strict;
use warnings;
no warnings 'uninitialized';

my $JENKINS_HOME = $ARGV[0];
my $JOB_URL = $ARGV[1];
my $BUILD_NUMBER = $ARGV[2];
my $WORKSPACE = $ARGV[3];

my $comment;

my $jenkin_job_dir = ${JENKINS_HOME}."/jobs/";
my $PF_KGB_DATA_DIR = ${JENKINS_HOME}."/FULL_PF_KGB_DATA/";
my $PF_KGB_DATA_CURRENT_DIR = $PF_KGB_DATA_DIR."$BUILD_NUMBER";
my $CHECK_IN_FILES = $PF_KGB_DATA_DIR."$BUILD_NUMBER"."/CHECK_IN_FILES/";
my $output_file = $PF_KGB_DATA_DIR."$BUILD_NUMBER"."/xid_comment_tech.txt";
my $PF_KGB_DATA_FILE = $PF_KGB_DATA_CURRENT_DIR."/Platform_order.txt";

my $jobname= (split /\//,$JOB_URL)[-1];
my $job_build_dir = $jenkin_job_dir."$jobname"."/builds/"."$BUILD_NUMBER/";
my $WRKSPC_BUILD_DIR = $WORKSPACE."/workspace/".$jobname."/".$BUILD_NUMBER."/";
my $HTML_Report = $WRKSPC_BUILD_DIR."HTML_REPORT.html";

my $CLEARCASE_VIEWTAG = "platformjenkins_view";

my $MWS_DEST_PATH = "/tmp/PF_KGB/";
my $MWS_USER="root";
my $MWS_PASSWORD="shroot12";
my $MWS_SERVER = "ieatrcx6786.athtem.eei.ericsson.se";
my $Polling_log_file= $job_build_dir."polling.log";
my $change_log_xml= $job_build_dir."changelog.xml";

my @pf_modules = ("AdminUI", "alarmcfg", "alarm", "BusyHour", "common", "diskmanager", "dwhmanager", "ebsmanager", "engine", "eniq_config", "export", "helpset_stats", "installer", "libs", "licensing", "monitoring", "mediation", "repository", "runtime", "scheduler", "statlibs", "symboliclinkcreator", "uncompress");
my @pf_pkgs_checked_in;

print "===================================================================\n";
print "JOB URL is $JOB_URL \n";
print "Build Number is $BUILD_NUMBER \n";
print "Job Name is $jobname \n";
print "Job Build Dir is $job_build_dir \n";
print "Work Space is $WORKSPACE \n";
print "Work Space Current Build directory is $WRKSPC_BUILD_DIR \n";
print "===================================================================\n";

if ( ! -e $Polling_log_file)
{
	print " The Polling log for the Build $job_build_dir doesn't Exists. So Exiting..... \n";
	exit(6);
}

my @all_zip=`grep /vobs/eniq $Polling_log_file | sort | uniq | sed s'/"//g'| awk '{print \$2 \$3}'| awk '!seen[\$0]++' | grep zip | awk -F '/' '{print \$1","\$NF}' `;

my @zip_full_paths = `grep /vobs/eniq $Polling_log_file | sort | uniq | sed s'/"//g' | awk '{print  \$3}' | awk '!seen[\$0]++' | grep zip | cut -d'/' -f4- | awk '{print "/"\$0}'`;

sub uniq {
    my %seen;
    grep !$seen{$_}++, @_;
}

@all_zip=uniq(@all_zip);


############################################################
###### Below code gives the info about zip, XID and Comments and writes to a file
sub GET_ALL_PLATFORM_INFO
{
	print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n";
	chdir("$job_build_dir") or die "Unable to Switch to Build dir $job_build_dir $!\n";

	if (@all_zip)
	{
		print "*******************************************************************\n";
		print "We have these Platform Checked In \n @all_zip \n\n\n";
		print "********************************************************************\n";
		foreach (@all_zip)
		{
			chomp($_);
			my $xid = (split /,/ , $_)[0];
			$xid =~ s/\s+//g;
			my $plat_name = (split /,/ , $_)[1];
			$plat_name =~ s/\s+//g;
			my $plat_value = (split /_R[0-9]/,$plat_name)[0];
			chomp($plat_value);
			
			if ( grep( /^$plat_value/, @pf_modules ) ) { 
				my ($plat_full_path) = grep { /$plat_name/ } @zip_full_paths;
				print "The full Path for the platform $plat_name is : $plat_full_path \n";
				chomp($plat_full_path);
				$plat_full_path =~ s/ //g;
				my $cleartool_cmd = "/usr/atria/bin/cleartool desc ".$plat_full_path;
				$comment =`/usr/atria/bin/cleartool setview -exec "$cleartool_cmd" ${CLEARCASE_VIEWTAG} | grep ship`;
				chomp($comment);
				$comment =~ s/"//g;
				$comment =~ s/ //g;	
				$comment = (split /,/,$comment)[0];
				$comment = (split /:/,$comment)[1];

				my $rel = (split /\./,$comment)[0];
				my $num = (split /\./,$comment)[1];
				chomp($xid);
				chomp($plat_name);
				chomp($comment);
				
				if ($rel eq "19" and $num ge '4'){
					push (@pf_pkgs_checked_in,$plat_full_path);
					print "\n=====================================================================";  
					print "\nThe XID is $xid, Platform Package Name is $plat_name, Shipment is $comment\n";
					print "\n=====================================================================\n";
					open (Outputfile , ">> $output_file");
					print Outputfile "$xid===$plat_name===$comment\n";
					close Outputfile;
				}
				else{
					print "$plat_name is NOT a Linux Package!! ==> Package delivered to $comment shipment\n";
				}
			}
		}
		
		if (scalar @pf_pkgs_checked_in == 0) {
			print "Oops!! No Platform are checked in during this SCM Poll.\n";
			exit(5);
		}
	}
	else 
	{
		print "Oops!! No Platform are checked in during this SCM Poll.\n";
		exit(5);
	}
	print "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";
}	# GET_ALL_PLATFORM_INFO CLOSED


##### GET HTML Head
sub getHtmlHead{
return qq{
            <html><head><title>Platform Details Table</title></head>
            <body><table border="2"><tr><th><b> XID </th><th><b>Platform Packages</th><th><b>Shipment</th></tr>
         };
}

###########################################################
### Function to copy the PLATFORM to respective areas.
sub Copy_PLATFORM
{
	print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>";  
	print "\nCopying the latest platform packages to $CHECK_IN_FILES folder.\n";
	### copying the latest platform packages to $CHECK_IN_FILES folder.
	foreach (@pf_pkgs_checked_in)
        {
			chomp($_);
			my $plat_full_path= $_;
			my $platform_val = (split /\//,$_)[-1];
			my $platform_value = (split /_R[0-9]/,$platform_val)[0];
			chomp($platform_val);
			chomp($platform_value);
			$platform_value =~ s/ //g;
			print " The platform_value is $platform_value \n";
			print " The Platform Full path is $plat_full_path \n\n\n";
			
			print "Coping the Platform package $platform_val to $CHECK_IN_FILES path \n\n";
			`/usr/atria/bin/cleartool setview -exec 'cp -rf $plat_full_path $CHECK_IN_FILES' ${CLEARCASE_VIEWTAG} `;
	} # for closed
	
	`chmod 777 $CHECK_IN_FILES/*`;
	print "\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n";
}	#Copy_PLATFORM CLOSED

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
        chdir($PF_KGB_DATA_DIR)or die "Unable to Switch to dir $PF_KGB_DATA_DIR $! \n";
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
			my $plat_name = $temp_array[1];
			my $comment = $temp_array[2];
			$report.="<tr><td>$xid</td><td>$plat_name</td><td>$comment</td></tr>";
		}
	}
	$report.=getHtmlTail();
	print "The html page is $report \n";
	my $report_page = $HTML_Report	;
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
	`mkdir -p $PF_KGB_DATA_DIR;chmod 777 $PF_KGB_DATA_DIR`;
	chdir($PF_KGB_DATA_DIR)or die "Unable to Switch to dir $PF_KGB_DATA_DIR $! \n";
	`mkdir -p $WRKSPC_BUILD_DIR;chmod 777 $WRKSPC_BUILD_DIR`;
	`mkdir -p $PF_KGB_DATA_CURRENT_DIR;chmod 777 $PF_KGB_DATA_CURRENT_DIR`;
	`mkdir -p $CHECK_IN_FILES;chmod 777 $CHECK_IN_FILES`;
	`touch  $output_file;touch $PF_KGB_DATA_FILE`;
	`chmod 755 $output_file $PF_KGB_DATA_FILE`;
}


########## Main Function

{
	CREATE_FILES_AND_DIR();
	GET_ALL_PLATFORM_INFO();
	Copy_PLATFORM();
	if (@all_zip)
	{	
		HTML_REPORT();
	}
	print "PASS";
}	
