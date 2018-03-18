#!/usr/bin/env python3


import pandas as pd


class PowerCurve():

    """
    Power curve handling

    Read new power curves

    To be implemented:
    Keep track of previously used power curves as txt files
    Print a list of available power curves
    Read and write power curves from/to files
    """

    def __init__(self, fname=None, data=None):
        if fname is not None and data is not None:
            raise(ValueError("Specify filename or data value, not both"))
        if fname is None:
            self.power_curve = data
        else:
            self.load_new(fname)

    def print_current(self):
        print("Current Power Curve:\n")
        for windbin, generation in self.power_curve.items():
            print("{} ({})".format(windbin, generation))

    def choose_existing(self):
        print("Not yet implemented")

    def list_existing(self):
        print("not yet implemented")

    def load_new(self, fname=None):
        """
        Read power curve from file, either default or user-provided.
        Store power curve as dict in self.power_curve
        """
        if fname is None:
            from windrevenue.UI import UI
            fname = UI.get_user_input("Please provide a power curve file:\n")
        print("Reading power curve file: ", fname)
        try:
            self.power_curve = pd.read_table(fname, sep="\t")
        except FileNotFoundError:
            print("File not found, no data loaded.")
            return

    def get_current_pc(self):
        """
        Return the current power curve
        """
        return self.power_curve
