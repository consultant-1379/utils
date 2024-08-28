#!/view/eniq_view/vobs/cello/cade_A_tools_perl/SunOS/sparc/bin/perl -w

use strict;
use Getopt::Long;
use Expect;
#use POSIX qw(strftime);
use File::Basename;
use File::Copy;
#use lib "/vobs/ossrc/del-mgt/bin";
#use EniqEvents;

# ********************************
#
# CONFIGURATION SECTION
#
# ********************************
my $serverDetails = "/view/eniq_dmstats_ci/vobs/ossrc/del-mgt/bin/eniq_server_details.txt";
my $iniratorQuestionsAndAnswers;
my $statsBladeQuestions;
my $statsRackQuestions;

my $TMP_FILE;

my $runtime;
#my $run_time=strftime "%Y%m%d-%H:%M:%S", localtime;
my ($ss,$sm,$sh)=localtime;
my $ch;
my $cm;
my $cs;
my ($help, $rel, $ship, $llsv_no, $mach, $arch, $servertype, $type, $build, $features, $master_log, $time_zone, $operatingSystem, $SAN_TYPE);
my $RELEASE;
my $SHIPMENT;
my $LLSV_NO;
my $MACHINE;
my $BUILD_TYPE;
my $BUILD_TYPE1;
my $stat;
my $linloc;
my $linomloc;
my $sms_signum;
my $SMS_SIGNUM;

###########################
# Server Details Global Variables
###########################
my $hostname;
my $host;
my $macaddr;
my $ip_addr;
my $ARCH;
my $ilo_ip_addr;
my $SERVERTYPE;
my $def_route;
my $CLAR_HOST;
my $ip_SPA;
my $ip_SPB;
my $ip_NAS;
my $ip_NAS_1;
my $ip_NAS_2;
my $ip_NAS_3;
my $ip_NAS_4;
my $ip_NAS_5;
my $ip_NAS_6;
my $ip_NAS_7;
my $ip_NAS_8;
my $ip_VC;
my $ip_VC_UN;
my $ip_VC_PWD;
my $storagepool;
my $ip_NAS_MS;
my $ip_NAS_SPT;
my $NO_OF_SANS;
my $ENIQ_LIC;
my $SAN_UN;
my $SAN_PWD;
my $STG_IP;
my $STG_NET;
my $OSS_IP;
my $OSS_NET;
my $LDAP_DOM;
my $LDAP_IP;
my $LDAP_PWD;
my $NET_SUBS;
my $NET_USERS;
my $PART_PLAN;
my $STG_TYPE;
my $OSS_SERVER;
my $FQDN;
my $IQ_INST;
my $DWH_READER;
my $INST_TYPE;
my $DEPLOY;
my $STG_NET_NO;
my $STG_GRP_NAME;       
my $OSSSERVICEINTF;
my $FIRSTOSSSERVICEINTF;
my $SECONDOSSSERVICEINTF;
my $STORAGEINTF;
my $FIRSTSTORAGEINTF;
my $SECONDSTORAGEINTF;
my $NETWORKTYPE; 
my $MAINDBCORE; 
my $TMPDBCORE; 
my $MAINDBGRAN; 
my $TMPDBGRAN; 
my $MAINDBWRAN; 
my $TMPDBWRAN; 
my $NOCORENODES; 
my $NOGRANNODES; 
my $NOWRANNODES; 
my $MIRRORDISKS;
my $RDISK;
my $MDISK;      
my $CONNECTED_CEP_BLADE;        
my $CEP_BLADE; #CEP blade name
my $CEP_COORD; #Coordinator IP
my $CLAR_HOST_2;
my $ip_SPA_2;
my $ip_SPB_2;
##############################
# Internal Global Variables
##############################
my $root_user = 'root';
my $PASS = "shroot12";
my $eniq_jump_svr = "10.45.192.153";
my $dm_root_storage = "shroot12";
my $confignfs= "/net/${eniq_jump_svr}";
my $configdir= "/JUMP/export/jumpstart/misc";
my $mws = "/JUMP";
my $config;
my $username = "ossrcdm";
my $jumparea;
my $sw_location;
my $expectedresult;
my $grub_stat;
my $mws_stat;

my $timeout = 5;
my $undef = undef;
my $def = 7200;
my $exp;
my $question;
my $answer;
my $count;
my @lines;
my $local_ship;
my $Rel_Num;
my @Rel_Num;
my $Rel;
my $Num;
my $Feat_Path;
my $FEATURE_PATH;
# ********************************
#
# FUNCTIONS
#
# ********************************
sub error {
        print "ERROR:";
        exit;
}
sub usage{
        print "Unknown option: @_\n" if ( @_ );
        print "usage: program [-r RELEASE] [-s SHIPMENT] [-n LLSV_NO] [-m MACHINE] [-l MASTER_LOG] [-tz TIMEZONE] [--si SMS_SIGNUM] [-help|-?]\n";
        exit;
}

sub PARAMETERS{
        usage() if ( @ARGV < 1 or ! GetOptions('help|?' => \$help, 'rel|r=s' => \$rel, 'ship|s=s' => \$ship, 'llsv_no|n=s' => \$llsv_no, 'mach|m=s' => \$mach, 'sms_signum|si=s' => \$sms_signum, 'os|o=s' => \$operatingSystem,) or defined $help );

        #usage() if ( @ARGV < 12 or ! GetOptions('help|?' => \$help,
        print "StartTime : \t$sh:$sm:$ss\n";
        print "Arguments inputted:\n\n";
        if($rel){
                if ($rel !~ /^ENIQ_S[0-9][0-9].[0-9]$/)
                {
                        print " The Release entered is $rel Wrong, Please check it \n";
                        exit(5);
                }
                print "RELEASE: $rel\n";
        }
        if($ship){
                if ($ship !~ /^[0-9][0-9].[0-9].[0-9]/)
                {
                                if ($ship !~ /^[0-9][0-9].[0-9].[0-9].EU[0-9]$/)
                                {
                                        print "The Shipment entered is $ship Wrong, Please check it \n";
                                        #exit(5);
                                }
                }
                print "SHIPMENT: $ship\n";
        }

        $Rel_Num = (split /ENIQ_S/, "$rel")[1];

        @Rel_Num = (split /ENIQ_S/, "$rel")[1];

        $Rel =( split /\./, "$Rel_Num")[0];
        $Num =( split /\./, "$Rel_Num")[1];
        if ($Num == "0"){
        $Feat_Path= "Features_"."$Rel"."A";
        }
        if ($Num == "2"){
        $Feat_Path= "Features_"."$Rel"."B";
        }
        if ($Num == "4"){
        $Feat_Path= "Features_"."$Rel"."C";
        }

        $FEATURE_PATH = "/net/${eniq_jump_svr}/JUMP/ENIQ_STATS/ENIQ_STATS/${Feat_Path}_${ship}";
        #$FEATURE_PATH = "/net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/Features_19B_19.2.11";
        if ($ship eq "17.2.8EU2_LATEST_DO_NOT_USE_OR_DELETE")
        {
                $FEATURE_PATH = "/net/${eniq_jump_svr}/JUMP/ENIQ_STATS/ENIQ_STATS/Features_17B_17.2.8.EU2"; 
        }
        print "FEATURE PATH: $FEATURE_PATH\n";
        print "LLSV Number: $llsv_no\n";
        print "MACHINE: $mach\n";

        if($sms_signum){
                print "SMS Signums: $sms_signum\n";
                $SMS_SIGNUM = $sms_signum;
        }
        if($operatingSystem){
                print "Operating System is $operatingSystem\n";
        }

        $RELEASE = $rel;
        $SHIPMENT = $ship;
        $LLSV_NO = $llsv_no;
        $MACHINE = $mach;
        
        if($operatingSystem){
                if($operatingSystem eq "linux"){
                        $config = "config_file_${mach}_linux";
                }
        }
        
        if($operatingSystem){
                if($operatingSystem eq "solaris"){
                        $config = "config_file_${mach}";
                }
        }elsif(!$operatingSystem){
                $operatingSystem = "solaris";
                $config = "config_file_${mach}";
        }
        
        $BUILD_TYPE = $rel;
        $BUILD_TYPE =~ s/[0-9].*$//;
        print "BUILD_TYPE: $BUILD_TYPE\n\n";
        
        $TMP_FILE = "/tmp/eniq_log_${RELEASE}_${SHIPMENT}.txt";
        if(-f $TMP_FILE){
                unlink($TMP_FILE);
        }
}

sub ENIQRACKDETAILS{
        open(SERVERDETAILS, $serverDetails) || die "Can not open file $serverDetails";
        my @eniqServerdedetails=<SERVERDETAILS>;
        close(SERVERDETAILS);

        foreach (@eniqServerdedetails){
                # read the fields in the current record into an array
                my @fields = split(';', $_);
                $hostname = $fields[0];
                my $bladecount = 0;
                if("$hostname" eq "$MACHINE"){
                        $host = $fields[$bladecount++];
                        $macaddr = $fields[$bladecount++];
                        $ip_addr = $fields[$bladecount++];
                        $ARCH = $fields[$bladecount++];
                        $ilo_ip_addr = $fields[$bladecount++];
                        $SERVERTYPE = $fields[$bladecount++];
                        $def_route = $fields[$bladecount++];
                        $CLAR_HOST = $fields[$bladecount++];
                        $ip_SPA = $fields[$bladecount++];
                        $ip_SPB = $fields[$bladecount++];
                        $ip_NAS = $fields[$bladecount++];
                        $ip_NAS_1 = $fields[$bladecount++];
                        $ip_NAS_2 = $fields[$bladecount++];
                        $ip_NAS_3 = $fields[$bladecount++];
                        $ip_NAS_4 = $fields[$bladecount++];
                        $ip_NAS_5 = $fields[$bladecount++];
                        $ip_NAS_6 = $fields[$bladecount++];
                        $ip_NAS_7 = $fields[$bladecount++];
                        $ip_NAS_8 = $fields[$bladecount++];
                        $ip_VC = $fields[$bladecount++];
                        $ip_VC_UN = $fields[$bladecount++];
                        $ip_VC_PWD = $fields[$bladecount++];
                        $storagepool = $fields[$bladecount++];
                        $ip_NAS_MS = $fields[$bladecount++];
                        $ip_NAS_SPT = $fields[$bladecount++];
                        $INST_TYPE = $fields[$bladecount++];
                        #########################################
                        #######Temp solution for ENC-660#########
                        #########################################
                        if("$SHIPMENT" =~ m/^3.[2-9].[1-9]/ || "$SHIPMENT" =~ m/^4.[0-9].[1-9]/ || "$SHIPMENT" =~ m/^5.[0-9].[1-9]/ || "$SHIPMENT" =~ m/^6.[0-9].[1-9]/) {
                                if ("$INST_TYPE" == 3){
                                        $INST_TYPE = 6;
                                }
                                elsif ("$INST_TYPE" == 4){
                                        $INST_TYPE = 5;
                                }elsif ("$INST_TYPE" == 5){
                                        $INST_TYPE = 4;
                                }elsif ("$INST_TYPE" == 6){
                                        $INST_TYPE = 3;
                                }
                        }
                        #########################################
                        #######END Temp solution for ENC-660#########
                        #########################################

                        $ENIQ_LIC = $fields[$bladecount++];

                        if("$BUILD_TYPE" eq "ENIQ_E")
                        {
                                    $ENIQ_LIC = "/net/159.107.177.74/eniq/eniq_build/license/${RELEASE}";
                        }
                        if("$BUILD_TYPE" eq "ENIQ_S"){
                                $ENIQ_LIC = "/net/159.107.177.74/eniq/eniq_build/license/${RELEASE}";
                                if("$SHIPMENT" eq "16.0.1" || "$SHIPMENT" eq "16.0.2" || "$SHIPMENT" eq "16.0.3" || "$SHIPMENT" eq "16.0.4"){
                                        $ENIQ_LIC = "/net/159.107.177.74/eniq/eniq_build/license/ENIQ_S16.0_bkp";
                                }
                        }

                        $NO_OF_SANS = $fields[$bladecount++];
                        $SAN_UN = $fields[$bladecount++];
                        $SAN_PWD = $fields[$bladecount++];
                        $STG_IP = $fields[$bladecount++];
                        $STG_NET = $fields[$bladecount++];
                        $OSS_IP = $fields[$bladecount++];
                        $OSS_NET = $fields[$bladecount++];
                        $LDAP_DOM = $fields[$bladecount++];
                        $LDAP_IP = $fields[$bladecount++];
                        $LDAP_PWD = $fields[$bladecount++];
                        $NET_SUBS = $fields[$bladecount++];
                        $NET_USERS = $fields[$bladecount++];
                        $PART_PLAN = $fields[$bladecount++];
                        $STG_TYPE = $fields[$bladecount++];
                        $OSS_SERVER = $fields[$bladecount++];
                        $FQDN = $fields[$bladecount++];
                        $IQ_INST = $fields[$bladecount++];
                        $DWH_READER = $fields[$bladecount++];
                        $DEPLOY = $fields[$bladecount++];
                        $STG_NET_NO = $fields[$bladecount++];
                        $STG_GRP_NAME = $fields[$bladecount++]; 
                        
                        $OSSSERVICEINTF = $fields[$bladecount++];
                        $OSSSERVICEINTF =~ s/,/ /;
                        $STORAGEINTF = $fields[$bladecount++];
                        $STORAGEINTF =~ s/,/ /;

                        ($FIRSTOSSSERVICEINTF,$SECONDOSSSERVICEINTF) = split(/ /,$OSSSERVICEINTF);
                        ($FIRSTSTORAGEINTF,$SECONDSTORAGEINTF) = split(/ /,$STORAGEINTF);

                        $NETWORKTYPE = $fields[$bladecount++]; 
                        $MAINDBCORE = $fields[$bladecount++]; 
                        $TMPDBCORE = $fields[$bladecount++]; 
                        $MAINDBGRAN = $fields[$bladecount++]; 
                        $TMPDBGRAN = $fields[$bladecount++]; 
                        $MAINDBWRAN = $fields[$bladecount++]; 
                        $TMPDBWRAN = $fields[$bladecount++]; 
                        $NOCORENODES = $fields[$bladecount++]; 
                        $NOGRANNODES = $fields[$bladecount++]; 
                        $NOWRANNODES = $fields[$bladecount++]; 
                        $MIRRORDISKS = $fields[$bladecount++];
                        $RDISK = $fields[$bladecount++];
                        $MDISK = $fields[$bladecount++];
                        $operatingSystem = $fields[$bladecount++];
                        $SAN_TYPE = $fields[$bladecount++];

                        $CONNECTED_CEP_BLADE = $fields[$bladecount++];
                        $CONNECTED_CEP_BLADE =~ s/,/ /;
                        ($CEP_BLADE,$CEP_COORD) = split(/ /,$CONNECTED_CEP_BLADE);
                        if("$BUILD_TYPE" eq "ENIQ_E" && "$SHIPMENT" lt "3.2.7"){
                                print ("no CEP needed reseetting to none");
                                 $CEP_BLADE = "NONE";
                                 $CEP_COORD = "NONE";
                                 $CONNECTED_CEP_BLADE ="NONE,NONE"; 
                            }

                        if ($NO_OF_SANS==2) {
                                $CLAR_HOST_2=$fields[$bladecount++];
                                $ip_SPA_2=$fields[$bladecount++];
                                $ip_SPB_2=$fields[$bladecount++];
                        
                        }
                        print "Information Currently stored on Server_details file\n\n";
                        print "HOSTNAME : $host\n";
                        print "MAC_ADDR : $macaddr\n";
                        print "ARCH : $ARCH\n";
                        print "IP_ADDR : $ip_addr\n";
                        print "ILOM IP ADD : $ilo_ip_addr\n";
                        print "Server type : $SERVERTYPE\n";
                        print "DEFROUTE : $def_route\n";
                        print "Clariion/VNX Host Name : $CLAR_HOST\n";
                        print "SP A_1 : $ip_SPA\n";
                        print "SP B_1 : $ip_SPB\n";
                        print "NAS MGMT IP: $ip_NAS\n";
                        print "NAS IP 1: $ip_NAS_1\n";
                        print "NAS IP 2: $ip_NAS_2\n";
                        print "NAS IP 3: $ip_NAS_3\n";
                        print "NAS IP 4: $ip_NAS_4\n";
                        print "NAS IP 5: $ip_NAS_5\n";
                        print "NAS IP 6: $ip_NAS_6\n";
                        print "NAS IP 7: $ip_NAS_7\n";
                        print "NAS IP 8: $ip_NAS_8\n";
                        print "VIRTUAL CONNECT IP : $ip_VC\n";
                        print "VIRTUAL CONNECT UN : $ip_VC_UN\n";
                        print "VIRTUAL CONNECT PWD : $ip_VC_PWD\n";
                        print "Storage Pool : $storagepool\n";
                        print "NAS Master PWD: $ip_NAS_MS\n";
                        print "NAS Support PWD: $ip_NAS_SPT\n";
                        print "ENIQ Installation type: $INST_TYPE\n";
                        print "Licence File: $ENIQ_LIC\n";
                        print "Number of SANS: $NO_OF_SANS\n";
                        print "SAN UN: $SAN_UN\n";
                        print "SAN PWD: $SAN_PWD\n";
                        print "Storage IP: $STG_IP\n";
                        print "Storage Netmast: $STG_NET\n";
                        print "OSS IP: $OSS_IP\n";
                        print "OSS Netmast: $OSS_NET\n";
                        print "LDAP DOM: $LDAP_DOM\n";
                        print "LDAP IP: $LDAP_IP\n";
                        print "LDAP PWD: $LDAP_PWD\n";
                        print "No of Network Subscribers: $NET_SUBS\n";
                        print "No of Network Users: $NET_USERS\n";
                        print "Partition Plan: $PART_PLAN\n";
                        print "Storage Type: $STG_TYPE (ie: 1--> raw, 2--> zfs)\n";
                        print "OSS Server IP: $OSS_SERVER\n";
                        print "FQDN: $FQDN\n";
                        print "IQ Instance: $IQ_INST\n";
                        print "DWH Reader: $DWH_READER\n";
                        print "ENIQ Deployment: $DEPLOY\n";
                        print "ENIQ Storage Network Number: $STG_NET_NO\n";
                        print "ENIQ Storage Group name is $STG_GRP_NAME\n";     
                        print "ENIQ OSS Service Interfaces are $OSSSERVICEINTF\n";
                        print "ENIQ Storage Interfaces $STORAGEINTF\n";
                                
                        print "ENIQ First OSS Service Interface $FIRSTOSSSERVICEINTF\n";
                        print "ENIQ Second OSS Service Interface $SECONDOSSSERVICEINTF\n";
                        print "ENIQ First Storage Interface $FIRSTSTORAGEINTF\n";
                        print "ENIQ Second Storage Interface $SECONDSTORAGEINTF\n";

                        print "ENIQ Network Type is $NETWORKTYPE\n"; 
                        print "ENIQ MainDB Core $MAINDBCORE\n";
                        print "ENIQ TmpDB Core $TMPDBCORE\n";
                        print "ENIQ MainDB GRAN $MAINDBGRAN\n";
                        print "ENIQ TmpDB GRAN $TMPDBGRAN\n";
                        print "ENIQ MainDB WRAN $MAINDBWRAN\n"; 
                        print "ENIQ TmpDB ERAN $TMPDBWRAN\n";
                        print "Number of Core Nodes $NOCORENODES\n";
                        print "Number of GRAN Nodes $NOGRANNODES\n";
                        print "Number of WRAN Nodes $NOWRANNODES\n";
                        print "Mirrored Disks $MIRRORDISKS\n";
                        
                        if("$RDISK" ne "NONE" ){
                                print "Root Disk $RDISK\n";
                                $RDISK = "rdisk=${RDISK}"; 
                        }
                        if("$MDISK" ne "NONE"){
                                print "Mirror Disk $MDISK\n";
                                $MDISK = "mdisk=${MDISK}"; 
                        }
                        print "Operating System : $operatingSystem\n";
                        print "SAN Type (clariion, vnx) : vnx\n";
                        print "Connected CEP Blade & CEP Coordinator : $CONNECTED_CEP_BLADE\n";
                        print "CEP Blade connected to Coordinator : $CEP_BLADE\n";
                        print "Coordinator connected to CEP Blade : $CEP_COORD\n";
                        if ($NO_OF_SANS==2) {
                                
                        print "Clariion 2 Host Name : $CLAR_HOST_2\n";
                        print "SP A 2: $ip_SPA_2\n";
                        print "SP B 2: $ip_SPB_2\n";
                        
                        }       
				    print "##############################################\n\n";
        
					$local_ship = $SHIPMENT;
					$local_ship =~ s/^_//g;
					$local_ship =~ s/_.*//g;
					chomp($local_ship);
					$statsRackQuestions = "/view/eniq_dmstats_ci/vobs/ossrc/del-mgt/bin/rack_ii_questionnaire.txt";
					print "Questions file : $statsRackQuestions\n";
                }
        }
}

sub CONFIGUREWEB{
#       if ("$SHIPMENT" eq "3.2.3_ES")
        if("$SHIPMENT" =~ m/_ES/){
                $BUILD_TYPE1 = "ENIQ_EVENTS";
                $stat = "es";
                $jumparea = "/JUMP/$BUILD_TYPE1/ENIQ_ES";
                print "LTEES\n\n\n\n\n\n ";
        }elsif("$BUILD_TYPE" eq "ENIQ_E"){
                $BUILD_TYPE1 = "ENIQ_EVENTS";
                $stat = "events";
                $jumparea = "/JUMP/$BUILD_TYPE1/$BUILD_TYPE1";
                print "EVENTS\n\n\n\n\n\n";
        }elsif ("$BUILD_TYPE" eq "ENIQ_S"){
                $BUILD_TYPE1 = "ENIQ_STATS";
                $stat = "stats";
                $jumparea = "/JUMP/$BUILD_TYPE1/$BUILD_TYPE1";
        }
        

        if(" $llsv_no" == "3"){
                $sw_location = "Features_17B_${SHIPMENT}";
        }else{
                $sw_location = "${SHIPMENT}.LLSV${llsv_no}";
        }
        
        if(! -d "${confignfs}/${jumparea}/${sw_location}"){
                #print "Can't find  ${confignfs}/${jumparea}/${sw_location}\n"; 
                if(" $llsv_no" == "3"){
                        $sw_location = ${SHIPMENT};
                }else{
                        $sw_location = "${SHIPMENT}.lsv${llsv_no}";
                }
                #$jumparea = "/export/jumpstart/${RELEASE}";
                print "The jump area is now $jumparea\n"; 
        }
        print "sw_location : $sw_location ";
        #####################################
        #
        #EJOHMCI When the ENIQ Platform of Stats/Events Merged in shipment 12.1 2.1.4/12.1.4 the grub parameter
        #eniq_install changed to config from that point on.
        #The Next conditional statement requires that the ENIQ Q&A txt file contains either config/install_eniq
        #which the below parses and adds to the install parameters, this allows this not to be hardcoded, if
        #the Q&A file does not contain a config/install_eniq then config is used by events as default and eniq_install
        #for stats.
        #
        #####################################
        if($BUILD_TYPE eq "ENIQ_E"){
                print "EVENTS1";
                open(CONFIG,$iniratorQuestionsAndAnswers);
                my @eniqtest=<CONFIG>;
                close(CONFIG);

                foreach (my $i=0; $i<@eniqtest; $i++){
                        my $testresult = $eniqtest[$i];
                        if($testresult =~ "eniqdmconfig"){
                                $expectedresult = $testresult;
                                $expectedresult =~ s/#[a-z]*=//;
                                chomp($expectedresult);
                        }elsif(!$expectedresult){
                                #$expectedresult = "config=events inst_type=eniq label_disks";
                #if($ship eq '3.2.4_ES'){
                                if ("$SHIPMENT" =~ m/_ES/){
                                        $expectedresult = "config=es inst_type=eniq";
                                        $stat = "es";
                                        $mws_stat = "es";
                                }elsif ($BUILD_TYPE eq "ENIQ_E"){
                                        print "EVENTS2";
                                        $expectedresult = "config=events inst_type=eniq";
                                        $stat = "events";
                                        $mws_stat = "events";
                                }
                        }
                }
                # $stat = "es";
                # $mws_stat = "es";
                $grub_stat = $stat;
        }
        elsif ( $BUILD_TYPE eq "ENIQ_S" && $ARCH eq "i86pc"){
                if ( "$mach" =~ m/ieatrcx/ ){
                        open(CONFIG,$statsRackQuestions);
                }
                elsif( "$mach" =~ m/atrcxb/ ){
                        open(CONFIG,$statsBladeQuestions);
                }
                my @eniqtest=<CONFIG>;
                close(CONFIG);

                foreach (my $i=0; $i<@eniqtest; $i++){
                        my $testresult = $eniqtest[$i];
                        if( $testresult =~ "eniqdmconfig"){
                                $expectedresult = $testresult;
                                $expectedresult =~ s/#[a-z]*=//;
                                chomp($expectedresult);
                        }elsif(!$expectedresult){
                                $expectedresult = "eniq_install=stats inst_type=eniq label_disks";
                                #$expectedresult = "config=stats inst_type=eniq";
                                #if ($BUILD_TYPE eq "ENIQ_S")
                                #{
                                #       print "STATS1";
                                #       $expectedresult = "config=stats inst_type=eniq";
                                #       $stat = "stats";
                                #       $mws_stat = "stats";
                                #}      
                        }
                }
                $stat = "stats";
                $mws_stat = "stats";
                $grub_stat = $stat;
        }
        elsif($BUILD_TYPE eq "ENIQ_S" && $ARCH ne "i86pc"){
                open(CONFIG,$statsRackQuestions);
                my @eniqtest=<CONFIG>;
                close(CONFIG);

                foreach (my $i=0; $i<@eniqtest; $i++){
                        my $testresult = $eniqtest[$i];
                        if ( $testresult =~ "eniqdmconfig"){
                                $expectedresult = $testresult;
                                $expectedresult =~ s/#[a-z]*=//;
                                chomp($expectedresult);
                        }
                        elsif( ! $expectedresult ){
                                $expectedresult = "eniq_install=oss inst_type=eniq label_disks";
                        }
                }
                $stat = "oss";
                $mws_stat = "stats";
                if ( $expectedresult eq "config"){
                        $grub_stat = "stats";
                }else{
                        $grub_stat = $stat;
                }
        }
        
        if ( $jumparea !~ /\/JUMP\/jumpstart\// ){
                ####PRINT INFORMATION TO BE PASSED TO DHCP WEBPAGE: ####
                print "Information to be passed to DHCP Configuration Web Page\n\n";
                print "ROOT USER: $root_user\n";
                print "ROOT USER PASS: $PASS\n";
                print "ILO IP_ADDR : $ilo_ip_addr\n";
                print "USERNAME : $username\n";
                print "MACADDR : $macaddr\n";
                print "MACHINE : $mach\n";
                print "ENIQ_JUMP_SVR : $eniq_jump_svr\n";
                print "ARCH : i86pc\n";
                print "JUMP AREA : $jumparea\n";
                print "SW_LOCATION : $sw_location\n\n";
                print "##############################################\n\n";

                #####################################
                # Configure Server in DHCP Webpage
                #####################################
                $ship =~ s/lsv/LLSV/;

                 #if ( $SHIPMENT eq "3.2.4_ES" )
                if ("$SHIPMENT" =~ m/_ES/){
                        if ( ! -d "${confignfs}/$mws/$BUILD_TYPE1/ENIQ_ES/${ship}" )
                        {
                                        print "Error No MWS build found this shipment\n";
                                        print "Unable to find:\n";
                                        print "${confignfs}/$mws/$BUILD_TYPE1/ENIQ_ES/${ship}\n\n";
                                        print "Exiting!!!!\n";
                                        exit 1;
                        }
                }
                elsif ( $llsv_no eq "3" ){
                        if( ! -d "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}" ){
                                print "Error No MWS build found this shipment\n";
                                print "Unable to find:\n";
                                print "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}\n\n";
                                print "Exiting!!!!\n";
                                exit 1;
                        }
                }
                elsif ( $llsv_no ne "3"){
                        if ( ! -d "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}.LLSV${llsv_no}" ){
                                print "Error No MWS build found this shipment\n";
                                print "Unable to find:\n";
                                print "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}.LLSV${llsv_no}\n\n";
                                print "Exiting!!!!\n";
                                exit 1;
                        }
                }
                
                if ( $llsv_no eq "3"  && $operatingSystem eq "linux" ){                 
                        open LINLOC, "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}/lin_i86pc.loc" or die "Couldn't open file lin_i86pc.loc"; 
                        $linloc.=<LINLOC>; 
                        close (LINLOC);
                        chomp $linloc;
                        print "LINLOC FILE $linloc\n";

                        open LINOMLOC, "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}/om_lin.loc" or die "Couldn't open file om_lin.loc"; 
                        $linomloc.=<LINOMLOC>; 
                        close (LINOMLOC);
                        chomp $linomloc;
                        print "LINOMLOC FILE $linomloc\n";
                }
                elsif ( $llsv_no ne "3" && $operatingSystem eq "linux" ){
                        open LINLOC, "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}.LLSV${llsv_no}/lin_i86pc.loc" or die "Couldn't open file lin_i86pc.loc";
                        $linloc.=<LINLOC>;
                        close (LINLOC);
                        chomp $linloc;
                        $linloc = dirname($linloc);
                        print "LINLOC FILE $linloc\n";

                        open LINOMLOC, "${confignfs}/$mws/$BUILD_TYPE1/$BUILD_TYPE1/${ship}.LLSV${llsv_no}/om_lin.loc" or die "Couldn't open file om_lin.loc"; 
                        $linomloc.=<LINOMLOC>; 
                        close (LINOMLOC);
                        chomp $linomloc;
                        print "LINOMLOC FILE $linomloc\n";
                }
                print "Conf Directory ${confignfs}/${configdir}/${config}\n";
                open(CONF,">${confignfs}/${configdir}/${config}") or die "Can't write to file '${confignfs}/${configdir}/${config}' [$!]\n";
                
                print CONF "CLIENT_HOSTNAME\@$host\n";
                print CONF "CLIENT_IP_ADDR\@$ip_addr\n";
                print CONF "CLIENT_NETMASK\@255.255.255.0\n";
                print CONF "CLIENT_MAC_ADDR\@$macaddr\n";
                print CONF "CLIENT_ARCH\@i86pc\n";
                print CONF "CLIENT_DISP_TYPE\@NON-VGA\n";
                print CONF "LDAP_SERVER_HOSTNAME\@none\n";
                print CONF "LDAP_DOMAIN_NAME\@none\n";
                print CONF "LDAP_ROOTCERT\@/JUMP/PKS_CERT/2/rootca.cer\n";
                if("$operatingSystem" eq "linux"){
                        print CONF "CLIENT_TZ\@Eire\n";
                        print CONF "CLIENT_KICK_LOC\@/JUMP/LIN_MEDIA/1\n";
                        print CONF "CLIENT_OM_LOC\@$linomloc\n";
                        print CONF "CLIENT_APPL_TYPE\@eniq_events\n";
                }
                print CONF "IPV6_PARAMETER\@NO\n";
                print CONF "CLIENT_IP_ADDR_V6\@\n";
                print CONF "ROUTER_IP_ADDR_V6\@\n";

                if($operatingSystem eq "linux"){
                        #print CONF "CLIENT_APPL_MEDIA_LOC\@none\n";
                        print CONF "CLIENT_APPL_MEDIA_LOC\@/JUMP/$BUILD_TYPE1/$BUILD_TYPE1/${ship}\n";
                }
                
                if( "$ARCH" eq "i86pc" ){
                        if("$operatingSystem" eq "linux" && "$SERVERTYPE" eq "mediation_cep"){
                                print CONF "CLIENT_INSTALL_PARAMS\@inst_type=eniq config=cep \n";
                        }
                }else{
                        if("$operatingSystem" eq "linux" && "$SERVERTYPE" eq "mediation_cep"){
                                print CONF "CLIENT_INSTALL_PARAMS\@- install inst_type=eniq config=cep \n";
                        }               
                }
                close(CONF);

                print "\n#####################################\n";
                print "About to Run configuration for tftpboot command...\n";
                print "#######################################\n";
                #####################################
                # Calling Expect Module
                #####################################
                my $timeout = 10;
                my $undef = undef;
                $exp = Expect->spawn("/usr/bin/ssh $root_user\@$eniq_jump_svr" ) or die "Unable to spawn ssh  to $eniq_jump_svr.\n";

                ########################################################
                ## NOTE : This is temporary for debugging purpose
                #$exp->log_file ("$LOGDIR/$LOGFILE");
                ########################################################

                if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                        $exp->send('yes' . "\n");
                }

                $exp->expect($timeout,
                        [ 'ssword: $' => sub {
                                                $exp->send("$dm_root_storage\r");
                                                exp_continue; }
                        ],

                        '-re', qr'[^.*->#] $' => sub {
                                         exp_continue; }

                );
                if ($operatingSystem eq "linux"){
                        my $mancount = 1;
                        while ($mancount <= 3) {
                                #print "YES\n";
                                $exp->send("cd /JUMP/LIN_MEDIA/1/kickstart/${mach} \r");
                                $exp->expect(15);
                                $exp->send("/usr/bin/cp -rf ${mach}_ks_cfg.txt /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/Clients\r"); 
                                $exp->expect(15);
                                $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a remove -c ${mach} -N\r");
                                $exp->expect(45);
                                $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a add -f /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/Clients/${mach}_ks_cfg.txt -N\r");
                                $exp->expect(45);
                                # captures the output of the last send exp command
                                my $manageoutput = $exp->before();
                                #my $manageoutput = "with client data";
                                if ( $manageoutput =~ /with client data/){
                                        print "\n###############################################\n";
                                        print "Breaking from While Manage_dhcp was successful\n";
                                        print "Successful on try $mancount of 3\n";
                                        print "###############################################\n";
                                        $exp->expect(15);       
                                        #$$exp->send("\rm -rf /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/Clients/* \r");
                                        #$exp->expect(15);
                                        last;
                                }else{
                                        $mancount ++;
                                        if ($mancount == 4){
                                                print "\n\n###############################################\n";
                                                print "manage_dhcp was unsuccessful\n";
                                                print "Tried 3 times to configure\n";
                                                print "Exiting!!! Please investigate....\n";
                                                print "###############################################\n\n\n";
                                                exit 1;
                                        }else{
                                                print "###############################################\n";
                                                print "manage_dhcp was unsuccessful\n";
                                                print "Executing try $mancount of 3\n";
                                        }
                                        # Generate a Random number between 20s and 300s
                                        my $manrange = 280;
                                        my $manminimum = 20;
                                        my $manrandom = int(rand($manrange)) + $manminimum;
                                        print "Sleeping for $manrandom seconds\n";
                                        print "###############################################\n";
                                        $exp->expect($manrandom);
                                }
                        }
                }
                $exp->expect($undef, '#');
                $exp->expect(15);
                $exp->soft_close();
        }
}
      
sub MWS_CONNECTION{
                print "\n#####################################\n";
                print "About to  connect MWS server to connect the ILO...\n";
                print "#######################################\n";
                #####################################
                # Calling Expect Module
                #####################################
                my $timeout = 10;
                my $undef = undef;
                $exp = Expect->spawn("/usr/bin/ssh $root_user\@$eniq_jump_svr" ) or die "Unable to spawn ssh  to $eniq_jump_svr.\n";

                ########################################################
                ## NOTE : This is temporary for debugging purpose
                #$exp->log_file ("$LOGDIR/$LOGFILE");
                ########################################################

                if ($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')) {
                        $exp->send('yes' . "\n");
                }

                $exp->expect($timeout,
                        [ 'ssword: $' => sub {
                                                $exp->send("$dm_root_storage\r");
                                                exp_continue; }
                        ],

                        '-re', qr'[^.*->#] $' => sub {
                                         exp_continue; }

                );

}


sub ILOMCON{
        print "\n###############################\n";
        print "About to Call Expect Module... Connect to ILO\n";
        print "###############################\n";      
        
        #print "/usr/bin/ssh $root_user\@$ilo_ip_addr\n";
        #$exp = Expect->spawn("/usr/bin/ssh $root_user\@$ilo_ip_addr" ) or die "Unable to spawn ssh  to $ilo_ip_addr.\n";

        $exp->send("/usr/bin/ssh $root_user\@$ilo_ip_addr \r");

        if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')){
                $exp->send('yes' . "\n");
        }

        $exp->expect(20,
                [ '[Pp]assword: $' => sub {
                                        $exp->send("$PASS\r");
                                        exp_continue; }
                ],

                '-re', qr'[^.*->] $' => sub { exp_continue; }
        );
        #$exp->expect(20, ['->', sub {$exp->send("\r");}]) or die "ssh failed to connect: $!\n";
        $exp->expect(20, '>') or die "ssh failed to connect:\n";
}

sub ILOMCON_RACKMOUNT{

		#One time boot 
		$exp->expect($timeout, ['hpiLO->', sub {$exp = shift; $exp->send("onetimeboot netdev1\r");}]);

		## Wait 300 seconds
		$exp->expect(300);

		$exp->expect($timeout, ['hpiLO->', sub {$exp = shift; $exp->send("stop /system1/oemhp_vsp1\r");}]);
		## Wait 200 seconds
		$exp->expect(200);

        #Reset System ( form of cold boot)
        $exp->expect($timeout, ['hpiLO->', sub {$exp = shift; $exp->send("reset /system1\r");}]);

        ### Wait 300 seconds
        $exp->expect(300);

        ### Start VSP
        $exp->expect($undef, ['hpiLO->', sub {$exp = shift; $exp->send("vsp\r");}]);
        #$exp->expect(20, ['hpiLO-> Virtual Serial Port active', sub {$exp->send("\r");}]) or die "vsp failed to start: $!\n";
        $exp->expect(20, ['Virtual Serial Port [Aa]ctive', sub {$exp->send("\r");}]) or die "vsp failed to start: $!\n";
        $exp->expect(10);

}

sub success_cleanup($){
        my ($sms_message)=$_[0];
        print "Running cleanup before exiting\n";
        if($sms_signum){
                &send_sms ($RELEASE, $SHIPMENT, $sms_message, $sms_signum);
        }else{
                print "No signum entered.\nExiting\n";
        }
        exit 0;
}

sub send_sms($$$$){
        my ($release)=$_[0];
        my ($shipment)=$_[1];
        my ($MESSAGE)=$_[2];
        my ($SIGNUMID)=$_[3];
        my $TITLE="$release $shipment";

        # put the signums in an array
        my @arr = split(/\,/,$SIGNUMID);

        #loop over the array
        foreach (@arr) {
                #  print "$_\n";
                #check if user exists
                my $EXISTS=`ldapsearch -h ecd.ericsson.se -b o=ericsson -D uid=VOBADM100,ou=Users,ou=Internal,o=ericsson -w "Ericsson123" uid=$_`;
                if ( $EXISTS ){       # tests to see if the user exists
                        my $MOBILE=`ldapsearch -h ecd.ericsson.se -b o=ericsson -D uid=VOBADM100,ou=Users,ou=Internal,o=ericsson -w "Ericsson123" uid=$_ | grep mobile | awk -F":|=" '{print \$2}'`;
                        $MOBILE =~ s/^\s+//; #remove leading spaces
                        $MOBILE =~ s/\s+$//; #remove trailing spaces

                        #if there is a mobile number for the person, send a txt
                        if ( $MOBILE ){
                                #Convert the mobile number to SMS URL
                                $MOBILE .= "\@sms.ericsson.com";
                                `echo "$MESSAGE" | mailx -s "$TITLE" $MOBILE`;
                                print "SMS sent to $_ at $MOBILE. Message is: $MESSAGE\n";
                        }else{
                                my $MAIL=`ldapsearch -h ecd.ericsson.se -b o=ericsson -D uid=VOBADM100,ou=Users,ou=Internal,o=ericsson -w "Ericsson123" uid=$_ | grep mail | awk -F":|=" '{print \$2}'`;
                                print "No mobile number setup for user: $_. sending email instead to: $MAIL\n";
                                my $MAILMESSAGE = "Please add your mobile number to your outlook details so you can receive automatic update texts related to your install/ug.";
                                `echo "$MAILMESSAGE" | mailx -s "No mobile number setup" $MAIL`;
                                `echo "$MESSAGE" | mailx -s "$TITLE" $MAIL`;
                        }
                }else{
                        print "$_ does not exist\n";
                }
        }
}

############# STATS RACK ###################

sub LOAD_EXP_STATS_RACK{
        open(EniqStatsOnRack, $statsRackQuestions) || die "Can not open file $statsRackQuestions: $!\n";
#       print "\nInirator questions and Answers will be read from $statsRackQuestions\n\n";
        $count = 0;
        my $questionAndAnswer;

        while(<EniqStatsOnRack>){
                chomp;
                push @lines, split ('\n', $_);
        }
    
    foreach (@lines){
                if (!/(^#|^$)/){
                        s/=/="/;
                        eval '$' . $_ . '";';
                        ($question, $answer) =  split (/ && /, $questionAndAnswer);
                        $exp->expect($def, "$question") or die "Answer for $question not found: $!\n";
                        $exp->expect(5);
                        $exp->send("$answer\r");
                        $count++;
                }
        }
        
        close(EniqStatsOnRack);

        $exp->log_file("$TMP_FILE", "w");       
        $exp->expect($def, "Available ENIQ features");
        $exp->expect(10);

        $exp->log_file(undef);
                
        my $entryfull = `cat ${TMP_FILE} | egrep "^\[[0-9][0-9]" | tail -1 | awk -F "]" '{print \$1}'`;
        my ($entry, $muck) = split (/ /, $entryfull);
        $entry =~ s/\[//;
        $entry =~ s/\]//;
        #print "***$entry***";
		
        $exp->send("1-${entry}\r");
        
        if ($exp->expect(10, 'Are the values above correct (Yes/No)')){
                $exp->expect(3);
                $exp->send("Yes\r");
        }
        elsif ($exp->expect(10, 'Are the values above correct (Yy/Nn)')){
                $exp->expect(3);
                $exp->send("y\r");
        }
        
        $exp->expect(64800, "Entering ERIC Bootstrap Stage cleanup") or die "failed to install features or features took longer than timeout, please investigate\n";
        $exp->send("\r");
        $exp->expect(1200);
        $exp->soft_close();
}

sub TIMECALC{
        print "\nStartTime : \t$sh:$sm:$ss\n";  
        my ($es,$em,$eh)=localtime;
        print "\nEndTime : \t$eh:$em:$es\n";
        if($sh <=12 && $eh <= 12 )
{
        $sh=$sh+24;
        $eh =$eh + 24;
        $ch=$eh - $sh;
#       print "Upgrade Execution time in hour :$ch hour\n";
}
        if ( $eh <= 12 ){
        $eh =$eh + 24;
        $ch=$eh - $sh;
#       print "II Execution time in hour :$ch hour\n";
}
        else
        {
        $ch=$eh -$sh;
#       print "II Execution time in hour :$ch hour\n";
        }
        $ch =$ch -1;
        $sm = 59 - $sm;
        $cm = $sm + $em;

        $ss = 61 - $ss;
        $cs = $ss + $es;
        if ( $cs >=61 )
        {
        $cm = $cm+1;
        }
        if ( $cm >=60)
        {
        $ch = $ch + 1;
        }       
        print "Total Run Time is $ch:$cm:$cs\n";
}

###### Main Script #####

{
        PARAMETERS();           ### Gets the inputted parameter a set to variables
        ENIQRACKDETAILS();     ### Gets the server details from the server_details.txt file
        #CONFIGUREWEB();         ### Run the configure web page and the edits the Grub
        MWS_CONNECTION();                               
        # Rack Server Events and Stats
        if("$ARCH" eq "i86pc" && "$operatingSystem" eq "linux"){
                #REORDER_BOOT_DISKS_BLADE();    
                ILOMCON();                      ### Connect server to ilom
                if(("$BUILD_TYPE" eq "ENIQ_S") && (("$mach" eq "ieatrcx6527") || ("$mach" eq "ieatrcx6575") || ("$mach" eq "atrcx3371"))){
                        ILOMCON_RACKMOUNT();       ### This section can be used for all HP RACK server Stats
                        LOAD_EXP_STATS_RACK();
                        TIMECALC();
                }
				else
				{
					print "Invalid Server or Release!!";
					error()
				}
        }
        success_cleanup("Your II was successful on $MACHINE");
        exit 0;
}