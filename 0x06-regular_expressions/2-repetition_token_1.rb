#!/usr/bin/env ruby  
 #This script will search for htn and hbtn 
 puts ARGV[0].scan(/hb{0,1}tn/).join
