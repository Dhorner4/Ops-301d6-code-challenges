#!/usr/bin/env python3
#Script: Ops 301 Class 11 Ops Challenge Solution
# Author: Dericus Horner
# Date of latest revision:03/27/2023
# Assistance from Chat GPT

# Main
# Library interface for retrieving system info
import psutil

# Using the cpu_times() function of the psutil library to get a nametuple
cpu_times = psutil.cpu_times()

# The following print the amount of time spent for each action
print("Time spent by normal processes executing in user mode:", cpu_times.user)
print("Time spent by processes executing in kernel mode:", cpu_times.system)
print("Time when system was idle:", cpu_times.idle)
print("Time spent by priority processes executing in user mode:", cpu_times.nice)
print("Time spent waiting for I/O to complete:", cpu_times.iowait)
print("Time spent for servicing hardware interrupts:", cpu_times.irq)
print("Time spent for servicing software interrupts:", cpu_times.softirq)
print("Time spent by other operating systems running in a virtualized environment:", cpu_times.steal)
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", cpu_times.guest)
