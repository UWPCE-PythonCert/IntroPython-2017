#!/usr/bin/env python3

""" 
Peak hours handling for Backcast

Get and set peak hours
Get and set non-peak hours 
"""
import pandas as pd

class PeakHours():

    def __init__(self):
        self.peakHours = pd.Series([i for i in range(0, 12)])  # 0..11
        self.offPeakHours = pd.Series([i for i in range(12, 24)])  # 12..23

    def print_peak_hours(self):
        print("Peak hours: ", self.peakHours)
        print("Off-Peak hours: ", self.offPeakHours)

    def get_peak_hours(self):
        return (self.peakHours, self.offPeakHours)

    def set_peak_hours(self):
        """
        Ask user to specify peak hours. Parse the input.
        Off-Peak are all the
        other hours on 24-hour basis. Set attributes for peak/offPeakHours
        """
        choice = input("Enter peak hours (1-24) as list or range e.g.1,3,5-9\n")
        parsed = [i.split('-') for i in choice.split(',')]
        print(parsed)
        flat = set()
        print(flat)
        for elem in parsed:
            if len(elem) == 2:
                inclusive = set([i for i in range(int(elem[0]),int(elem[1])+1)])
                flat = flat.union(inclusive)
            else:
                flat.update([int(elem[0])])
        allhours = [i + 1 for i in range(0, 24)]
        self.offPeakHours = list(set(allhours).difference(flat))
        self.peakHours = list(flat)





