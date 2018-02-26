#!/usr/bin/env python3

""" 
Power curves for Backcast

Keep track of previously used power curves as .json files
Print a list of available power curves
Read new power curves
Read and write power curves from/to .json files
"""
import os
import pandas as pd
import numpy as np

class PowerCurve():

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

    def load_new(self, fname):
        """ 
        Read power curve from file, either default or user-provided.
        Store power curve as dict in self.power_curve
        """
        print("Reading power curve file: ", fname)
        pcdict = dict()
        with open(fname) as f:
            f.readline()
            for line in f:
                entry = (line.strip().split())
                # to do: round the key.... or use numpy array to interpolate
                pcdict[float(entry[0])] = float(entry[1])
        self.power_curve = pcdict

        def get_user_inpt(self, fname=os.path.abspath("windrevenue/sample_data/power_curve.txt")):
            filename = None
            filename = input("Full path to power curve file (leave blank to use sample data):\n")
            fname = filename or fname

    def get_current_pc(self):
        """
        Return the current power curve
        """
        return self.power_curve
