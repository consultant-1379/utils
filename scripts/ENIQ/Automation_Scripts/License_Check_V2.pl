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
#   DATE         : 24/07/2017
#   Description  : This Script is to check the License is valid under which a TP is bundled in FDM model.
#   REV          : A1 
# --------------------------------------------------------------
#   
# 

# set the variable to install the tech pack's
#system("export CONF_DIR=/eniq/sw/conf");

use strict;
use warnings;
use Getopt::Long;
use File::Copy;
no warnings 'uninitialized';
use Term::ANSIColor qw(:constants);


###### Variables ####
my $help;
my $Release;
my $Shipment;
my $List;
my $TP;
my $Rel;
my $Rel_Num;
my $Num;
my $Rel_Alphabet;
my $Feature_Path;
my $Properties_File;
my $MWS_Shared_Path = "/net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/";
my $Extract_TP_Script = "/eniq/sw/installer/extract_report_packages.bsh";
my $Installer_Path = "/eniq/sw/installer/";
my $BOREPORTS_PATH = $Installer_Path."/boreports/";
my $CXC_List;


########## ARRAYS #####
my @Rel_Num;
my @CXC_List;
my @Final_CXC_List;

sub usage{
        print "Unknown option: @_\n" if ( @_ );
        print "usage: program [-r RELEASE] [-s SHIPMENT] [-l LIST of CXC's ][-help|-?]\n";
        exit;
}

sub PARAMETERS
{
        usage() if ( @ARGV < 1 or ! GetOptions('help|?' => \$help, 'release|r=s' => \$Release, 'ship|s=s' => \$Shipment, 'list|l=s' => \$CXC_List) or defined $help );

        if ( (!$Release) || (!$Shipment) || (!$CXC_List) )
        {
                usage();
        }

        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n";
        if($Release){
                     if ($Release !~ /^ENIQ_S[0-9][0-9].[0-9]$/)
                     {
                        print " The Release entered is $Release Wrong, Please check it \n";
                        exit(5);
                     }
                print "Release is: $Release\n";
        }
        
        if($Shipment){
                       if ($Shipment !~ /^[0-9][0-9].[0-9].[0-9]/)
                        {
                                if ($Shipment !~ /^[0-9][0-9].[0-9].[0-9].EU[0-9]/)
                                {       
                                        print  "The Shipment entered is $Shipment Wrong, Please check it \n";
                                        exit(5);
                                }
                        }
                print "Shipment is : $Shipment\n";
        }

        $Rel_Num = (split /ENIQ_S/, "$Release")[1];
        #print "Rel_Num is $Rel_Num \n";

        @Rel_Num = (split /ENIQ_S/, "$Release")[1];
                
        $Rel =( split /\./, "$Rel_Num")[0];
        $Num =( split /\./, "$Rel_Num")[1];
                
        if ($Num == "0")
        {
                $Feature_Path= "Features_"."$Rel"."A";
                $Rel_Alphabet = "A";
        }
        if ($Num == "2")
        {
                $Feature_Path= "Features_"."$Rel"."B";
                $Rel_Alphabet = "B";
        }
        if ($Num == "4")
        {
                $Feature_Path= "Features_"."$Rel"."C";
                $Rel_Alphabet = "C";
        }

        if($CXC_List)
        {
                print "CXC LIST is : $CXC_List\n";
                @CXC_List = split /,/, $CXC_List;
        }
        $MWS_Shared_Path = $MWS_Shared_Path."$Feature_Path"."_$Shipment"."/eniq_techpacks";
        print "MWS Shared Path is : $MWS_Shared_Path \n";
        print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n";

}

####################################################################################################################
### Function to check if the Given Values of CXC are valid and the zip files Exists or not. and unzip the ZIP files 

sub PRE_CHECKS
{
        print GREEN, "\n Running PRE CHECKS \n", RESET;
        foreach my $cxc (@CXC_List)
        {
                chomp($cxc);
                $cxc =~ s/\s+//g;
                if ( $cxc =~ /^CXC[0-9]{7}$/ )
                {
                        if ( -e  "/$cxc.zip")
                        {
                                print GREEN, "\n Unziping the $cxc.zip \n", RESET;
                                system("unzip -oj \"/$cxc.zip\" -d /$cxc");
                                push (@Final_CXC_List,$cxc);
                        }
                        else
                        {
                                print RED, "\n $cxc zip file Doesn't Exists. Please Check\n", RESET;
                        }
                }
                else
                {
                        print RED, "\n $cxc is NOT a VALID CXC number \n", RESET;
                }
                
        }       
        print "\n Final_CXC_List list is : @Final_CXC_List \n";
        print GREEN, "\n PRE CHECKS Completed \n", RESET;
}


###############################################################################################
# function to Check the license value is correct using which the tp is packgerd
sub LICENSE_CHECK
{
        foreach my $CXC (@Final_CXC_List)
        {
                print WHITE, "\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n", RESET;
                print GREEN, "\n Feature $CXC License Check STARTED \n", RESET;
                my @TP_LIST = `ls "/$CXC"`;
                foreach my $TP (@TP_LIST)
                {
                        $Properties_File = undef;
                        print MAGENTA," \n\n =========================================================== \n\n", RESET;
                        print "Tech Pack name : $TP \n";
                        chomp($TP);
                        my $TP_FULL_NAME = $TP;
                        $TP_FULL_NAME =~ s/\s+//g;
                        my $TP_RSTATE_NAME = ( split /\./, "$TP_FULL_NAME")[0];
                        my $TP_ORG_NAME = (split /_R[0-9]/,"$TP_FULL_NAME")[0];
                        chomp($TP_RSTATE_NAME);
                        chomp($TP_ORG_NAME);
                        my $TP_TEMP_DIR = "/var/tmp/$TP_RSTATE_NAME/";
                        my $TP_ABS_PATH = "/$CXC/".$TP_FULL_NAME;
                        if (-d "$TP_TEMP_DIR"){
                                `rm -rf $TP_TEMP_DIR`;
                        }
                        `mkdir -p $TP_TEMP_DIR`;
                        #print CYAN,"\n Copying the Tech Pack $TP_ABS_PATH to $TP_TEMP_DIR\n", RESET;

                        `cp $TP_ABS_PATH $TP_TEMP_DIR; chmod 777 $TP_TEMP_DIR/*`;
                        

                        if ( $TP =~ /^DC|^DIM|^DWH|^LTE|^PM|^UTRAN|^AlarmInterfaces|^BO/ )
                        {
                                $Properties_File = extract_TP($TP_TEMP_DIR,$TP_RSTATE_NAME);

                                if ( -e "$Properties_File")
                                {
                                        check_License($CXC,$Properties_File,$TP_RSTATE_NAME);
                                }
                                else
                                {
                                        print RED, "\n $Properties_File doesn't exists !!! \n", RESET;
                                }

                        }
                        elsif ( $TP =~ /^INTF/ )
                        {
                                $Properties_File = undef;
                                print GREEN,"\n Skipping interface $TP\n", RESET; 
                        }
                        else
                        {
                                print RED, "The $TP is NOT a VALID Tech Pack \n", RESET;
                        }       
                
                }
                print GREEN,"\n Feature $CXC License Check COMPLETED \n", RESET; 
                print WHITE, "\n <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n", RESET;
        }
}


##############################################
# Function to extract TP
sub extract_TP
{
        my $TP_DIR = shift;
        my $TP_RSTATE_NAME=shift;
        my $Lic_File = undef;
        #`su - dcuser -c "cd $Installer_Path;$Extract_TP_Script $TP_DIR"`;

        ###Extracting the Packages........
        `su - dcuser -c "cd $Installer_Path;$Extract_TP_Script $TP_DIR"`;
        #`cd $Installer_Path;$Extract_TP_Script $TP_DIR`;
        my $res = `echo $?`;
        if ( $res != 0 )
        {
                print RED, "\nExtraction of Tech Pack $TP_RSTATE_NAME has Failed!!!\n", RESET;
        }
        $Lic_File = $BOREPORTS_PATH.$TP_RSTATE_NAME."/install/version.properties";
        return $Lic_File;
}

#######################################################
# Function to check the License is Valid or NOT
sub check_License
{
        my $CXC = shift;
        my $Properties_File = shift;
        my $TP_RSTATE_NAME =    shift;
        my $License = `grep 'license.name' $Properties_File | cut -d= -f2` ;
        my @Licenses = split /,/, $License;
        print " License's for Tech Pack $TP_RSTATE_NAME is/are = @Licenses \n";
        if ( grep /$CXC/, @Licenses)
        {
                print GREEN, " $TP_RSTATE_NAME tech pack License $CXC is Valid !!!\n", RESET;
                check_Dependency($CXC,$Properties_File,$TP_RSTATE_NAME);
        }
        else
        {
                print RED, "$TP_RSTATE_NAME tech pack License $CXC is NOT Valid!!! \n", RESET;
        }
}

#############################################################
# Function to check if there are any Dependencies
sub check_Dependency
{
        my $CXC = shift;
        my $Properties_File = shift;
        my $TP_RSTATE_NAME = shift;
        my $dependencies = `grep 'required_tech_packs' $Properties_File | grep -v DWH_BASE | grep -v DWH_MONITOR | cut -d. -f2 | cut -d= -f1`;
        #print CYAN, "\n Dependent Packages are $dependencies \n", RESET;
        my @dependencies = split(/\n+/, $dependencies);

        if (@dependencies)
        {
                foreach (@dependencies)
                {
                        chomp($_);
                        #$_ =~ s/\s+//g;
                        extract_Dependent_TP($_,$CXC);
                }
        }
        else
        {
                print CYAN, "\n NO Required Tech Packs found for $TP_RSTATE_NAME \n", RESET;
        }

}

#############################################################
# Function to extract the Dependdency Packages from teh MWs server
sub extract_Dependent_TP
{
        my $TP = shift;
        $TP = $TP."_";
        my $CXC = shift;
        print YELLOW, "\n Dependent Tech Pack Name is $TP\n", RESET;
        my $TP_IN_MWS = `ls $MWS_Shared_Path | grep '^$TP'`;
        print "MWS Shared Path : ".$MWS_Shared_Path;
        print "TP in MWS : ".$TP_IN_MWS;
        $TP_IN_MWS =~ s/\s+//g;
        if ( !$TP_IN_MWS )
        {
                print RED, "\n Reuiqred Tech Pack $TP doesn't exists in $MWS_Shared_Path, Please Check !!! \n", RESET;
        }
        print YELLOW, "\n Dependent Tech Pack Name in MWS is $TP_IN_MWS\n", RESET;
        my $TP_ABS_PATH = $MWS_Shared_Path."/$TP_IN_MWS";
        chomp($TP_ABS_PATH);
        $TP_ABS_PATH =~ s/\s+//g;
        print YELLOW, "\n Tech Pack Absolute Path is $TP_ABS_PATH\n", RESET;
        
        if ( ! -e $TP_ABS_PATH )
        {
                print RED, "\n $TP_ABS_PATH doesn't exists!!! \n", RESET;
        }

        my $TP_RSTATE_NAME = ( split /\./, "$TP_IN_MWS")[0];
        my $TP_ORG_NAME = (split /_R[0-9]/,"$TP_IN_MWS")[0];
        chomp($TP_RSTATE_NAME);
        chomp($TP_ORG_NAME);
        my $TP_TEMP_DIR = "/var/tmp/$TP_RSTATE_NAME/";
        if (-d "$TP_TEMP_DIR")
        {
                `rm -rf $TP_TEMP_DIR`;
        }
        `mkdir -p $TP_TEMP_DIR`;
        `cp $TP_ABS_PATH $TP_TEMP_DIR ; chmod 777 $TP_TEMP_DIR/*`;

        if ( $TP =~ /^DC|^DIM|^DWH|^LTE|^PM|^UTRAN|^AlarmInterfaces|^BO/ )
        {
                $Properties_File = extract_TP($TP_TEMP_DIR,$TP_RSTATE_NAME);
                if ( -e "$Properties_File")
                {
                        check_License($CXC,$Properties_File,$TP_RSTATE_NAME);
                }
                else
                {
                        print RED, "\n $Properties_File doesn't exists !!! \n", RESET;
                }

        }
        elsif ( $TP =~ /^INTF/ )
        {
                $Properties_File = undef;
                print GREEN, "\n Skipping the Interface $TP \n", RESET; 
        }
        else
        {
                print RED, "The $TP is NOT a VALID Tech Pack \n", RESET;
        }       
}

        
#### Main Function ######
{
        PARAMETERS();
        PRE_CHECKS();
        LICENSE_CHECK();
        
}
