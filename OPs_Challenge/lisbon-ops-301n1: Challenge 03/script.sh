#!/bin/bash 
# Script: Ops Challenge 03
# Purpose: Loop Menu


while :
do
    clear
    cat<<EOF
    ==============================
    Menu
    ==============================
    Please enter your choice:

    For printing a "Hello world"  (1)
    For ping the loopback address (2)
    For print IP Information      (3)
           (Q)uit
    ------------------------------
EOF
    read -n1 -s
    case "$REPLY" in
    "1")  echo "Hello World" ;;
    "2")  ping -c 4 127.0.0.1 ;;
    "3")  ifconfig ;;
    "Q")  exit                      ;;
    "q")  exit   ;; 
     * )  echo "invalid option"     ;;
    esac
    sleep 2
done

