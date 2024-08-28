#!/vobs/cello/cade_A_tools_perl/SunOS/sparc/bin/perl -w
#-----------------------------------------------------------
# COPYRIGHT Ericsson Radio Systems  AB 2011
#
# The copyright to the computer program(s) herein is the 
# property of ERICSSON RADIO SYSTEMS AB, Sweden. The 
# programs may be used and/or copied only with the written 
# permission from ERICSSON RADIO SYSTEMS AB or in accordance 
# with the terms and conditions stipulated in the agreement
# contract under which the program(s)have been supplied.
#-----------------------------------------------------------
#-----------------------------------------------------------
#
#   PRODUCT      : NM I&V
#   CRA NUMBER
#   CRA NUMBER
#   PRODUCT REV  :
#   Document REV :
#
#   REV          : B
#
#
#--------------------------------------------------------------
#   
# 
#use strict;
use Getopt::Long;
use Expect;

#use lib "/vobs/ossrc/del-mgt/bin";
#use EniqEvents;

# ********************************
#
# CONFIGURATION SECTION
#
# ********************************
my $serverDetails = "/vobs/ossrc/del-mgt/bin/eniq_Linux_server_details.txt";
my $TMP_FILE;
my $TMP_FILE2;
my $TMP_FILE_2;
my $TMP_FILE_3;
my $Rel_ONM;

#my $runtime;
#my $run_time=getDateTime();
my ($ss,$sm,$sh)=localtime;
my $ch;
my $cm;
my $cs;
my ($help, $rel, $ship, $llsv_no, $mach, $arch, $vendor, $type, $build, $features, $SMS_SIGNUM);
my $RELEASE;
my $BASE_SHIPMENT=0;
my $SHIPMENT;
my $LLSV_NO;
my $MACHINE;
my $BUILD_TYPE;

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
my $cep_ip_addr;
my $CEP_STG_IP;
my $storagepool;
my $ip_NAS_MS;
my $ip_NAS_SPT;
my $NO_OF_SANS;
my $ENIQ_LIC;
my $SAN_UN;
my $SAN_PWD;
my $STG_IP;
my $STG_NET;
my $list ="";
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
my $STR_GRP_NAM;
#my $dateAndTime;
my $dateAndTime = getDateTime();
#my $SMS_Date;
my $Mig_IP_ADD;
my $Mig_Dir;
my $OM_path;
my $jumparea1;
my $featurearea;

##############################
# Internal Global Variables
##############################

my $root_user = 'root';
my $PASS = "shroot12";
my $eniq_jump_svr = "10.45.192.153";
my $dm_root_storage = "shroot12";
chomp $eniq_jump_svr;
my $command = "uname -a | cut -d ' ' -f3";
my $jumparea;
my $om_sw_loc;
my $upg_sw_loc;
my $upgradeDir = "";
my $tmp_om_sw_loc;
my $tmp_os_sw_loc;
my $os_sw_loc;
my ($entry, $muck);
my $deployment;
my $upgrade_type="standard";
my $localcount;
my $bootenviron;
my $sms_signum;
my $SMS_SIGNUM;
my $lun;

my $timeout = 20;
my $timeout2 = 9600;
my $timeout3 = 26000;
my $timeout4 = 600;
my $timeout5 = 120;
my $undef;
my $def = 10800;
my $exp;
my $res;
my $logfile;
my $DEPLOY1;
my $DIR_BUILDLOGS;
my $logindep;

my @fields;
my @UGServerArray;

my $coOrdinator;
my $engine;
my $readerOne;
my $readerTwo;
my $readerThree;
my $presentation;
my $mediation;
my $mediationTwo;
my $cepMediation;
my $managedeployserviceDo;
my $managedeployserviceCommand;
my $ManageDeploymentServices;
my $ManageSnapshots;
my $CheckForZFS;
my $ManageUnpackCoreSW;
my $ManageUnpackCoreSWUG;
my $checkCommand;
my $PrepEniqSnapshots;
my $mqWorkflow;
my $coreInstall;
my $result;
my $UnPackcoreInstall;
my $IPMP_Group_Intf;
my $Storge_VLAN_INT;

my $feature_upgrade_start_time;
my $feature_upgrade_finish_time;

my $replaceSnap1;
my $replaceSnap2;

my $cep_server_ip;
my $cep_server_storage_ip;

my $logging;
my $deployment1;
my $Rel_Alphabet;
my $Rel;
my $Num;
my $Feature_Path;
my $Release;
my $Rel_Num;
my $output;

my @upgrade_stages;
        
my @sol11migration_stages=("5.5.1 Run Pre-migration","5.5.4 Solaris OS Installation","5.5.4 Migration","5.6.5 Restart ENIQ Statistics Services");

my @Zpool_coOrdinator=("eniq_sp_1","stats_coordinator_pool");
my @Zpool_engine=("eniq_sp_1","stats_engine_pool");
my @Zpool_reader=("eniq_sp_1","stats_iqr_pool");

my $curr_stage;
my $stage_file="stage_file.txt";
my $curr_stage_file="/curr_stage.txt";
my $SolPatchExists="patches exists";
my $solaris_lu_service_status="notonline";
my %solaris_lu_progress;

# ********************************
#
# FUNCTIONS
#
# ********************************
sub error {
        print "ERROR:";
        exit;
}
sub Init_sequence{
                 #if( "$output" == "5.11"){
                 if( "$output" eq "Linux"){
                 @upgrade_stages=("Chapter 2: Prerequisites",
                        "5.4.6 Mandatory Pre-Upgrade IQ check",
                        "5.4.8 UNPACK CORE SOFTWARE",
                        "5.4.9 Upgrade Pre-Execution Check",
                        "5.7.1 For Full Upgrade",
                        "chapter6: PostUpgradeViews_Accessibility");
                }

        else{
                @upgrade_stages=("Chapter 2: Prerequisites",
                        "5.4.6 Mandatory Pre-Upgrade IQ check",
                        "5.4.8 Unpack Core Software",
                        "5.5.1 Run Pre-migration",
                        "5.5.4 Solaris OS Installation and Migration",
                        #"5.6.5 Restart ENIQ Statistics Services",
                        "5.7.1 For Full Upgrade",
                        "5.11 Post Upgrade Steps");     
                }
}
sub getDateTime{
        my @local_time = localtime;
        my $year_str = $local_time[5] - 100 + 2000;
        my $mon_str = $local_time[4] + 1;
        my $time_str="$year_str$mon_str$local_time[3]-"
                ."$local_time[2]:$local_time[1]:$local_time[0]";
        return $time_str;
}

sub getDateTimeForLiveUpgrade{
        my $min_offset=shift;
        chomp($min_offset);
        my @local_time = localtime(time() + $min_offset*60);
        my $mon_str = $local_time[4] + 1;
        my $day_str = $local_time[3];
        my $hour_str = $local_time[2];
        my $min_str = $local_time[1];
        length($min_str) < 2 ? $min_str = "0".$min_str : $min_str = $min_str;
        length($hour_str) < 2 ? $hour_str = "0".$hour_str : $hour_str = $hour_str;
        length($day_str) < 2 ? $day_str = "0".$day_str : $day_str = $day_str;
        length($mon_str) < 2 ? $mon_str = "0".$mon_str : $mon_str = $mon_str;
        my $time_str="$mon_str$day_str$hour_str$min_str";
                
        return $time_str;
}

sub getDateTimeForFeatureUpgrade{
        my $min_offset=shift;
        chomp($min_offset);
        my @local_time = localtime(time() + $min_offset*60);
        my $year_str = $local_time[5] + 1900;
        my $mon_str = $local_time[4] + 1;
        my $day_str = $local_time[3];
        my $hour_str = $local_time[2];
        my $min_str = $local_time[1];
        my $sec_str = $local_time[0];
        my $time_str=sprintf("%4d-%02d-%02d %02d:%02d:%02d",$year_str,$mon_str,$day_str,$hour_str,$min_str,$sec_str);
                
        return $time_str;
}
        
sub bannerPrint{
        my $statement = $_[0];

        print "\n\n\n##########################################################\n";
        print "##########################################################\n";
        print "##########################################################\n";
        print "\n$statement\n\n";
        print "##########################################################\n";
        print "##########################################################\n";
        print "##########################################################\n\n\n";

        print "\n\n";
}


sub usage{
        print "\n";
        print "Unknown option: @_\n" if ( @_ );
        print "Usage: program Maditory: [-r RELEASE] [-s SHIPMENT] [-n LLSV_NO]  \n";
        print "       program Optional: [-help|-?] [-m Machine][--si SMS_SIGNUM] \n";
        print "\n";
        exit;
}

sub PARAMETERS {
        usage() if ( @ARGV < 1 or ! GetOptions('help|?' => \$help, 'rel|r=s' => \$rel, 'ship|s=s' => \$ship, 'llsv_no|n=s' => \$llsv_no, 'mach|m=s' =>  \$mach,'lun|l=s' => \$lun, 'sms_signum|si=s' => \$sms_signum) or defined $help );



        print "\nStartTime : \t$sh:$sm:$ss\n";  
        print "Arguments inputted:\n\n";
        print "RELEASE: $rel\n";
        print "SHIPMENT: $ship\n";
        print "LLSV_NO: $llsv_no\n";
        $MACHINE = $mach;
        my $server_number= $mach;
        print "SMS Signums: $sms_signum\n";
        #$SMS_SIGNUM = $sms_signum;
		
        $Rel_Num = (split /ENIQ_S/, "$rel")[1];
	$Rel_ONM = (split /_/, "$ship")[0];
		
        $Rel =( split /\./, "$Rel_Num")[0];
        $Num =( split /\./, "$Rel_Num")[1];

           if ($Num == "0")
             {
                $Feature_Path= "Features_"."$Rel"."A";                             
              }
           if ($Num == "2")
              {
                 $Feature_Path= "Features_"."$Rel"."B";  
              }
           if ($Num == "4")
              {
                 $Feature_Path= "Features_"."$Rel"."C";           
              }
        
        $RELEASE = $rel;
        $SHIPMENT = $ship;
        $LLSV_NO = $llsv_no;

        $TMP_FILE = "/tmp/eniq_log_${RELEASE}_${SHIPMENT}_llsv${LLSV_NO}_${mach}_MB_MG.txt";
        $TMP_FILE2 = "/tmp/new_eniq_log_${RELEASE}_${SHIPMENT}_llsv${LLSV_NO}_${mach}_MB_MG_ADD.txt";

        $TMP_FILE_3 = "/tmp/eniq_log_${RELEASE}_${SHIPMENT}_llsv${LLSV_NO}_${mach}_MB_MG_ADD2.txt";
        if( -f $TMP_FILE){
                unlink($TMP_FILE);
        }
		
        $DIR_BUILDLOGS="/proj/eniqdmt/logs/ENIQ/${RELEASE}/${SHIPMENT}/LLSV${LLSV_NO}"
}

sub ENIQBLADEDETAILS{
        open(SERVERDETAILS, $serverDetails) || die "Can not open file $serverDetails";
        my @eniqServerdedetails=<SERVERDETAILS>;
        close(SERVERDETAILS);

        foreach (@eniqServerdedetails){
                # read the fields in the current record into an array
                my @fields = split(';', $_);
                $hostname = $fields[0];
                my $bladecount = 0;
                if ( "$hostname" eq "$MACHINE" ){
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
                        $ENIQ_LIC = $fields[$bladecount++];
                        
						$ENIQ_LIC = "/net/159.107.177.74/eniq/eniq_build/license/${RELEASE}";
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
                        #$STG_TYPE = $fields[$bladecount++];
                        $STG_TYPE = $fields[$bladecount++];
                        if ($STG_TYPE == 1){
                                $STG_TYPE = "raw";
                        }elsif ($STG_TYPE == 2){
                                $STG_TYPE = "zfs";
                        }
                        $OSS_SERVER = $fields[$bladecount++];
                        $FQDN = $fields[$bladecount++];
                        $IQ_INST = $fields[$bladecount++];
                        $DWH_READER = $fields[$bladecount++];
                        $DEPLOY = $fields[$bladecount++];
                        $STG_NET_NO = $fields[$bladecount++];
                        $STR_GRP_NAM = $fields[$bladecount++];

                        print "\nStartTime : \t$sh:$sm:$ss\n";  
                        print "Information Currently stored on Server_details file\n\n";
                        print "HOSTNAME : $host\n";
                        print "MAC_ADDR : $macaddr\n";
                        print "ARCH : $ARCH\n";
                        print "IP_ADDR : $ip_addr\n";
                        print "ILOM IP ADD : $ilo_ip_addr\n";
                        print "Server type : $SERVERTYPE\n";
                        print "DEFROUTE : $def_route\n";
                        print "Clariion Host Name : $CLAR_HOST\n";
                        print "SP A : $ip_SPA\n";
                        print "SP B : $ip_SPB\n";
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
                        print "Storage Type: $STG_TYPE\n";
                        print "OSS Server IP: $OSS_SERVER\n";
                        print "FQDN: $FQDN\n";
                        print "IQ Instance: $IQ_INST\n";
                        print "DWH Reader: $DWH_READER\n";
                        print "ENIQ Deployment: $DEPLOY\n";
                        print "ENIQ Storage Network Number: $STG_NET_NO\n";
                        print "ENIQ Storage Group Name: $STR_GRP_NAM\n";        
                }
        }
}

sub MediaInfo {
        $jumparea = "/net/$eniq_jump_svr/JUMP/ENIQ_STATS/ENIQ_STATS/$SHIPMENT/eniq_base_sw";
		$featurearea = "/net/$eniq_jump_svr/JUMP/ENIQ_STATS/ENIQ_STATS/${Feature_Path}_${SHIPMENT}";
		print "\n###############################\n";
		print "PLATFORM JUMPAREA ==> $jumparea\n";
		print "FEATURE AREA ==> $featurearea\n";
		print "###############################\n";
		
		$om_sw_loc = "/net/$eniq_jump_svr/JUMP/OM_LINUX_MEDIA/OM_LINUX_0${Rel}_${Num}/${Rel_ONM}";
		$upgradeDir= "${rel}_${ship}_llsv${llsv_no}_upgrade_sw";
		print "\n###############################\n";
		print "OM ==> $om_sw_loc \n";
		print "UPGRADE DIRECTORY ==> $upgradeDir\n";
		print "###############################\n\n";
}

sub UpgradeServerConnection{
        my $serv_conn = $_[0];
        print "\n###############################\n";
        print "About to Connect to UG server $serv_conn...\n";
        print "###############################\n";

        #####################################
        # Calling Expect Module
        #####################################
        $timeout = 10;
        $exp = Expect->spawn("/usr/bin/ssh -l $root_user ${serv_conn}.athtem.eei.ericsson.se" ) or die "Unable to spawn ssh to ${serv_conn}.\n";
        if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')){
                $exp->send('yes' . "\n");
        }
        $exp->expect($timeout,[ 'assword: ' => sub {$exp->send("$PASS\r");exp_continue; }],'-re', qr'[^.*->#] $' => sub {exp_continue; });

        $exp->expect(2);
}

sub MultibladeMigration{

        #SRUUpgradeStandalone();



        #Mandatory upgrade check whether OS migration needed or not
        print "\n####################################################################################################################################\n";
        print "This is a mandatory procedure which needs to be executed before starting upgrade to check whether the OS migration is needed or not\n";
        print "\n####################################################################################################################################\n";

        $exp->send("uname\r");
		if($exp->expect($timeout, 'SunOS')){
			print"\n###############################\n";
			print "\nSolaris Server\n";
			print"\n###############################\n";
			print "Starting the Migration from Solaris to Linux\n";
		}
		else{
			print"\n###############################\n";
			print "\Linux Server\n";
			print"\n###############################\n";
			print "Migration is not required, So exiting..!!\n";
			#exit;
		}
          
        
		#5.5.4 Solaris OS Installation
		bannerPrint("CHAPTER 5.5.4: STARTING SOLARIS OS INSTALLATION ...");
		solaris_OS_installation_standalone();
		bannerPrint("CHAPTER 5.5.4: COMPLETED SOLARIS OS INSTALLATION ...");
		
		#5.5.4 Migration
		bannerPrint("CHAPTER 5.5.4: STARTING MIGRATION ...");
		Migration_standalone();
		bannerPrint("CHAPTER 5.5.4: COMPLETED MIGRATION ...");
		
		#5.6.5 Restart ENIQ Statistics Services
		bannerPrint("CHAPTER 5.6.5: STARTING RESTART ENIQ STATISTICS SERVICES ...");
		Post_migration_standalone();
		bannerPrint("CHAPTER 5.6.5: COMPLETED RESTART ENIQ STATISTICS SERVICES ...");
		
	   # 5.7.1 For Full Upgrade
	#	bannerPrint("CHAPTER 5.7.1: STARTING FOR FULL UPGRADE ...");
	#	ENIQStatisticsBaseSoftwareUpgrade();
	#	bannerPrint("CHAPTER 5.7.1: COMPLETED FOR FULL UPGRADE ...");
	#	UpgradeServerConnection($mach);

}

sub mig_prerequisites{
        print "\n\n--------------- Starting upgrade stage prerequisites ----------------\n\n";
        print "\n\n================================================================================";
        print "\n\n=================== CHECKING THE CURRENT VERSION OF THE SERVER ==================";
        print "\n\n================================================================================\n\n";
        ESServerVersion();
        print "\n\n================================================================================";
        print "\n\n======================= CHECKING THE SERVICE STATE =============================";
        print "\n\n================================================================================\n\n";
        EEserviceInMaintenanceState();
        print "\n\n================================================================================";
        print "\n\n======================= INSTALLING THE LICENCES ================================";
        print "\n\n================================================================================\n\n";
        installLicence();
        print "\n\n================================================================================";
        print "\n\n--------------- Upgrade stage Prerequisites Done ----------------\n\n";
}

sub ESServerVersion{
        #Find the current status of server
        print "\n###############################\n";
        print "Checking status of server\n";
         print "\n###############################\n";
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("cat /eniq/admin/version/eniq_status \r");}]);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("\r");}]);
        }


sub EEserviceInMaintenanceState{
    #Find the service that is in a maintenance state
    print "\n###############################\n";
    print "Checking status of services\n";
	print "If a service is in a maintenance state then it is necessary to clear the service\n";
	print "before attempting to restart or stop the service\n";
    print "###############################\n";
    $exp->log_file("$TMP_FILE", "w");
	$exp->expect($def, ['#', sub {$exp = shift; $exp->send("/usr/bin/svcs -a | egrep -i  'maintenance.*/eniq' \r");}]);
	$exp->expect($def, ['#', sub {$exp = shift; $exp->send("/usr/bin/svcs -a | egrep -i  'maintenance.*/ddc:' \r");}]);
    $exp->expect(5);
    $exp->log_file(undef);

	open (TMP_FILE, $TMP_FILE);
	my @service_status = <TMP_FILE>;
	close(TMP_FILE);
					
	@service_status=grep(/maintenance/,@service_status);
	foreach my $maintenance_state_on_server (@service_status){                      
	if(!grep(/usr/, $maintenance_state_on_server)){					
		$maintenance_state_on_server =~ s/\r//g;                #remove newlines from a string
		$maintenance_state_on_server =~ s/.*svc:\///;           #keep service name after svc:/
		$maintenance_state_on_server =~ s/^\s+//;               #remove leading spaces
		$maintenance_state_on_server =~ s/\s+$//;               #remove trailing spaces
				
		#check service that is in a maintenance state
		#The chomp() function will remove (usually) any newline character from the end of a string.
		chomp($maintenance_state_on_server);
				
		#print "\n\n Service in maintenance state >@service_status< \n\n";
		print "\n\n Service in maintenance state >$maintenance_state_on_server< \n\n";
				
		print "\n###############################\n";
		print "Attempting to clear service that is in a maintenance state\n";
		print "This may take a number of minutes to complete \n";
		print "###############################\n";
		$exp->expect($def, ['#', sub {$exp = shift; $exp->send("svcadm clear $maintenance_state_on_server\r");}]);
		$exp->expect($def, ['#', sub {$exp = shift; $exp->send("\r");}]);
		$exp->expect($def, ['#', sub {$exp = shift; $exp->send("\r");}]);
		$exp->expect(100);
		}
	}
} 

# If a service is in a maintenance state then it is necessary to clear the service
# before attempting to stop/restart the service again
sub installLicence{
        #######################
        #Install the license needed for upgrading
        #######################
        CheckAndEnableLIC();
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("su - dcuser\r");}]);
        $exp->expect(5);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("licmgr -install $ENIQ_LIC\r");}]);
        $exp->expect(5);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("licmgr -restart\r");}]);
        $exp->expect(40);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("exit\r");}]);
        $exp->expect(5);
}

sub CheckAndEnableLIC{
        $exp->log_file("$TMP_FILE", "w");
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("/usr/bin/svcs svc:/eniq/licmgr:default \r ");}]);
        $exp->expect(5);
        $exp->log_file(undef);

        open (TMP_FILE, $TMP_FILE);
        my @service_status = <TMP_FILE>;
        close(TMP_FILE);
        
        if(grep(/disabled/,@service_status)){
                $exp->expect($def, ['#', sub {$exp = shift; $exp->send("/usr/bin/svcadm enable svc:/eniq/licmgr:default\r ");}]);
                $exp->expect(60);
                $exp->expect($def, ['#', sub {$exp = shift; $exp->send("/usr/bin/svcs svc:/eniq/licmgr:default \r ");}]);
                $exp->expect(5);
        }
        unlink($TMP_FILE);
}

sub PreUpgradeMandatoryIQCheck{
        #5 Mandatory pre upgrade IQ check
        print "\n#############################################################################################\n";
        print "This is a mandatory procedure which needs to be executed before starting upgrade.\n";
		print "This will help to verify the state of tables and identify if any table is corrupted\n";
        print "\n#############################################################################################\n";
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("cat /eniq/admin/etc/dbcheck.env | grep RUNNUMBER\r");}]);
        if($exp->expect($timeout, 'RUNNUMBER=0')){
        print"\n###############################\n";
        print "If RUNNUMBER is 0, Full run will be performed otherwise Delta Run\n";
        }
}

sub UnpackCoreSW{
        print "\n############################################\n";
        print "To unpack the Core SW across the deployment\n";
		print "\n############################################\n";
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("cd /eniq/installation/core_install/bin\r");}]);
        $exp->expect(3);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("bash ./unpack_core_sw.bsh -a create -d $jumparea -p $upgradeDir\r");}]);
        if($exp->expect($timeout, 'Enter [Yes | No] (case sensitive) :')){
                $exp->send('Yes' . "\n");
        }
        if($exp->expect($timeout, 'Is the input provided correct? (Yy/Nn) :')){
                $exp->send('Y' . "\n");
        }
        $exp->expect(300, "#");
}

sub UpgradePreCheckExecutionProcedure{
        print "\n#############################################################################################\n";
        print "Upgrade Pre-check utility checks the readiness of ENIQ Statistics system prior to upgrade\n";
		print "\n#############################################################################################\n";
       # $exp->expect($def, ['#', sub {$exp = shift; $exp->send("cd /eniq/installation/core_install/eniq_checks/bin\r");}]);
	$exp->send("cd /eniq/installation/core_install/eniq_checks/bin\r");
        $exp->expect($timeout, "#");
        #$exp->expect($def, ['#', sub {$exp = shift; $exp->send("bash ./eniq_checks.bsh\r");}]);
	$exp->send("bash ./eniq_checks.bsh\r");
        $exp->expect(700, "#");
}

sub Multiblade_Migration_PM_procedure{

		#4.1.1  Solaris OS migration  procedure on existing Solaris 11 server
		#7.1.1  Pre Migration Procedure
		print "\n##################################################################\n";
		print "Solaris OS migration  procedure on existing Solaris 11 server \n";
		print "####################################################################\n";
		print "\n##################################################################\n";
		print "Pre Migration Procedure\n";
		print "\n##################################################################\n";
		#$jumparea = "/net/$eniq_jump_svr/JUMP/ENIQ_STATS/ENIQ_STATS/$SHIPMENT/eniq_base_sw";
		# $upgradeDir = "${rel}_${ship}_llsv${llsv_no}_upgrade_sw/";
		#my $OM_path="/net/10.44.194.10/JUMP/OM_MEDIA/OSSRC_O18_0/18.0.3/om";
		#UpgradeServerConnection($mach);
		$exp->send("cd /var/tmp/upgrade/$upgradeDir/core_install/bin\r");
		#$exp->expect($def, ['#', sub {$exp = shift; $exp->send("cd /var/tmp/upgrade/$upgradeDir/core_install/bin\r");}]);
		$exp->expect($timeout, "#:");
		#$exp->expect($timeout);
		#$exp->expect($def, ['#', sub {$exp = shift; $exp->send("zpool list\r");}]);
		$exp->send("zpool list\r");
		$exp->expect($timeout, "#");
		#$exp->expect($def, ['#', sub {$exp = shift; $exp->send("bash eniq_solaris_linux_migration.bsh -a premigration\r");}]);
		$exp->send("bash eniq_solaris_linux_migration.bsh -a premigration\r");
		$exp->expect($timeout, "#");
		if($exp->expect($timeout, 'Please enter ENIQ base SW location for migration')){
		$exp->send("$jumparea\r");
		}
		$exp->expect(10);
		if($exp->expect($timeout, 'Please enter O&M SW location for migration')){
		$exp->send("$om_sw_loc/om_linux\r");
		}
		if($exp->expect($timeout, 'Please enter Feature SW location for migration')){
		$exp->send("$featurearea\r");
		}
		$exp->expect(10);
		if($exp->expect($timeout, 'Do you want to proceed? (Yy/Nn)')){
		$exp->send("Y\r");
		}

		$exp->expect(10);
		if($exp->expect($timeout, 'Do you want to proceed? (Yy/Nn)')){
		$exp->send('Y' . "\n");
		}
		$exp->expect(10);
		if($exp->expect($timeout, 'password')){
		$exp->send("$SAN_PWD\n");
		}
		$exp->expect(10);
		if($exp->expect($timeout, 'Do you want to proceed? (Yy/Nn)')){
		$exp->send("Y\r");
		}
		$exp->expect(10);
		
		for( my $a = 0; $a < 4; $a = $a + 1 ) {
			if($exp->expect($timeout, "Please enter Is Backup VLAN is configured on")){
			$exp->send("NO\r");
			}
			$exp->expect(10);
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Please enter MWS IP')){
					$exp->send("10.45.192.153\r");
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Please enter NAS Console IP')){
					$exp->send("\r");
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Do you want to proceed? (Yy/Nn)')){
					$exp->send("Y\r");
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Please enter ENIQ license File path for Migration')){
					$exp->send("$ENIQ_LIC\r");
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Do you want to proceed? (Yy/Nn)')){
					$exp->send("Y\r");
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Please enter password for root user')){
					$exp->send("shroot12\r");
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Please enter password for  dcuser')){
					$exp->send("dcuser\r");
		}
		$exp->expect(10);
		if ($exp->expect($timeout, 'Do you want to proceed? (Yy/Nn)')){
					$exp->send("Y\r");
		}
		$exp->expect(50);       
		if ($exp->expect($timeout, ' Press enter key to continue.')){
					$exp->send("\r");
		}
		
		if ($exp->expect(900, 'Entering Linux premigration stage - get_migration_data')){
			$exp->expect(10);
			for( my $a = 0; $a < 3; $a = $a + 1 ) {
				if ($exp->expect($timeout, 'Please enter password for root user')){
							$exp->send("shroot12\r");
				}
				$exp->expect(10);
				if ($exp->expect($timeout, 'Please enter password for  dcuser')){
							$exp->send("dcuser\r");
				}
				$exp->expect(10);
				if ($exp->expect($timeout, 'Do you want to proceed? (Yy/Nn)')){
							$exp->send("Y\r");
				}
				$exp->expect(200);
			}
		}
		
		if ($exp->expect($undef, 'Successfully completed - cleanup_premigration')){
			print "Successfully completed - premigration stage\n\n";
		}else{
			print "Premigration got failed in server: Hence exiting \n\n";
		    exit;
		}

		$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("zpool list\r");}]);
		$exp->expect(60);
        
}


sub solaris_OS_installation_standalone{
#6.6.3.3 Boot command
                UpgradeServerConnection($mach);
                $exp->expect($def, ['#', sub {$exp = shift; $exp->send("init 6\r");}]);
                $exp->expect(60);

               solaris_BootCommand();
                #ILOMCON();
                #$exp->expect($def, ['#:', sub {$exp = shift; $exp->send("init 6\r");}]);
                #$exp->expect(60);

#6.6.4 Solaris OS Installation
                LOAD_EXP_BLADE();
}

sub solaris_BootCommand{
#6.6.3.3 Boot command
                print "\n#####################################\n";
                print "About to Run configuration for tftpboot command...\n";
                print "#######################################\n";
                #####################################
                # Calling Expect Module
                #####################################
                my $timeout = 90;
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
                        [ 'assword: $' => sub {
                                                $exp->send("$dm_root_storage\r");
                                                exp_continue; }
                        ],

                        '-re', qr'[^.*->#] $' => sub {
                                         exp_continue; }

                );
                #if ("$operatingSystem" eq "linux"){
                        my $mancount = 1;
                        while ($mancount <= 3) {
                                print "YES\n";
                                 #$exp->send("cd /JUMP/LIN_MEDIA/1/kickstart/${mach} \r");
                                #$exp->expect(15);
                                #$exp->send("cp ${mach}_ks_cfg.txt /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/Clients \r");
                                #$exp->expect(15);
                                $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a remove -c ${mach} -N\r");
                                $exp->expect(15);
                                $exp->send("/ericsson/kickstart/bin/manage_linux_dhcp_clients.bsh -a add -f /net/10.45.192.153/JUMP/ENIQ_STATS/ENIQ_STATS/Clients/${mach}_ks_cfg.txt -N\r");

                                $exp->expect(15);
								# captures the output of the last send exp command
                                my $manageoutput = $exp->before();
                                if ( $manageoutput =~ /with client data/){
                                        print "\n###############################################\n";
                                        print "Breaking from While Manage_dhcp was successful\n";
                                        print "Successful on try $mancount of 3\n";
                                        print "###############################################\n";
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


sub LOAD_EXP_BLADE {
        print "\n###############################\n";
        print "About to Call Expect Module... Connect to ILO\n";
        print "###############################\n";

        #print "/usr/bin/ssh $root_user\@$ilo_ip_addr\n";
        #$exp = Expect->spawn("/usr/bin/ssh $root_user\@$ilo_ip_addr" ) or die "Unable to spawn ssh  to $ilo_ip_addr.\n";

        $exp->send("/usr/bin/ssh $root_user\@$ilo_ip_addr \r");
        $exp->expect(50);

        #if($exp->expect($timeout, 'Are you sure you want to continue connecting (yes/no)?')){
                $exp->send('yes' . "\n");
        #}

        $exp->expect(120,
                [ '[Pp]assword: $' => sub {
                                        $exp->send("$PASS\r");
                                        exp_continue; }
                ],

                '-re', qr'[^.*->] $' => sub { exp_continue; }
        );
       # $exp->expect(20, ['->', sub {$exp->send("\r");}]) or die "ssh failed to connect: $!\n";
        $exp->expect(20, '>') or die "ssh failed to connect:\n";

        $exp->expect($timeout, ['hpiLO->', sub {$exp = shift; $exp->send("onetimeboot netdev1\r");}]);
        ### Wait 200 seconds
        $exp->expect(20);

        #Reset System ( form of cold boot)
        #$exp->expect($timeout, ['hpiLO->', sub {$exp = shift; $exp->send("start /system1\r");}]);

        ### Wait 30 seconds
        #$exp->expect(300);

    #Reset System ( form of cold boot)
        $exp->expect($timeout, ['hpiLO->', sub {$exp = shift; $exp->send("reset /system1\r");}]);

        ### Wait 30 seconds
        $exp->expect(30);

        ### Reorder the boot order to boot from disk
        #$exp->expect($undef, ['hpiLO->', sub {$exp = shift; $exp->send("set /system1/bootconfig1/bootsource3 bootorder=1\r");}]);

        ### Stop VSP
        $exp->expect($undef, ['hpiLO->', sub {$exp = shift; $exp->send("stop /system1/oemhp_vsp1 \r");}]);
         $exp->expect(30);

        ### Start VSP
        $exp->expect($undef, ['hpiLO->', sub {$exp = shift; $exp->send("vsp\r");}]);
        $exp->expect(1800);
}

sub Migration_standalone{
#6.8 Run Migration
     # my $jumparea = "/net/$eniq_jump_svr/JUMP/ENIQ_STATS/ENIQ_STATS/$SHIPMENT/eniq_base_sw";
      #  my $OM_path="/net/10.44.194.10/JUMP/OM_MEDIA/OSSRC_O18_0/18.0.4/";
          print "\n\n###############################################\n";
                print "Strating the migration procedure\n";

        #       $Storge_VLAN_INT=`dladm show-phys | awk -F" " '{print \$1}' | grep $IPMP_Group_Intf `;
                if($exp->expect($timeout, 'Select one appropriate group interface configured for PM Services Group from the list above (Example :<Interface_1>)')){
                $exp->send("eno50\r");
                }
                $exp->expect(10);
                 if($exp->expect($timeout, 'If there are multiple IP addresses to be entered, then they should be separated by comma')){
                $exp->send("10.45.192.153,10.45.193.229\r");
                 }
                 $exp->expect(60);
		if($mach =~ 'ieatrcxb6506'){
                	if($exp->expect($timeout, 'Is Storage VLAN configured on ieatrcxb6506? (Yes/No)')){
                	$exp->send("No\r");
                	}
		}
		if($mach =~ 'ieatrcxb6507'){
                	if($exp->expect($timeout, 'Is Storage VLAN configured on ieatrcxb6507? (Yes/No)')){
                	$exp->send("No\r");
                	}
                }
		if($mach =~ 'ieatrcxb6508'){
                	if($exp->expect($timeout, 'Is Storage VLAN configured on ieatrcxb6508? (Yes/No)')){
                	$exp->send("No\r");
                	}
                }
		if($mach =~ 'ieatrcxb6509'){
                	if($exp->expect($timeout, 'Is Storage VLAN configured on ieatrcxb6509? (Yes/No)')){
                	$exp->send("No\r");
                	}
                }

                 $exp->expect(60);
                # if($exp->expect($timeout, 'Please enter the Storage VLAN Interface Name')){
                # $exp->send("bnxe0\r");
        #       }
        #        $exp->expect(60);
        #       if($exp->expect($timeout,'Please enter the Storage VLAN IP address')){
        #       $exp->send("$STG_IP\r");
        #       }
        #        $exp->expect(60);
        #       if($exp->expect($timeout,'Please enter the Storage VLAN Netmask IP')){
        #       $exp->send("$STG_NET\r");
        #       }
        #        $exp->expect(60);
		if($mach =~ 'ieatrcxb6506'){
                	if ($exp->expect($timeout, 'Is Backup VLAN configured on ieatrcxb6506? (Yes/No)')) {
                        $exp->send("No\r");
                	}
		}
		if($mach =~ 'ieatrcxb6507'){
                	if ($exp->expect($timeout, 'Is Backup VLAN configured on ieatrcxb6507? (Yes/No)')) {
                        $exp->send("No\r");
                	}
                }
		if($mach =~ 'ieatrcxb6508'){
                	if ($exp->expect($timeout, 'Is Backup VLAN configured on ieatrcxb6508? (Yes/No)')) {
                        $exp->send("No\r");
                	}
                }
		if($mach =~ 'ieatrcxb6509'){
                	if ($exp->expect($timeout, 'Is Backup VLAN configured on ieatrcxb6509? (Yes/No)')) {
                        $exp->send("No\r");
                	}
                }

                $exp->expect(10);

                if ($exp->expect($timeout, 'Do you want to proceed with above values? (Yes/No)')) {
                        #$exp->send("/vx/$storagepool-backup/migration_sw\r");
                        $exp->send("Yes\r");
                }
                 $exp->expect(10);

                if ($exp->expect($timeout, 'Enter Migration backup server IP address')) {
                        $exp->send("10.148.9.116\r");
                }
                 $exp->expect(10);
                 if ($exp->expect($timeout, 'Enter the directory path of Migration backup [e.g. /vx/<NAS_POOL>-portbackup]')) {
                        $exp->send("/vx/s_eniq-portbackup\r");
                }
                $exp->expect(10);
        if ($exp->expect($timeout, 'Do you want to proceed with above values? (Yes/No)')) {
                        $exp->send("Yes\r");
                }
                $exp->expect(10);
		if ($exp->expect($timeout, 'Enter LUN ID of the newly created LUN:')) {
                        $exp->send("${lun}\r");
                }
                $exp->expect(10);
        if ($exp->expect($timeout, 'Do you want to proceed with above values? (Yes/No)')) {
                        $exp->send("Yes\r");
                }
                $exp->expect(10);


                if ($exp->expect($undef, 'Successfully completed OS Migration on Linux')){
                        print "Successfully completed - Migration stage\n\n";
                }else{
                        print "Migration got failed in server: Hence exiting \n\n";
                        exit 1;
                }
                $exp->expect(160);
                if ($exp->expect($undef, ' login')){
                        print "Successfully completed OS Migration on Linux\n\n";
                }else{
                        print "Migration got failed in server: Hence exiting \n\n";
                        exit 1;
                }
                $exp->expect(640);

         #$exp->expect($def, ['~#', sub {$exp = shift; $exp->send("bash /eniq/installation/core_install/bin/eniq_solaris_migration.bsh -a migration -d $jumparea -o $OM_path\r");}]);
}


sub Post_migration_standalone{
#6.9 Post Migration
# Start all ENIQ Services

        print "\n###############################\n";
        print "Calling manage_eniq_services to start the Eniq Services \n";
        print "###############################\n";
        $exp->expect(640);
        UpgradeServerConnection($mach);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("cd /eniq/admin/bin\r");}]);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("bash ./manage_eniq_services.bsh -a start -s ALL -N\r");}]);
        $exp->expect(10);
        if ($exp->expect($timeout, 'Are you sure you wish to start the services on the above servers?
Enter [Yes | No] (case sensitive) :')) {
                        $exp->send("Yes\r");
                }
        $exp->expect(40);
        $exp->expect($def, ['#', sub {$exp = shift; $exp->send("/usr/bin/systemctl -a | grep eniq\r");}]);
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
#       print "Upgrade Execution time in hour :$ch hour\n";
}
        else
        {
        $ch=$eh -$sh;
#       print "Upgrade Execution time in hour :$ch hour\n";
        }
        $ch =$ch -1;
        $sm = 59 - $sm;
        $cm = $sm + $em;

        $ss = 60 - $ss;
        $cs = $ss + $es;
        if ( $cs >=60 )
        {
        $cm = $cm+1;
        $cs = $cs - 60;
        }
        if ( $cm >=60)
        {
        $ch = $ch + 1;
        $cm = $cm - 60;
        }
        print "Total Run Time is $ch:$cm:$cs\n";
}




##Main 
{
        $ENV{"TZ"}="Eire";
        PARAMETERS();           
	print "Is Storage VLAN configured on ${mach}? (Yes/No)\n";
        MediaInfo();
        ENIQBLADEDETAILS();
	UpgradeServerConnection($mach);
	MultibladeMigration();

        TIMECALC();
        #cleanup("Your UG was successful on $MACHINE at $SMS_Date");
        #printf"\n\nEND : %s\n\n", $run_time;
}

