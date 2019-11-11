import sys
import time


from pickler import *

# App sets times, removes times, checks times
# TODO: get times from pickle file
# TODO: remove overdue times
# TODO: pick better variable names so it's more obvious what's going on
# apps should be new_apps, and times should be ban_times


class Setter:
    def __init__(self, args):
        try:
            self.timestamp = time.time() + int(args[-1])*60
            self.apps = args[:-1]
        except ValueError:
            self.timestamp = time.time()
            self.apps = []
        self.times = loader("times")

    def set_new_times(self):
        """
        Dumps the new times into pickle file, to be read by Nuclear.
        """
        dumper(self.times, "times")

    def get_new_times(self):
        """
        :returns: Returns dictionary with the app name (key) and the
        time it should be blocked until (value).
        """
        return {app: self.timestamp for app in self.apps}

    def update_times(self):
        new_apps = list(filter(
            lambda app: self.timestamp > self.times.get(app, default=0),
            self.apps))
        for app in new_apps:
            self.times[app] = self.timestamp



