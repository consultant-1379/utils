#!/usr/bin/perl 
use strict;
use warnings;

print "\n\n\n\n Executing the Package Installation Check script \n\n\n\n";


my @All_TP=`cat /eniq/sw/installer/Tech_pack_order.txt`;

if ( ! -e "/eniq/sw/installer/Tech_pack_order.txt" )
{
        print "\n\n The input file is missing. So exiting....\n\n";
        exit 55;
}

chomp(@All_TP);

my $HTML_REPORT = "/eniq/sw/installer/TP_BO_Installation_Status.html";
my $Installation_Status_Text_File = "/eniq/sw/installer/TP_BO_Installation_Status.txt";
my $Install_Failed_File = "/tmp/installation_failed.txt";

#######################################################
# Function to Generate a HTML Report
sub Generate_Report
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
                open(my $status_file_update,'>>', "$Installation_Status_Text_File");
        my $report;
        
        $report.= getHtmlHead();

        foreach my $tp (@All_TP)
        {       
                print " Full TP name is : $tp \n";
                my $temp_tp = (split /\./,$tp)[0];
                my $tech_pack = (split /_R[0-9]/,$temp_tp)[0];
                my $RState = (split /$tech_pack\_/,$temp_tp)[1];
                chomp $tech_pack;

                                if ( system("grep '^$tech_pack' $Install_Failed_File ") != 0 )
                                {
                                $report.="<tr bgcolor=\"#99ffdd\" align=\"center\"><td>$SNo</td><td> $tech_pack </td><td>$RState</td><td bgcolor=\"green\"><b>PASSED</td></tr>";
                                                                print $status_file_update "$tp,PASSED\n";
                                }
                                else
                                {
                                $report.="<tr bgcolor=\"#99ffdd\" align=\"center\"><td>$SNo</td><td> $tech_pack </td><td>$RState</td><td bgcolor=\"red\"><b>FAILED</td></tr>";
                                                                print $status_file_update "$tp,FAILED\n";
                                }
                                
            ### increment the Sno
                $SNo++; 
        } # for looop closed

        $report.=getHtmlTail();
        print " Installation Status Html Report value is : $report \n";
        open(my $out, '>', $HTML_REPORT) or die "Could not open file '$HTML_REPORT' $!";
        print $out "$report";
        close $out;
} ###Check_Installation Closed



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
        Generate_Report();
}

