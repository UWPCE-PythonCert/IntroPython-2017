#!/usr/bin/env python3

import pandas as pd
import numpy as np


class MetData():

    """
    Met data handling

    Read observational meteorological data
    Determine the highest wind speed sensor and extract data
    Drop other columns
    Replace missing values with NaN
    Drop rows with any NaN
    Resample time series to hourly
    Use associated power curve to calculate gross revenue.
    """

    def __init__(self, fname=None, pct=None):
        if pct is not None:
            self.pct = pct
        if fname is not None:
            self.parse_met_file(fname)

    def setPct(self, pct):
        self.pct = pct

    def parse_met_file(self, fname=None):
        """
        Read met data file, store in data frame and store sensor choice
        """
        if fname is None:
            from windrevenue.UI import UI
            prompt_string = "Please specify the met time series file:\n"
            fname = UI.get_user_input(prompt_string)
        try:
            self.load_new(fname)
        except FileNotFoundError:
            print("File not found, no data loaded.")
            return
        except TypeError:  # TODO
            print(self, fname)
            raise
        self.sensorInfo = self.parse_sensor_information(self.metdf)
        self.windVar = self.locate_highest_anemometer(self.sensorInfo)

    def load_new(self, fname):
        # Read met data from file into data frame self.metdf
        print("Reading met file: ", fname)
        metdf = pd.read_table(fname, skiprows=1,
                              index_col=0,
                              parse_dates=True,
                              infer_datetime_format=True)
        metdf.index.name = 'DateTime'
        self.metdf = metdf

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

    def get_met_timeseries(self):
        # Return the current working time series in native format
        # with nan rows dropped
        currentdf = pd.DataFrame(self.metdf[self.windVar])
        # Replace invalid data with nan
        currentdf.iloc[:, 0] = currentdf.iloc[:, 0].replace(-99.99, np.nan)
        # Drop rows with missing values
        currentdf = currentdf.dropna(axis=0, how='any')
        return currentdf

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

    def get_wind_and_generation(self):
        """
        Construct a time series (dataframe) of power generation.
        Create 10-min power generation data from
        10-min wind speed and the power curve dict
        Otherwise, round windspeed to the nearest 0.5m/s and select generation
        value from power curve dictionary.
        """
        met_timeseries = self.get_met_timeseries()
        pcdf = self.pct.power_curve

        pcdf = pcdf.append(pd.DataFrame({'WS': (self.get_met_timeseries()[(self.windVar)])}), True)
        power_lookup = pd.Series(index=pcdf.WS, data=pcdf.Pwr.values).interpolate(method='index')
        subset = power_lookup.tail(len(power_lookup) - len(self.pct.power_curve))

        subset_df = pd.DataFrame(subset)
        subset_df.index = met_timeseries.index

        generated = pd.concat([met_timeseries, subset_df], axis=1)
        generated.columns = [self.windVar, 'Generation']

        return generated


