#!/usr/bin/env python3

import shutil
import psutil

def disk_usage_check(disk):
    """Check the usage of a specific disk"""
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage / disk_usage.total * 100
    return free > 25

def cpu_usage_check():
    """Check CPU usage is under 75%"""
    usage = psutil.cpu_percent(1)
    return usage < 75

if not cpu_usage_check("/") or not cpu_usage_check():
    print("CPU Usage too high!")
else:
    print("All good, nothing to worry about")