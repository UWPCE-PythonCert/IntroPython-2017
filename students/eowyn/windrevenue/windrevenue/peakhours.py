#!/usr/bin/env python3

import pandas as pd


class PeakHours():

    """
    Peak hours handling.
    Peak hours are used to calculate tables of revenue

    Get and set peak hours
    Get and set non-peak hours
    """

    def __init__(self, peak=None, offpeak=None):
        # PeakHours instances contain series of peak and off peak hours
        # By default those are 0-11 and 12-23, respectively
        # No restriction is made on the hours, but they should be lists
        if peak is not None:
            self.peak_hours = pd.Series(peak)
        else:
            self.peak_hours = pd.Series([i for i in range(0, 12)])  # 0..11
        if offpeak is not None:
            self.off_peak_hours = pd.Series(offpeak)
        else:
            self.off_peak_hours = pd.Series([i for i in range(12, 24)])  # 12..23

    def print_peak_hours(self):
        print("Peak hours: ", self.peak_hours)
        print("Off-Peak hours: ", self.off_peak_hours)

    def get_peak_hours(self):
        return (self.peak_hours, self.off_peak_hours)

    def set_peak_hours(self):
        """
        Ask user to specify peak hours. Parse the input.
        Off-Peak are all the
        other hours on 24-hour basis. Set attributes for peak/off_peak_hours
        """

        choice = input("Enter peak hours (0-23) as list or range e.g.1,3,5-9\n")
        parsed = [i.split('-') for i in choice.split(',')]
        flat = set()
        for elem in parsed:
            if len(elem) == 2:
                inclusive = set([i for i in range(int(elem[0]), int(elem[1])+1)])
                flat = flat.union(inclusive)
            else:
                flat.update([int(elem[0])])
        allhours = [i + 1 for i in range(0, 24)]
        self.off_peak_hours = list(set(allhours).difference(flat))
        self.peak_hours = list(flat)
