#!/bin/python
import psutil
import subprocess

# Get system CPU times
cpu_times = psutil.cpu_times()

# Create a string with the required information
cpu_info = f"Time spent by normal processes executing in user mode: {cpu_times.user}\n" \
           f"Time spent by processes executing in kernel mode: {cpu_times.system}\n" \
           f"Time when system was idle: {cpu_times.idle}\n" \
           f"Time spent by priority processes executing in user mode: {cpu_times.nice}\n" \
           f"Time spent waiting for I/O to complete: {cpu_times.iowait}\n" \
           f"Time spent for servicing hardware interrupts: {cpu_times.irq}\n" \
           f"Time spent for servicing software interrupts: {cpu_times.softirq}\n" \
           f"Time spent by other operating systems running in a virtualized environment: {cpu_times.steal}\n" \
           f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {cpu_times.guest}\n"

# Stretch Goals

# Save the information to a text file
with open('cpu_info.txt', 'w') as f:
    f.write(cpu_info)

# Email the text file using Sendmail
to_address = 'your_email_address'
subject = 'CPU Information'
body = 'Please find attached the CPU information.'
sendmail_command = 'echo "{}" | mail -s "{}" -a cpu_info.txt {}'.format(body, subject, to_address)
subprocess.call(sendmail_command, shell=True)
