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

class parse_met_data():

    #  Given a pandas series, return series with outliers replaced by nan
    #  For series with few unique variables, do nothing and return the series
    #  The hepatitis dataset has many columns with 2 or 3 unique variables
    def replace_outliers_with_na(x):
        if len(x.unique()) < 5:
            return x
        xbar = np.mean(x) # Mean, ignoring NA
        xsd = np.std(x) # Standard deivation, ignoring NA
        LL = xbar - 2*xsd # Lower limit for outlier detection
        UL = xbar + 2*xsd # Upper limit for outlier detection
        return x.map(lambda y: y if y > LL and y < UL else np.nan) # Change outliers to NA

    # Given a pandas series x, replace any NA with median of non-NA values
    def replace_na_with_median(x):
        return x.fillna(np.mean(x))

    def parse_met_file(self):
        pass

    def inspect_met_sensor(self):
        pass

    def change_met_sensor(self):
        pass

