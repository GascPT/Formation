#!/bin/bash
# Script: Ops Challenge 04
# Purpose: Clearing Logs


sizea=$(du -lh /var/log/syslog) 
stringarraya=($sizea)
echo "Syslog File size : ${stringarraya[0]}"

sizeb=$(du -lh /var/log/wtmp) 
stringarrayb=($sizeb)
echo "wTmp File size : ${stringarrayb[0]}"

zip -q syslog.zip /var/log/syslog
zip -q wtmp.zip /var/log/wtmp
echo "Compressed the File: syslog.zip"
echo "Compressed the File: wtmp.zip"

timestamp=$(date +"%Y%m%d%H%M%S")

mv syslog.zip "syslog_$timestamp.zip"
mv wtmp.zip "wtmp_$timestamp.zip"
backupdirectory="./backups"

if [ ! -d $backupdirectory ]
then
	mkdir $backupdirectory
	sudo chown -R $(whoami) $backupdirectory
fi

mv syslog_* $backupdirectory
mv wtmp_* $backupdirectory


echo "$(ls -lh $backupdirectory/syslog_$timestamp.zip) | Original Size: ${stringarraya[0]}"
echo "$(ls -lh $backupdirectory/wtmp_$timestamp.zip) | Original Size: ${stringarrayb[0]}"