#!/bin/bash 
# Script: Ops Challenge 02
# Purpose: Input Path to a folder 
#          Input Permissions to change all the files in that folder
#          Log to a file


# Input the PAth to the file 
read -p "Input the Path to the file: " FILEPATH
# Input the new file permission
read -p "Input new permissions: " FP

#Backup to a file 
chmod $FP $FILEPATH 
echo "$(date +'%Y_%m_%d_%H:%M:%S') : chmod $FP $FILEPATH" >> "script_log.log"

# Display files in folder with delay 
for entry in $FILEPATH
do
  echo "$entry: Permission Change to $FP"
  sleep 1
done
 
