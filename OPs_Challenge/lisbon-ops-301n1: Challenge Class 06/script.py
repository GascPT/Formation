#!/bin/python
import os
import subprocess

print("____________________________________________First Command ____________________________________________")
os.system("whoami")
print("____________________________________________Second Command____________________________________________")
os.system("ip a")
print("____________________________________________Third Command____________________________________________")
os.system("lshw -short")






print("With Subprocess")
print("____________________________________________First Command ____________________________________________")
subprocess.run("whoami", shell=True)

print("____________________________________________Second Command____________________________________________")
subprocess.run(['ip', 'a'])

print("____________________________________________Third Command____________________________________________")
subprocess.run(['lshw', '-short'])