#!/usr/bin/env python3

"""
Gross revenue calculator for Backcast

Pull wind speed, generation, and pricing data on same time axis
Pull peak and off peak hours to filter on
Calculate monthly sum revenue, ave wind speed, ave pricing
for peak and off-peak hours
Print results to stdout and save to file(s) on disk
"""

import pandas as pd
import numpy as np
from windrevenue.peakhours import PeakHours
from windrevenue.align_data import AlignData


class GrossRevenue():
    """
    Generate monthly tables of gross revenue given a data frame of
    aligned (1-year, Jan - Dec) pricing and generation data. Include
    wind speed in the final tables that are printed and written
    to .csv file.
    """

    def __init__(self, aligned_data, peak_hours=None):
        """
        Require aligned pricing and generation data in AlignData obj
        Optionally, accept PeakHours object. Otherwise create one
        using default parameters.d
        """
        if peak_hours is not None:
            self.peak_hours = peak_hours
        else:
            self.peak_hours = PeakHours()
        self.aligned_data = aligned_data

    def add_revenue_column(self, scale=1e-4):
        """
        ALignedData has 3 columns, wind speed, generation, and price
        Append a column with the gross revenue, scaling input power to
        MWh (default 1e-4)
        """
        colnames = list(self.aligned_data)
        pricevar, genvar = colnames[1], colnames[2]
        revenue = scale * self.aligned_data[genvar] * self.aligned_data[pricevar]
        self.aligned_data["Revenue"] = revenue

    def subset_data(self, subset_on="peak"):
        """
        Return a dataframe containing only peak, or off-peak, times
        as determined by the arg "subset_on" which can be "peak" or
        "off-peak", with "peak" as the default. Other times are NaN
        """
        subset_on = subset_on.strip().lower()
        hrsoptions = self.peak_hours.get_peak_hours()  # Peak & off-peak
        # Select peak or off peak hours
        if subset_on == "peak":
            hours = hrsoptions[0]
        elif subset_on == "off-peak":
            hours = hrsoptions[1]
        else:
            raise(UserWarning, "Selection must be peak or off-peak")
        # Construct timeseries of 1, NaN for times included,excluded
        include_times = pd.Series(self.aligned_data.index.hour).isin(hours)
        # Set up time index to match aligned_data so we can mask
        include_times.index = AlignData.get_typical_year()
        include_times.index.names = ["TimeStamp"]
        include_times = include_times.apply(lambda x: 1 if x else np.nan)
        # Mask aligned_data to NaN-out excluded times
        return self.aligned_data.mul(include_times, axis=0)

    def group_data(self, input_df):
        """
        Return a dataframe of the data grouped by month, and hour
        of day (latter is inherent in aligned_data) for a dataframe
        of windspeed, generation, price, and revenue. Average the
        windspeed and price; sum generation and revenue.
        """
        pass

    def save_pretty_table(self, outputfile="sample_output.csv"):
        """
        Save a pretty table of results to outputfile (.csv)
        """
        pass

    def print_pretty_table(self):
        """
        Print a pretty table of results to stdout
        """
        pass




