#!/usr/bin/env python
import sys
from windrevenue.parse_met_data import MetData as met
from windrevenue.power_curve_tool import PowerCurve as pct
from windrevenue.electricity_pricing import ElectricityPricing as pricing
from windrevenue.peakhours import PeakHours as peak
from windrevenue.revenue import GrossRevenue as rev
from windrevenue.align_data import AlignData as ad


class UI():

    """
    Top level user interface for wind revenue gross generation.
    The user must load a met tower time series, a power curve file,
    and an electricity pricing file. These can be loaded in any order.

    The user may optionally set peak and off peak pricing hours. The
    default is 0-11 peak, 12-23 off peak.

    Once the input data are provided, the gross revenue can be caculated.
    The calculation is performed on a monthly and hourly basis.
    The data is saved in full precision to a pair of csv files,
    GrossRevenue-PeakHrs.csv and GrossRevenue-OffPeakHrs.csv
    and it is output to stdout in a pretty tabular format.

    The UI will start when windrevenue is first run. Sample data
    may be found in sample_data/*txt
    """

    def __init__(self, metin=None, pctin=None, pricingin=None):
        """
        Instantiate classes to store state related to
        different data and funcionality.
        """
        if metin is not None:
            self.met = metin
        else:
            self.met = met()
        if pctin is not None:
            self.pct = pctin
        else:
            self.pct = pct()
        if pricingin is not None:
            self.pricing = pricingin
        else:
            self.pricing = pricing()

        self.peak = peak()


    def quit_code(self):
        sys.exit()

    def return_to_menu(self):
        ''' Return True to trigger exit out of sub-loop'''
        return True

    @staticmethod
    def get_user_input(prompt_string):
        ''' Print a prompt_string, return keyboard input if no exceptions'''
        try:
            answer = input(prompt_string)
        except (EOFError, KeyboardInterrupt, TypeError):
            return None
        else:
            return answer

    def select_action(self, arg_dict, answer):
        ''' Execute an action from arg_dict that corresponds to answer.
        Return None if action was executed and False if an error occurs'''
        try:
            return arg_dict[answer]()
        except (KeyError):
            return False

    def run_interactive_loop(self, arg_dict, prompt_string):
        while True:
            answer = self.get_user_input(prompt_string)
            if answer:
                result = self.select_action(arg_dict, answer)
                if result:
                    return True

    def mainloop(self):
        '''
        main interactive loop
        '''
        while True:
            arg_dict = {"1": self.read_powercurve_file,
                        "2": self.read_met_file,
                        "3": self.read_pricing_file,
                        "4": self.set_peakhours,
                        "5": self.calc_revenue,
                        "6": self.quit_code}
            prompt_string = """Calculate gross revenue from a single turbine: \n
            (1) Load Power Curve File\n
            (2) Load Meteorological Time Series\n
            (3) Load Electricity Pricing Data \n
            (4) Select Peak/Off-Peak Hours\n
            (5) Calculate Peak & Off-Peak Monthly Revenue Table\n
            (6) Quit\n>"""
            self.run_interactive_loop(arg_dict, prompt_string)

    def read_powercurve_file(self):
        self.pct.load_new()
        if self.met is not None:
            # associate new power curve with met data
            self.met.setPct(self.pct)

    def read_met_file(self):
        self.met.parse_met_file()
        if self.pct is not None:
            # associate new met data with power curve
            self.met.setPct(self.pct)

    def read_pricing_file(self):
        self.pricing.load_new()

    def set_peakhours(self):
        self.peak.set_peak_hours()

    def calc_revenue(self):
        self.ad = ad(price_data=self.pricing, met_data=self.met)
        self.rev = rev(self.ad)
        self.rev.calculate_gross_revenue()

    def get_powercurve_object(self):
        return self.pct
