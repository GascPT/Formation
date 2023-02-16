#!/bin/bash 
# Script: Ops Challenge 01
# Purpose: Backup the syslog file 
#          Append the timestamp on the file 

# Variables
IFL=/var/log/syslog


cp $IFL .
echo "Copying the File"
mv syslog "syslog_$(date +'%Y_%m_%d_%H:%M:%S')"
echo "Append Time to File name"


