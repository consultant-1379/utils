#!/usr/bin/perl

use strict;
use warnings;
no warnings 'uninitialized';
use Data::Dumper;

my ($secs,$mins,$hours,$mdays,$mons,$years,$wdays, $ydays,$isdsts)=localtime( time - 86400 );
$mons++;
$years=1900+$years;
my $yesterdayDate = sprintf "%02d-%02d-%4d", $mdays,$mons,$years;

############################################################### Copying Files from Storage(TopologyFiles) to Server(Predefined Path)
sub copyFilesFromTopoToServer{
	my $topologyFile = $_[0];
	my $string = $_[1];
	my $dir = $_[2];
	my $srcPath = $topologyFile.$string;
	my $targetPath = '/eniq/data/pmdata/eniq_oss_1/'.$dir;
	print "SourcePath : $srcPath \n TargetPath: $targetPath \n";
	system ("mkdir -p $targetPath ") == 0 or die "failed to create a directory $targetPath\n";
	system ("cp -R $srcPath $targetPath");
}

sub epfgdataGeneration{
	my ($line);
	my $i;
	my @array;
	my @query_array;
	my $key;
	my $path;
	my $epfgpropertiesfile = '/eniq/home/dcuser/epfg/config/epfg.properties';
	my $topologyFile = '/eniq/home/dcuser/TopologyFiles/';
	
	my $file = '/eniq/home/dcuser/data.txt';
	open FILE, '<', $file or die "Could not open '$file', No such file found in the provided path $!\n";
	@array = <FILE>;
	print "@array\n";
	close(FILE);
	my $count = @array;

###############################################################
	
	for ($i=0;$i<$count;$i++) {
		undef $line;
		$line = shift @array;
		chomp $line;
		print "$line\n";
		my ($d,$string,$r,$b) = $line  =~ m/(DC_\w_|DIM_\w_)(\w*)(\_R.+\_b)(\d+)/;
		print "$d";
		print "$string\n";
		################################ List of gen flags from epfg.properties file 
		my %PmGenNodes = (
				"GGSN" => ["ggsnGenFlag" , "ggsnMpgGenFlag" , "ggsnPgwGenFlag" , "ggsnSgwGenFlag" , "ggsnNodeGenFlag" , "epgMbmSgwGenFlag" , "epgyangGenFlag" , "epgyang2GenFlag"],
				"SGSN" => ["enable3gppGenFlag" ,"ebssSgsnGenFlag" , "sgsnGenFlag"],
				"SGSN-MME" => ["sgsnMmeGenFlag" , "sgsnmmecomGenFlag"],
				"SNMP" => ["snmpNtpGenFlag" , "snmpMgcGenFlag" , "snmpIpRouterGenFlag" , "snmpHpMrfpGenFlag" ,"snmpHotsipGenFlag","snmpDnsServerGenFlag","snmpDhcpServerGenFlag","snmpCsMsGenFlag","snmpCsDsGenFlag","snmpCsCdsGenFlag","snmpCsAsGenFlag","snmpLanSwitchGenFlag","snmpGgsnGenFlag","snmpFirewallGenFlag","snmpAcmeGenFlag"],
				"MGW"  => ["mgwGenFlag" , "mgw2fdGenFlag"],
				"SASN" => ["sasnGenFlag" , "sasnSaraGenFlag" , "sasn3gppGenFlag"],
				"SAPC" => ["sapcGenFlag" ,"sapcECIMGenFlag","sapcTSPGenFlag"],
				"IMSGW_SBG" => ["sbgGenFlag","ISSBGGenFlag",],
				"IMS" => ["cscfGenFlag","imsWuigmGenFlag" ,"imsGenFlag","imsMGenFlag","imsTSPGenFlag"],
				"HSS" => ["hssTSPGenFlag","hssGenFlag" ,"hssECIMGenFlag"],
				"RNC" => ["rncGenFlag"],
				"BSS" => ["bscApgGenFlag" , "bscIogGenFlag" , "ebagBscGenFlag" , "bssEventGenFlag" , "GSMMixModeOffGenFlag"],
				"RBS" => ["wranRBSGenFlag"],
				"STN" => ["stnPicoGenFlag" , "stnSiuGenFlag" , "stnTcuGenFlag" ],
				"CPG" => ["cpgGenFlag"],
				"DSC" => ["dscGenFlag"],
				"EPDG" => ["epdgGenFlag"],
				"TCU" => ["Tcu03GenFlag" , "vTIFGenFlag" , "twampSlGenFlag" , "RadioNodeMixedGenFlag" , "RBSG2GenFlag" , "GSMG2GenFlag" , "5GRadioNodeGenFlag" , "nrEventsGenFlag", "vPPGenFlag"],
				"REDBACK" => ["edgeRtrGenFlag" , "RedbComEcimGenFlag"],
				"MTAS" => ["mtasGenFlag"."mtasTSPGenFlag"],
				"CUDB" => ["cudbGenFlag"],
				"IMS_IPW" => ["ipworksGenFlag"],
				"CSCF" => ["vcscfGenFlag"],
				"SMPC" => ["smpcGenFlag"],
				"GMPC" => ["gmpcGenFlag"],
				"ERBS" => ["lteEventGenFlag","wranLteGenFlag"],
				"REDB" => ["smartMetroGenFlag"],
				"MGC" => ["mgcGenFlag"], 
				"CNAXE" => ["hlrBsGenFlag" , "mscApgGenFlag" , "mscApgOmsGenFlag" , "mscIogGenFlag" , "mscIogOmsGenFlag" , "mscBcGenFlag" , "mscBcOmsGenFlag" , "hlrApgGenFlag" , "hlrIogGenFlag"],
				"BBSC" => ["bbscGenFlag"],
				"CCDM" => ["CCDMGenFlag"],
				"CCRC" => ["CCRCGenFlag"],
				"CCSM" => ["CCSMGenFlag"],
				"CISCO" => ["CISCOGenFlag"],
				"CCPC" => ["CCPCGenFlag"],
				"CCES" => ["CCESGenFlag"],
				"IPTRANSPORT" => ["spitfireGenFlag","ipTransportGenFlag","FrontHaulGenFlag","MinilinkOutdoorGenFlag","MiniLinkIndoorSNMPGenFlag" , "MinilinkoutdoorSwitchGenFlag"],
				"JUNOS" => ["JUNIPERGenFlag"],
				"MRS" => ["mrsGenFlag","MRSvGenFlag"],
				"NETOP" => ["mrrGenFlag","NCSGenFlag"],
				"NR" => ["5GRadioNodeGenFlag","nrEventsGenFlag", "RadioNodeMixedGenFlag"],
				"PCC" => ["PCCGenFlag"],
				"AFG" => ["afgGenFlag"],
				"BSP" => ["bspGenFlag"],
				"WMG" => ["WmgGenFlag" , "wmgyangGenFlag"],
				"ESC" => ["EscGenFlag"],
				"PCG" => ["PCGGenFlag"],
				"SMSF" => ["SMSFGenFlag"],
				"SC" => ["SCGenFlag"],
				"CUDB" => ["cudbGenFlag" , "EirFeGenFlag"],
				"SCEF" => ["scefGenFlag"],
				"ERBSG2" => ["erbsg2GenFlag" , "RadioNodeMixedGenFlag"],
				"RBSG2" => ["RadioNodeMixedGenFlag" , "RBSG2GenFlag"],
				"BTSG2" => ["RadioNodeMixedGenFlag" , "GSMG2GenFlag"],
				"RNC" => ["rncGenFlag"],
				"CPP" => ["rncGenFlag" , "wranRXIGenFlag" , "wranRBSGenFlag","wranLteGenFlag"],
				"RXI" => ["wranRXIGenFlag"],
				"TSSAXE" => ["TSSAXEASNAPGGenFlag" , "TSSAXEASNIOGGenFlag" , "TSSAXEASNOmsGenFlag" , "TSSAXE3gppGenFlag"],
				"UDM" => ["UdmGenFlag"],
				"CONTROLLER" => ["ControllerGenFlag"],
				"CMN_STS" => ["GSMMixModeOffGenFlag"],
				"UPG" => ["upgGenFlag"],
				"WCG" => ["WcgGenFlag"],
				"vEME" => ["vEMEGenFlag"],
				"vPP" => ["vPPGenFlag"],
			);
		
		my %PmDirList = (
				"LTE" => ["lte/topologyData"],
				"ERBS" => ["lte/topologyData/ERBS"],
				"NR" => ["lte/topologyData/nr"],
				"ERBSG2" => ["lte/topologyData/ERBS"],
				"CN" => ["core"],
				"CSCF" => ["core/topologyData/CoreNetwork"],
				"MTAS" => ["core/topologyData/CoreNetwork"],
				"vEME" => ["core/topologyData/CoreNetwork"],											
				"WMG" => ["core/topologyData/CoreNetwork"],
				"BSP" => ["core/topologyData/CoreNetwork"],
				"IMSGW_SBG" => ["core/topologyData/CoreNetwork"],
				"AFG" => ["core/topologyData/CoreNetwork"],
				"CUDB" => ["core/topologyData/CoreNetwork"],
				"SAPC" => ["core/topologyData/CoreNetwork"],
				"IMS_IPW" => ["core/topologyData/CoreNetwork"], 
				"MRS" => ["core/topologyData/CoreNetwork"],
				"AFG" => ["core/topologyData/CoreNetwork"],
				"GGSN" => ["core/topologyData/CoreNetwork"],	
				"HSS" => ["core/topologyData/CoreNetwork"],
				"SGSN" => ["core/topologyData/CoreNetwork"],		 	
				"SGSNMME" => ["core/topologyData/CoreNetwork"],
				"vPP" => ["core/topologyData/CoreNetwork/vPP"],
				"CCSM" => ["5GCORE"],
				"CCRC" => ["5GCORE"],
				"CCDM" => ["5GCORE"],
				"CCES" => ["5GCORE"],
				"CCPC" => ["5GCORE"],
				"PCC" => ["5GCORE"],
				"NRFAGENT" => ["5GCORE"],
				"PCG" => ["5GCORE"],
				"IPTRANSPORT" => ["transport/topologyData"],
				"LLE" => ["LLEConfig"],
				"BTSG2" => ["gsm/topologyData/RADIO"],
				"CNAXE" => ["core/topologyData/AXE"],								 
				"ESC" => ["transport/topologyData/ESC"],
				"RNC" => ["utran/topologyData/RNC"],
				"RBS" => ["utran/topologyData/RBS"],
				"RXI" => ["utran/topologyData/RXI"],
				"CPP" => ["utran/topologyData" , "lte/topologyData:ERBS"],
				"JUNOS" =>["transport/topologyData/JUNOS_XML"],
				"SPITFIRE" =>["transport/topologyData/Router6k"],
				"TSSAXE" => ["tss/topologyData/AXE"],
				"BSS" => ["gran/topologyData"],
				"CISCO" => ["transport/topologyData/CISCO_XML"],
				"FFAX" => ["lte/topologyData/ERBS"],
				"RBSG2" => ["utran/topologyData/RBS"],
				"BBSC" => [""],
				"CMN_STS" =>  [""],		 	
				"CMN_STS_PC" =>  [""],	 			 	
				"CN_TOP" =>  [""],
				"CPG" => [""], 		 	
				"CSCFV" => [""], 	 		 		 	
				"DSC" =>  [""],
				"EBSG" =>  [""],		 	
				"EBSS" =>  [""],		
				"EBSW" =>  [""],		 	
				"ENERGY" => [""], 		
				"EPDG" => [""],	 		 		 	
				"EVENTS" => [""],	 	
				"FFAXW" =>  [""],		 	
				"GMPC" => [""],		 	
				"GRAN_BASE" => [""],		 	
				"GRAN_TOP" => [""],	 	
				"HWUTIL" => [""],	 	
				"IMS" => [""], 	
				"IMSGW_MGW" => [""],
				"IMSGW_SBG_ECIM" => [""],
				"IMS_ICS" => [""],
				"IMS_M" => [""],
				"IMS_PTT" => [""],
				"INFORMATION_STORE"	=> [""], 	
				"IPPROBE" => [""],	 	
				"IPRAN" => [""],	 	
				"IPTNMS" => [""],		 	
				"IPTNMS_TOP" => [""],
				"IPTRANSPORT_TOP" => [""],
				"MGC" => [""],
				"MGW" => [""], 	
				"ML_HC_E" => [""],
				"MSP" => [""],
				"NETOP"	 => [""], 		 		 	
				"NSDS" => [""],		 	
				"OCC" => [""],	 	
				"OPT1600_1200" => [""],		 	
				"OPT3200" => [""],	 	
				"OPT800_1400" => [""],		 	
				"OPT_MHL3000" => [""],		 	
				"OPT_OMS3200" => [""],	 		 	
				"PRBS" => [""],		 	
				"PRBS_CPP" => [""],		 	
				"PRBS_ERBS"	 => [""],	 	
				"PRBS_RB" => [""],		 	
				"RAN_BASE_SITEDST" => [""],		 	
				"RED" => [""],	 	
				"REDB_CPG" => [""],		 	
				"REDB_EDGE" => [""],	 	
				"REDB_MLPPP" => [""],		 	
				"REDB_SAEGW" => [""],		 	
				"SAS" => [""],		 	
				"SASN_SARA" => [""],		 	
				"SC" => [""],
				"SCEF" => [""],		 	
				"SDNCP" => [""],		 	
				"SGS" => [""],		 	
				"SMPC" => [""],		 	
				"SMSF" => [""],		 	
				"SNMP" => [""],		 	
				"SOEM" => [""],		 	
				"SOEM_MBH" => [""],		 	
				"SOEM_TOP" => [""],		 	
				"SONV_CM" => [""],		 	
				"SONV_FM" => [""],		 	
				"SONV_PM" => [""],		 	
				"STN" => [""],	 	
				"TCU" => [""],		 	
				"TDRAN_BASE" => [""],	 	
				"TDRAN_TOP"	 => [""],	 	
				"TDRBS"	 => [""],	 	
				"TDRNC"	 => [""],	 	
				"TNSPP" => [""],		 		 	
				"TSS" => [""],	 	
				"TSSAXD" => [""],	 		 	
				"TSS_TGC" => [""],	 	
				"TSS_TOP" => [""],		 	
				"UDM" => [""],	 	
				"UPG" => [""],	 	
				"UTRAN_BASE" => [""],	 	
				"UTRAN_TOP" => [""],		 			 	
				"VOLTE"	 => [""],	 	
				"VOWIFI" => [""],		 	
				"VPP" => [""],		 	
				"WCG" => [""],		 	
				"WIFI" => [""],		 	
				"WLE" => [""],	 	
			);
		my @keys = keys %PmGenNodes;
			
			###########################################################	Checking DC Techpack
		if ( $d =~ m/(^DC_\w*)/ ) {	
			
			opendir my $tpDir, $topologyFile or die "Cannot open directory:$topologyFile $!";
			my @tpDirList = readdir $tpDir;
			closedir $tpDir;
			
			if ($string ~~ @tpDirList){
				
				my $storage = $topologyFile.$string.'/';
				opendir my $dirs, $storage."/" or die "Cannot open directory:$topologyFile.$string $!";
				my @dirList = grep { !/^\.\.?$/ } readdir $dirs;
				closedir $dirs;
				my $dirSize = scalar @dirList;
				if ( $dirSize > 0 ) {
					my @dirArray = @{$PmDirList{$string}};
					my $size = scalar @dirArray;
					if ($size == 1) {
						copyFilesFromTopoToServer($topologyFile,$string."/*",$dirArray[0]);
					} 
					if ( $size > 1 ) {
						my @seprateDir;
						for my $dir (@dirArray) {
							my @dirName = split(':', $dir); 
							if( defined $dirName[1]) {
								push(@seprateDir, $dirName[1]);
							}
						}
						for my $dir (@dirArray) {
							my @dirName = split(':', $dir); 
							if( defined $dirName[1]) {
								for my $folder (@dirList) {
									if( $folder ~~ @seprateDir) {
										copyFilesFromTopoToServer($topologyFile,$string."/".$folder."/",$dirName[0]);
									}
								}
							} else {
								for my $folder (@dirList) {
									if ( !($folder ~~ @seprateDir) ) {
										copyFilesFromTopoToServer($topologyFile,$string."/".$folder."/",$dirName[0]);
									}
								}
							}
						}
					}
					sleep (60);
				} else {
					print "$string directory is not exists under the $topologyFile";
				}
			}
			if ($string ~~ @keys){

				print "From hash : @{$PmGenNodes{$string}}\n";
				@query_array = @{$PmGenNodes{$string}};
				print "From condition : @query_array\n";				
				my ($count1,$j);
				$count1 = @{$PmGenNodes{$string}};
				print "$count1\n";
				
				##################################################### Changing the GenFlag, StartTime and EndTime
				for ($j=0;$j<$count1;$j++){
					my $genflag = $query_array[$j];
					my $flagName = substr($genflag,0, -7);
					print "$j : $genflag\n";
					
					my $pattern = $genflag."=NO";
					my $new_pattern = $genflag."=YES";
					print "Pattern in epfg is $pattern\n";
					
					my $oldStartTime = $flagName."StartTime=";
					my $newStartTime = $flagName."StartTime=".$yesterdayDate."-10:00\n";
					
					my $oldEndTime = $flagName."EndTime=";
					my $newEndTime = $flagName."EndTime=".$yesterdayDate."-11:00\n";
					open EPFGFILE, '<', $epfgpropertiesfile or die "Could not open '$epfgpropertiesfile', No such file found in the provided path $!\n";
					
					my @epfg_lines = <EPFGFILE>;
					close(EPFGFILE);

					my @epfg_newlines;
					foreach(@epfg_lines) {
						$_ =~ s/$pattern/$new_pattern/g;
						if($_ =~ m/(^$oldStartTime)/ ) {
							$_ =~ s/$_/$newStartTime/g;
						}
						if($_ =~ m/(^$oldEndTime)/ ) {
							$_ =~ s/$_/$newEndTime/g;
						}
						push(@epfg_newlines,$_);
					}
					open(EPFGFILE, ">/eniq/home/dcuser/epfg/config/epfg.properties") || die "File not found";
					print EPFGFILE @epfg_newlines;
					close(EPFGFILE);
				}
			}
		} 
		
		
		###########################################################	Checking DIM Techpack
		if ( $d =~ m/(^DIM_\w*)/) {
			
			opendir my $tpDir, $topologyFile or die "Cannot open directory:$topologyFile $!";
			my @tpDirList = readdir $tpDir;
			closedir $tpDir;
			
			if ($string ~~ @tpDirList){
				
				opendir my $dir, $topologyFile.$string or die "Cannot open directory:$topologyFile.$string $!";
				my @files = readdir $dir;
				closedir $dir;
				
				my $subDirpath = '/eniq/data/pmdata/eniq_oss_1/';
				my $sourceDir = $topologyFile.$string.'/';
				if (-d $sourceDir) {
					my $src = $sourceDir."*";
					print "SourcePath : $src \n TargetPath: $subDirpath \n";
					system ("cp -R $src $subDirpath");
				}
			}
		}
	}
}
	
	epfgdataGeneration();