#!/usr/bin/env ruby  
 #the script should output: [SENDER],[RECEIVER],[FLAGS] 
 puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(',')
