#!/usr/bin/env python3

import pandas as pd


class AlignData():

    """
    Time series alignment for Backcast

    Wind and generation data are high frequency
    Power is lower frequency
    Get a single data frame of both data on same time axis
    for a 1-year period, no leap years by doing the following:

    Resample all time series to hourly
    Remove Feb 29 if it exists
    Determine if there is any overlap, and if there is 1 year of overlap
    If there is 1 year of overlap, truncate data to that year
    If not, calculate a typical year from all available data
    Handle time axes at each step
    Return a single data frame of 1 year of aligned hourly data
    """

    @staticmethod
    def get_typical_year():
        # Construct a dummy TimeStamp index for the typical year
        return pd.date_range('2015-01-01', periods=8760, freq='H')

    def __init__(self, price_data=None, met_data=None):
        self.pricing = price_data
        self.met = met_data

    def resample_timeseries(self, timestep='60min'):
        """
        Resample met, generation, and power pricing data to hourly
        TO DO: Handle missing vals introduced by re-indexing better
        """
        repwr = self.pricing.get_pricing_field().resample(timestep).mean()
        self.power_hour = repwr.bfill()
        remet = self.met.get_wind_and_generation()
        remet = remet.resample(timestep).mean()
        self.met_hour = remet.bfill()

    def determine_overlap(self):
        # Check if there of overlap between generation and pricing data
        mstart, mend = self.met_hour.index.min(), self.met_hour.index.max()
        pstart, pend = self.power_hour.index.min(), self.power_hour.index.max()
        if mstart <= pstart:
            print("met data starts first")
            if mend <= pstart:
                print("met data starts and ends before power data. No overlap")
                overlap = False
            else:
                print("met data starts first but doesn't end til after power starts")
                overlap = True
        else:
            print("power data starts first")
            if pend <= mstart:
                print("pwr data stars and ends before met data. No overlap")
                overlap = False
            else:
                print("pwr data starts first but doesn't end til after met starts")
                overlap = True
        return overlap

    def determine_amt_overlap(self):
        """
        Calculate how much overlap exists between the met and power
        time series, and return True if it is at least 1 year,
        else return False
        """
        timesInCommon = self.met_hour.index.intersection(self.power_hour.index)
        enough = timesInCommon.max() - timesInCommon.min() >= pd.Timedelta('360 days')
        return enough

    def calculate_same_year(self):
        """
        For cases where there is a full year of overlapping data,
        truncate met and pwr data to this period.
        """
        mstart, mend = self.met_hour.index.min(), self.met_hour.index.max()
        pstart, pend = self.power_hour.index.min(), self.power_hour.index.max()
        self.met_hour = self.met_hour.truncate(before=min(mstart, pstart),
                                               after=max(mend, pend))
        self.power_hour = self.power_hour.truncate(before=min(mstart, pstart),
                                                   after=max(mend, pend))

    def calculate_typical_year(self):
        """
        If not enough overlap, calculate "typical year" for met and pwr.
        At this point, the datetime axis is no longer available.
        We will deal with leap-years then re-create the TimeStamp index.
        """
        self.met_yr = self.met_hour.groupby([self.met_hour.index.month,
                                             self.met_hour.index.day,
                                             self.met_hour.index.hour]).mean()
        self.pwr_yr = self.power_hour.groupby([self.power_hour.index.month,
                                               self.power_hour.index.day,
                                               self.power_hour.index.hour]).mean()
        self.remove_leap_day()
        typical_year = self.get_typical_year()
        self.met_yr.index = typical_year
        self.met_yr.index.names = ["TimeStamp"]
        self.pwr_yr.index = typical_year
        self.pwr_yr.index.names = ["TimeStamp"]


    def remove_leap_day(self):
        """
        Deal with leap years from hourly dataframe. 
        A normal year has 8760 hours, and a leap year
        has 8784; hours 1416 through 1439, inclusive, are Feb 29. 
        Drop all Feb 29 rows:
        temp2 = temp.drop(temp.index[1416:1440], axis = 0)
        """
        if len(self.met_yr.index) == 8784:
            print("removing leap day from met year")
            self.met_yr = self.met_yr.drop(self.met_yr.index[1416:1440], axis=0)
        if len(self.pwr_yr.index) == 8784:
            print("removing leap day from power year")
            self.pwr_yr = self.pwr_yr.drop(self.pwr_yr.index[1416:1440], axis=0)

    def align_data(self):
        """
        Determine if there is a year of overlapping data, else,
        calculate a typical year of data. Return single data frame
        of met and power on same time axis.
        """
        self.resample_timeseries()
        if self.determine_overlap() and self.determine_amt_overlap():
            print("Calcuating Concurrent Year")
            self.calculate_same_year()
            self.calculate_typical_year()
        else:
            print("Calcutating Typical Year")
            self.calculate_typical_year()
        return pd.concat([self.met_yr, self.pwr_yr], axis=1)

