#!/usr/bin/env python3

import pandas as pd


class ElectricityPricing():

    """
    Electricity pricing handling

    Read electricity files
    Select columns as desired
    Average across columns as desired
    Re-sample time series to hourly
    """

    def __init__(self, fname=None):
        if fname is not None:
            self.load_new(fname)

    def load_new(self, fname=None):
        """
        Read pricing time series data from file, provided or default.
        Store all pricing data as data frame, and select first
        substation as the powerVar.
        """
        if fname is None:
            from windrevenue.UI import UI
            fname = UI.get_user_input("Please specify pricing file:\n")

        print("Reading electicity pricing file: ", fname)
        try:
            powerdf = pd.read_table(fname, skiprows=0,
                                    index_col=0,
                                    parse_dates=True,
                                    infer_datetime_format=True)
        except FileNotFoundError:
            print("File not found, no data loaded.")
            return
        powerdf.index.name = 'DateTime'
        colnames = list(powerdf)
        self.powerdf = powerdf
        self.powerVar = colnames[0]

    def show_pricing_field(self):
        # Print the current selection of substation
        print("Current substation: ", self.powerVar)

    def get_pricing_field(self):
        # Return the current working time series in native format
        currentdf = pd.DataFrame(self.powerdf[self.powerVar])
        return currentdf

    def print_substation_info(self):
        print("All Substations:")
        colnames = list(self.powerdf)
        menu = dict(zip(range(len(colnames)), colnames))
        for sensor, number in menu.items():
            print("{} ({})".format(sensor, number))

    def set_pricing_field(self):
        """
        Prompt user to choose a sensor from among all available
        Update self.windvar and return time series of chosen sensor.
        """
        print("SELECT FROM:\n")
        colnames = list(self.powerdf)
        self.print_substation_info()
        choice = input("\n>>")
        menu = dict(zip(range(len(colnames)), colnames))
        if int(choice) in menu.keys():
            self.powerVar = colnames[int(choice)]
            print("Using substation: ", self.powerVar)
