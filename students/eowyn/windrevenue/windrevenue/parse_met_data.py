#!/usr/bin/env python3

""" 
Met data handling for Backcast

Read observational meteorological data
Determine the highest wind speed sensor and extract data
Drop other columns
Replace missing values with NaN
Drop rows with any NaN
Resample time series to hourly
"""

import pandas as pd
import numpy as np
import os


class MetData():

    # Round float value n to nearest precision
    # https://stackoverflow.com/questions/4265546/python-round-to-nearest-05
    def round_to_05(n, precision=0.5):
        correction = 0.5 if n >= 0 else -0.5
        return int( n/precision+correction ) * precision

    def parse_met_file(self):
        """
        Read met data file, store in data frame and store sensor choice
        """
        self.metdf = self.read_met_data()
        self.sensorInfo = self.parse_sensor_information(self.metdf)
        self.windVar = self.locate_highest_anemometer(self.sensorInfo)


    def get_met_timeseries(self):
        # Return the current working time series in native format
        # with nan rows dropped
        currentdf = pd.DataFrame(self.metdf[self.windVar])
        # Replace invalid data with nan
        currentdf.iloc[:, 0] = currentdf.iloc[:, 0].replace(-99.99, np.nan)
        # Drop rows with missing values
        currentdf = currentdf.dropna(axis=0, how='any')
        return currentdf

    def read_met_data(self, fname=os.path.abspath("windrevenue/sample_data/sample_met.txt")):
        # Use sample data, or else read data from file provided by user
        filename = None
        filename = input("Full path to met file (leave blank to use sample data):\n")
        fname = filename or fname
        print("Reading met file: ", fname)
        metdf = pd.read_table(fname, skiprows=1,
                              index_col=0,
                              parse_dates=True,
                              infer_datetime_format=True)
        metdf.index.name = 'DateTime'
        return metdf

    def parse_sensor_information(self, metdf):
        """
        Parse column names to determine sensor info: measurement height,
        sensor type, and field type (mean, max, etc.) handling the existance
        of fields like "St Dev" that need to be combined to "StDev" and
        retaining only the numeric component of the sensor height (in m or ft)
        """
        colnames = list(metdf)
        sensorInfo = []
        for col in colnames:
            sensor = col.split(' ')
            unitIndex, conversion = sensor[0].lower().find('m'), 1.0
            if unitIndex == -1:
                unitIndex, conversion = sensor[0].lower().find('ft'), 0.3048
            sensorInfo.append([float(sensor[0][:unitIndex]) * conversion,
                               sensor[1],
                               "".join(sensor[2:])])
        return sensorInfo

    def locate_highest_anemometer(self, sensorInfo):
        # Locate column name of highest mean anemometer sensor
        windAve = [(item[2] == "Mean" and item[1] == "Anemometer")
                   for item in sensorInfo]  # Boolean where field is ave wind
        heights = [item[0] for item in sensorInfo]
        meanWindHeights = [a * b for a, b in zip(windAve, heights)]
        mxInd = meanWindHeights.index(max(meanWindHeights))
        colnames = list(self.metdf)
        return colnames[mxInd]

    def inspect_met_sensor(self):
        # Print the current selection of met sensor
        print("Current anemometer: ", self.windVar)

    def print_sensor_info(self):
        print("All Sensors:")
        menu = dict(zip(range(len(self.sensorInfo)), self.sensorInfo))
        for sensor, number in menu.items():
            print("{} ({})".format(sensor, number))

    def change_met_sensor(self):
        """
        Prompt user to choose a sensor from among all available
        Update self.windvar and return time series of chosen sensor.
        """
        print("SELECT FROM:\n")
        self.print_sensor_info()
        choice = input("\n>>")
        menu = dict(zip(range(len(self.sensorInfo)), self.sensorInfo))
        if int(choice) in menu.keys():
            colnames = list(self.metdf)
            self.windVar = colnames[int(choice)]
            print("Using sensor: ", self.windVar)

    def calculate_power_generation(self):
        """
        Construct a time series (dataframe) of power generation.
        Create 10-min power generation data from
        10-min wind speed and the power curve dict
        Otherwise, round windspeed to the nearest 0.5m/s and select generation
        value from power curve dictionary. 
        """
        metdf = self.get_met_timeseries().applymap(self.round_to_05)
        # Create a new column with the power generation. IF the map fails 
        # to find a matching wind speed, the Generation is nan
        metdf["Generation"] = metdf.iloc[:,0].map(self.pct.power_curve)
        # Replace nan generation with zero for ws < cut-int or > cut-out
        metdf["Generation"] = metdf["Generation"].replace(np.nan, 0.0)
        return metdf

    def get_power_generation(self):
        """
        Return time series of the power generation
        """
        return self.metdf.iloc[:,"Generation"]

    def get_wind_and_generation(self):
        """
        Combine generation and one wind speed time series into 
        data frame for use outside this module.
        """
        wind = self.get_met_timeseries()
        gen = self.get_power_generation()
        return pd.concat([wind, gen])


