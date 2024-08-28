#!/usr/bin/perl

use warnings;
use strict;
no warnings 'uninitialized';

#my $directory = '/proj/wipba/stats_eniq/CHECKIN_FILES_ALL';
my $directory = $ARGV[0];
#my $dest_dir = '/proj/wipba/stats_eniq/CHECKIN_FILES';
my $dest_dir = $ARGV[1];
my $ES_LIST_FILE = "/proj/eiffel004_config_fem160/eiffel_home/bin/.ES_TOTAL_PKG_LIST.txt";

my @List;
my @files;
my $name;

open(my $fh, "<", "$ES_LIST_FILE") or die "Failed to open file: $!\n";
while(<$fh>) { 
    chomp; 
    push @List, $_;
} 
close $fh;
#print join ",", @List;

#opendir(DIR,$directory);
#@files = grep { $_ ne '.' && $_ ne '..' } readdir(DIR);
#closedir(DIR);

@files = `ls $directory`;
foreach(@files)	
{
	#print "$_\n";
	$name = (split /_R[0-9]/, "$_")[0] ;
	if(grep /$name/, @List)
	{
        chomp($name);
        my $trans_file="$directory/$_";
        #print "File transfer is $trans_file \n \n";
        chomp($trans_file);
        system("/bin/cp -rf $trans_file $dest_dir");
		print "Copied the file $trans_file to directory $dest_dir \n";
	}
	else 
	{
		print "This TP $name doesn't EXISTS in the ES_TOTAL_PKG_LIST , Please check it once \n";
	}
	`chmod 777 $dest_dir/*`;
}

