import sys
import time


from pickler import *

# App sets times, removes times, checks times
# TODO: get times from pickle file
# TODO: remove overdue times


class Setter:
    def __init__(self, args):
        try:
            self.minutes = int(args[-1])
            self.apps = args[:-1]
        except ValueError:
            self.minutes = 0
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
        return {app: time.time() + self.minutes*60 for app in self.apps}

    def update_times(self):
        # TODO: update times. How this works is you get the times (duh),
        #  if the new apps are already in the file, check if the new times
        #  are later, then update. Add new times as well.
        pass



