#!/usr/bin/env python
import sys
from windrevenue.parse_met_data import MetData as met
from windrevenue.power_curve_tool import PowerCurve as pct
from windrevenue.electricity_pricing import ElectricityPricing as pricing
from windrevenue.peakhours import PeakHours as peak
from windrevenue.revenue import GrossRevenue as rev
from windrevenue.align_data import AlignData as ad


class UI():

    def __init__(self, met=met, pct=pct, pricing=pricing):
        """
        Instantiate classes to store state related to
        different data and funcionality.
        """
        if met is not None:
            self.met = met
        else:
            self.met = met()
        if pct is not None:
            self.pct = pct
        else:
            self.pct = pct()
        if pricing is not None:
            self.pricing = pricing
        else:
            self.pricing = pricing()

        self.peak = peak()
        self.ad = ad()
        self.rev = rev(self.ad)


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
            arg_dict = {"1": self.read_met_file,
                        "2": self.read_powercurve_file,
                        "3": self.read_pricing_file,
                        "4": self.set_peakhours,
                        "5": self.calc_revenue,
                        "6": self.quit_code}
            prompt_string = """Calculate gross revenue from a single turbine: \n
            (1) Choose/Modify Meteorological Time Series\n
            (2) Add/Select Power Curve from Repository\n
            (3) Choose/Modify Electricity Pricing Data \n
            (4) Choose/Modify Peak/Off-Peak Hours\n
            (5) Calculate Peak & Off-Peak Monthly Revenue Table\n
            (6) Quit\n>"""
            self.run_interactive_loop(arg_dict, prompt_string)

    def read_met_file(self):
        self.met.parse_met_file(self.met)

    def read_powercurve_file(self):
        self.pct.load_new(self.pct)

    def read_pricing_file(self):
        self.pricing.load_new(self.pricing)

    def set_peakhours(self):
        self.peak.set_peak_hours()

    def calc_revenue(self):
        self.rev.calculate_gross_revenue()

