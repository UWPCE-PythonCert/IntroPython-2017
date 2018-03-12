#!/usr/bin/env python3

import pandas as pd
import numpy as np
from tabulate import tabulate
from windrevenue.peakhours import PeakHours
from windrevenue.align_data import AlignData


class GrossRevenue():

    """
    Gross revenue calculator

    Generate monthly tables of gross revenue given an object with
    access to a data frame of aligned (1-year, Jan - Dec) pricing and
    generation data -- which is what the code works on.

    Pull peak and off peak hours to filter on. Calculate monthly
    sum revenue, ave wind speed, ave pricing for peak and off-peak hours

    Include wind speed in the final tables that are printed and written
    to .csv files.
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
        self.aligned_data = aligned_data.align_data()

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
            hours = hrsoptions[0]
            print("Selection must be peak or off-peak. Using peak.")
        # Construct timeseries of 1, NaN for times included,excluded
        include_times = pd.Series(self.aligned_data.index.hour).isin(hours)
        # Set up time index to match aligned_data so we can mask
        include_times.index = AlignData.get_typical_year()
        include_times.index.names = ["TimeStamp"]
        include_times = include_times.apply(lambda x: 1 if x else np.nan)
        # Mask aligned_data to NaN-out excluded times
        return self.aligned_data.mul(include_times, axis=0)

    def group_data(self, input_df, methods=[np.mean, np.mean, sum, sum]):
        """
        Return a dataframe of the data grouped by month, and hour
        of day (latter is inherent in aligned_data) for an aligned_data
        of windspeed, generation, price, and revenue. Average the
        windspeed and price; sum generation and revenue. User may also
        adjust the methods as an arg.
        """
        self.method_names = [i.__name__ for i in methods]  # store it
        windname = input_df.columns[0]
        genname = input_df.columns[1]
        pricename = input_df.columns[2]
        revname = input_df.columns[3]
        aggdict = {windname: methods[0],
                   genname: methods[1],
                   pricename: methods[2],
                   revname: methods[3]}
        grouped = input_df.groupby(input_df.index.month).agg(aggdict)
        grouped.index.names = ["Month"]
        return grouped

    def save_grouped_data(self, input_df, outputfile="sample_output.csv"):
        """
        Save a table of results to outputfile (.csv) with
        headers indicating how the variables were aggregated.
        Retain full precision on values
        """
        colnames = list(input_df)
        methodnames = self.method_names
        headers = ', '.join('%s %s' % t for t in
                            zip(methodnames, colnames)).split(',')
        input_df.columns = headers
        input_df.to_csv(outputfile, sep=',')

    def print_pretty_table(self, input_df):
        """
        Print a pretty table of results to stdout
        """
        print(tabulate(input_df, headers='keys'))

    def calculate_gross_revenue(self):
        """
        Calculate monthly grouped values of wind speed, generation,
        price, and gross revenue. Pretty print result to screen, and
        also save full precision to csv file.
        """
        self.add_revenue_column()
        peak = self.subset_data(subset_on="peak")
        offpeak = self.subset_data(subset_on="off-peak")
        peak_grouped = self.group_data(peak)
        offpeak_grouped = self.group_data(offpeak)
        self.save_grouped_data(peak_grouped, 'GrossRevenue-PeakHrs.csv')
        self.save_grouped_data(offpeak_grouped, 'GrossRevenue-OffPeakHrs.csv')
        print("Peak Hours")
        self.print_pretty_table(peak_grouped)
        print("Off-Peak Hours")
        self.print_pretty_table(offpeak_grouped)






