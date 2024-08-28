#!/usr/bin/perl 
use strict;
use warnings;

use Cwd;

print "\n\n\n\n Executing the Package Installation Check script \n\n\n\n";

my $Main_tech_pack= "/eniq/log/sw_log/engine/";


chdir($Main_tech_pack) or die "Can not Change the Engine log dir $! \n";

my @All_TP=`cat /eniq/sw/installer/Tech_pack_order.txt`;

chomp(@All_TP);

my $HTML_REPORT = "/eniq/sw/installer/TP_BO_Installation_Status.html";

#######################################################
# Function to check the Installation Status and Generate a HTML Report
sub Check_Installation
{
        my $SNo = 1;
        # Check if HTML Report file exists if exists delete and re create it 
        if ( -e $HTML_REPORT )
        {
                `rm -rf $HTML_REPORT; touch $HTML_REPORT; chmod 755 $HTML_REPORT`;
        }
        else
        {
                `touch $HTML_REPORT; chmod 755 $HTML_REPORT`;
        }

        my $report;
        
        $report.= getHtmlHead();

        foreach my $tp (@All_TP)
        {       
                print " Full TP name is : $tp \n";
                my $temp_tp = (split /\./,$tp)[0];
                my $tech_pack = (split /_R[0-9]/,$temp_tp)[0];
                my $RState = (split /$tech_pack\_/,$temp_tp)[1];
                chomp $tech_pack;
                my $curr_dir;
                if ($tech_pack =~m /INTF/ )
                {
                        $curr_dir=$Main_tech_pack.$tech_pack."-eniq_oss_1";
                }
                else 
                {       
                        $curr_dir=$Main_tech_pack.$tech_pack;
                }
                if ( -d $curr_dir )
                {       
                        chdir($curr_dir) or die "Can not change directory for Installation Directory $curr_dir $!\n";
                        print "In the $curr_dir directory \n";
                        system("chmod 777 *");

                        my $Log_File= `ls $curr_dir | tail -1 `;
                        print "The Log file in  $curr_dir is $Log_File \n";

                        if ( system("grep -i 'warning' $Log_File ") != 0 && system("grep -i 'exception' $Log_File ") != 0 && system("grep -i 'skip' $Log_File ") != 0 && system("grep -i 'failure' $Log_File ") != 0 && system("grep -i 'error' $Log_File | grep -v INFO ") != 0 )
                        {                       
                                print "The installtion is Succesfull for $tech_pack \n";
                                $report.="<tr bgcolor=\"#99ffdd\" align=\"center\"><td>$SNo</td><td> $tech_pack</td><td>$RState</td><td bgcolor=\"green\"><b>PASSED</td></tr>";
                        }
                        else 
                        {
                                print " The installation is UnSuccessfull/Failed for $tech_pack \n";
                                $report.="<tr bgcolor=\"#99ffdd\" align=\"center\"><td>$SNo</td><td> $tech_pack</td><td>$RState</td><td bgcolor=\"red\"><b>FAILED</td></tr>";
                                chdir("/tmp") or die "Unable to switch to tmp directory $!\n";
                                if (! -e "/tmp/installation_failed.txt")
                                {
                                                system("touch /tmp/installation_failed.txt");
                                                system("chmod 777 /tmp/installation_failed.txt");
                                                #system("chown dcuser:dc5000 /tmp/installation_failed.txt");
                                }
                                else
                                {
                                        `rm -rf /tmp/installation_failed.txt;touch /tmp/installation_failed.txt;chmod 777 /tmp/installation_failed.txt`;
                                }
                                my $tp_failed = (split /_R[0-9]/,$tech_pack)[0];
                                open(my $fh, '>>', '/tmp/installation_failed.txt');
                                print $fh "$tp_failed\n";
                                close $fh;
                                print(" The Tech Packs that failed while installing is/are: ");
                                system("cat /tmp/installation_failed.txt");
                        }
                }
                else 
                {
                        print "There is no $curr_dir directory \n";
                }
            ### increment the Sno
                $SNo++; 
        } # for looop closed

        $report.=getHtmlTail();
        #print " Installation Status Html Report value is : $report \n";
        open(my $out, '>', $HTML_REPORT) or die "Could not open file '$HTML_REPORT' $!";
        #print $out "$report";
        close $out;

} ###Check_Installation Closed


#### Code to create required file for epfg and rt is below.
sub Create_Data_Files
{

        if ( -e "/tmp/installation_failed.txt" )
        {
                print "\n\n Looks like there are some installation Failures \n\n";
                my @Failed_TP = `cat /tmp/installation_failed.txt`;
                my @Data;

                foreach (@Failed_TP)
                {
                        @Data = grep {!/^$_$/} @All_TP;
                }

                open(my $data_epfg, '>>', '/eniq/home/dcuser/data_epfg.txt');
                open(my $data,'>>', '/eniq/home/dcuser/data.txt');
                foreach (@Data)
                {
                        chomp($_);
                        print $data "$_\n";
                                                if ($_ =~ /^BO/)
                                                {
                                                        my $tp_name = (split /_R[0-9]/,$_)[0];
                                                        print $data_epfg "$tp_name\n";
                                                }
                                                else
                                                {
                                                        my $tp_name = (split /_R[0-9]/,$_)[0];
                                                        print $data_epfg "$tp_name\n";
                                                }
                }
                close $data_epfg;
                close $data;
        }
        else
        {

                open(my $data_epfg, '>>', '/eniq/home/dcuser/data_epfg.txt');
                open(my $data,'>>', '/eniq/home/dcuser/data.txt');
                foreach (@All_TP)
                {
                        chomp($_);
                        print $data "$_\n";
                                                if ($_ =~ /^BO/)
                                                {
                                                        my $tp_name = (split /_R[0-9]/,$_)[0];
                                                        print $data_epfg "$tp_name\n";
                                                }
                                                else
                                                {
                                                        my $tp_name = (split /_R[0-9]/,$_)[0];
                                                        print $data_epfg "$tp_name\n";
                                                }

                }
        }
        `chmod 777 /eniq/home/dcuser/data_epfg.txt`;
        `chmod 777 /eniq/home/dcuser/data.txt`;

}  ##Create_Data_Files Closed

############################################################
# GET HTML TAIL
sub getHtmlTail{
return qq{
                        </table></body></html>
        };
}

##### GET HTML Head
sub getHtmlHead{
return qq{
            <html><head><title>Tech Pack Installtion Status Details Table</title></head>
            <body><table border="1"><tr bgcolor="#0066cc"><th ><b> S.No </th><th ><b>Tech Pack Name</th><th ><b>R-State</th><th ><b>Installation Status</th></tr>
         };
}

############### Main Function ################
{
        Check_Installation();
        Create_Data_Files();
}

