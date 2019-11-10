import time
import psutil
import subprocess
import re


class Nuclear:
    def __init__(self, applications, duration=0):
        self.apps = applications
        self.duration = time.time() + duration*60

    def get_pids(self, app_name):
        pids = re.findall('[\d]+', subprocess.check_output(['/usr/local/bin/pidof', app_name]).decode())
        return [int(pid) for pid in pids]

    def get_pid_cmd(self, pid):
        try:
            return psutil.Process(pid).cmdline()
        except (psutil.STATUS_ZOMBIE, psutil.STATUS_STOPPED, psutil.STATUS_DEAD):
            return []

    def is_pid_app(self, pid, app):
         """Returns BOOL. Checks whether the PID belongs to the app"""
         return re.match()

"""
This is too confusing. Instead of converting a procedureal app to a class-based app, it might make more sense
to just start from the ground up.

A class-based nuclear app would do the following:
    1. You pass in 'nuclear' and the apps you wish to blockade, and how long you wish to block them for.
        1. There could be a pickle file that is a dictionary that contains various apps and how long they're blocked until.
    2. The nukes look for the 'pidof' of that app, and kill it.
        1. The nuke is a while loop/monitor. So there is one app that sets the times, and one app that kills the apps.

This is a good framework. So we have two modules, one that sets the times and one that monitors the pickle file.
A setter and a monitor.
Monitor should remove times that have expired.
Setter can be called prompter, and the monitor can be called nuclear.
"""
