#!/usr/bin/perl

use strict;
use warnings;
no warnings 'uninitialized';
use DBI;
use Data::Dumper;

my ($sec,$min_current,$hour,$mday,$mon,$year,$wday, $yday,$isdst)=localtime(time);
my $min_future = $min_current + 2;
my $date = sprintf "%4d-%02d-%02d", $mday,$mon+1,$year+1900;
$date =~ s/^\s+|\s+$//g;
my $today = sprintf "%4d-%02d-%02d-%02d:%02d", $mday,$mon+1,$year+1900,$hour,$min_future;
$today =~ s/^\s+|\s+$//g;
print "$today\n";

sub epfgdataGeneration{
        my ($line);
        my $i;
        my @array;
        my @query_array;
        my $key;
        my $path;
        my $epfgpropertiesfile = '/eniq/home/dcuser/epfg/config/epfg.properties';
        
        my $file = '/eniq/home/dcuser/data.txt';
        open FILE, '<', $file or die "Could not open '$file', No such file found in the provided path $!\n";
        @array = <FILE>;
        print "@array\n";
        my $count = @array;

###############################################################
        
        for ($i=0;$i<$count;$i++) {
                undef $line;
                $line = shift @array;
                chomp $line;
                print "$line\n";
                my ($d,$string,$r,$b) = $line  =~ m/(DC_\w*_)(\w*)(\_R.+\_b)(\d+)/;
                print "$string\n";
                ################################ List of gen flags from epfg.properties file 
                my %PmGenNodes = (
                        "GGSN" => ["ggsnGenFlag","ggsnMpgGenFlag","ggsnPgwGenFlag","ggsnSgwGenFlag","epgMbmSgwGenFlag","ggsnNodeGenFlag",],
                        "CNAXE" => [ "mscApgGenFlag" ,"mscIogGenFlag","mscBcGenFlag", "hlrApgGenFlag" , "hlrIogGenFlag" ],
                        "SGSN" => ["enable3gppGenFlag" ,"ebssSgsnGenFlag" , "sgsnGenFlag" , "sgsnMmeGenFlag"],
                        "SNMP" => ["snmpNtpGenFlag" , "snmpMgcGenFlag" , "snmpIpRouterGenFlag" , "snmpHpMrfpGenFlag" ,"snmpHotsipGenFlag","snmpDnsServerGenFlag","snmpDhcpServerGenFlag","snmpCsMsGenFlag","snmpCsDsGenFlag","snmpCsCdsGenFlag","snmpCsAsGenFlag","snmpLanSwitchGenFlag","snmpGgsnGenFlag","snmpFirewallGenFlag","snmpAcmeGenFlag"], 
                        "MGW" => ["mgwGenFlag"],
                        "SASN" => ["sasnGenFlag","sasnSaraGenFlag"],
                        "SAPC" => ["sapcGenFlag" ,"sapcECIMGenFlag",],
                        "SBG" => ["sbgGenFlag","ISSBGGenFlag",],
                        "IMS" => ["imsWuigmGenFlag" ,"imsGenFlag","imsMGenFlag"],
                        "HSS" => ["hssGenTopology","hssGenFlag" ,"hssECIMGenFlag"],
                        "WRAN-LTE" => ["wranLteGenFlag" , "erbsg2GenFlag"],
                        "TD-RNC" => ["tdRNCGenFlag"],
                        "WRAN-RNC" => ["ebawRncGenFlag" , "rncGenFlag"],
                        "BSC" => ["bscApgGenFlag" , "bscIogGenFlag" , "ebagBscGenFlag"],
                        "Wran-RBS" => ["wranRBSGenFlag"],
                        "STN" => ["stnPicoGenFlag" , "stnSiuGenFlag" , "stnTcuGenFlag" ],                
                        "MLPPP" => ["mlpppGenFlag"],
                        "CPG" => ["cpgGenFlag"],
                        "TWAMP" => ["twampGenFlag"],
                        "TD-RBS" => ["tdRBSGenFlag"],                
                        "PRBS" => ["PRBSGenFlag"],
                        "DSC" => ["dscGenTopology","dscGenFlag"],
                        "EPDG" => ["epdgGenFlag"],
                        "TCU03" => ["Tcu03GenFlag"],
                        "EDGE-ROUTER" => ["edgeRtrGenFlag"],
                        "MTAS" => ["mtasGenFlag"],
                        "CUDB" => ["cudbGenFlag"],
                        "IPWORKS" => ["ipworksGenFlag"],
                        "CSCF" => ["cscfGenFlag"],
                        "MRFC" => ["mrfcGenFlag"],              
                        "SMPC" => ["smpcGenFlag"],      
                        "GMPC" => ["gmpcGenFlag"],
                        "EBSS-MME" => ["ebssMmeGenFlag"],
                        "LTE-Event" => ["lteEventGenFlag"], 
                        "SE-BGF" => ["seBgfGenFlag"],
                        "SMART-METRO" => ["smartMetroGenFlag"],
                        "vCSCF" => ["vcscfGenFlag"],
                        "TSS-TGC" => ["tssTgcGenFlag"],
                        "MGC" => ["mgcGenFlag"],
                        "HLR-BS" => ["hlrBsGenFlag"],
                        "MGW2.0FD" => ["mgw2fdGenFlag"],
                        "BBSC" => ["bbscGenFlag"],
                        "SDNC" => ["SDNCGenFlag"],
                        );
                
                        my @keys = keys %PmGenNodes;
                        
                        ###########################################################     
                        if ($string ~~ @keys){

                                print "From hash : @{$PmGenNodes{$string}}\n";
                                @query_array = @{$PmGenNodes{$string}};
                                print "From condition : @query_array\n";                                
                                my ($count1,$j);
                                $count1 = @{$PmGenNodes{$string}};
                                print "$count1\n";

                                ##################################################### Changing the GenFlag      
                                for ($j=0;$j<$count1;$j++){
                                        my $genflag = $query_array[$j];
                                        print "$j : $genflag\n";
                                        
                                        my $pattern = $genflag."=NO";
                                        my $new_pattern = $genflag."=YES";
                                        print "Pattern in epfg is $pattern\n";
                                        
                                        open EPFGFILE, '<', $epfgpropertiesfile or die "Could not open '$epfgpropertiesfile', No such file found in the provided path $!\n";
                                        
                                        my @epfg_lines = <EPFGFILE>;
                                        close(EPFGFILE);

                                        my @epfg_newlines;
                                        foreach(@epfg_lines) {
                                                $_ =~ s/$pattern/$new_pattern/g;
                                                push(@epfg_newlines,$_);
                                        }
                                        open(EPFGFILE, ">/eniq/home/dcuser/epfg/config/epfg.properties") || die "File not found";
                                        print EPFGFILE @epfg_newlines;
                                        close(EPFGFILE);

                                        ########################################################### Changing the gentime if Topology is there

                                        my $epfg_topo_date = "genTime=".$date."-10:00";
                                        my $new_epfg_topo_date = "genTime=".$today;
                                        print "$epfg_topo_date\n";
                                        
                                        if ($genflag =~ m/GenTopology/){
                                        
                                        open EPFGFILE1, '<', $epfgpropertiesfile or die "Could not open '$epfgpropertiesfile', No such file found in the provided path $!\n";
                                        
                                                my @epfg_topodate = <EPFGFILE1>;
                                                close(EPFGFILE1);

                                                my @epfg_newtopodate;
                                                foreach(@epfg_topodate) {
                                                $_ =~ s/$epfg_topo_date/$new_epfg_topo_date/g;
                                                push(@epfg_newtopodate,$_);
                                                }

                                                open(EPFGFILE1, ">/eniq/home/dcuser/epfg/config/epfg.properties") || die "File not found";
                                                print EPFGFILE1 @epfg_newtopodate;
                                                close(EPFGFILE1);
                                                #print "success\n";
                                        }
                                        else {
                                        #print "fail\n";
                                        }
                                }
                        }
                        else{
                        #print "FAIL\n";
                        }
                }
        }
        
        epfgdataGeneration();

