#!/usr/bin/env python
import sys
from windrevenue.parse_met_data import parse_met_data as met
from windrevenue.power_curve_tool import power_curve_tool as pct
from windrevenue.electricity_pricing import electricity_pricing as pricing
from windrevenue.peakhours import peakhours as peak
from windrevenue.revenue import revenue as rev


class UI():

    def __init__(self):
        """
        Instantiate classes to store state related to
        different data and funcionality.
        """
        self.met = met()
        self.pct = pct()
        self.pricing = pricing()
        self.peak = peak()
        self.rev = rev()

    def quit_code(self):
        sys.exit()

    def return_to_menu(self):
        ''' Return True to trigger exit out of sub-loop'''
        return True

    def get_user_input(self, prompt_string):
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
                        return

    def mainloop(self):
        ''' 
        main interactive loop
        '''
        arg_dict = {"1": self.met_loop,
                    "2": self.powercurve_loop,
                    "3": self.pricing_loop,
                    "4": self.peakhours_loop,
                    "5": self.revenue_loop,
                    "6": self.quit_code}
        prompt_string = """Calculate gross revenue from a single turbine: \n
        (1) Choose/Modify Meteorological Time Series\n
        (2) Add/Select Power Curve from Repository\n
        (3) Choose/Modify Electricity Pricing Data \n
        (4) Choose/Modify Peak/Off-Peak Hours\n
        (5) Calculate Peak & Off-Peak Monthly Revenue Table\n
        (6) Quit\n>"""
        self.run_interactive_loop(arg_dict, prompt_string)

    def met_loop(self):
        '''
        Parse meteorological time series files
        '''
        arg_dict = {"1": self.met.parse_met_file,
                    "2": self.met.inspect_met_sensor,
                    "3": self.met.change_met_sensor,
                    "4": self.return_to_menu}
        prompt_string = """Select one:\n
        (1) Load meteorological time series file\n
        (2) Inspect current met sensor selected for calculations\n
        (3) Change current met sensor selection for calculations\n
        (4) Return to the main menu\n"""
        self.run_interactive_loop(arg_dict, prompt_string)

    def powercurve_loop(self):
        '''
        Load power curve data new or from existing
        '''
        arg_dict = {"1": self.pct.list_existing,
                    "2": self.pct.choose_existing,
                    "3": self.pct.load_new,
                    "4": self.return_to_menu}
        prompt_string = """Select one:\n
        (1) View available power curves\n
        (2) Select from available power curves\n
        (3) Load new power curve from file\n
        (4) Return to the main menu\n"""
        self.run_interactive_loop(arg_dict, prompt_string)

    def pricing_loop(self):
        '''
        Parse electricity pricing time series files
        '''
        arg_dict = {"1": self.pricing.parse_pricing_file,
                    "2": self.pricing.get_pricing_field,
                    "3": self.pricing.set_pricing_field,
                    "4": self.return_to_menu}
        prompt_string = """Select one:\n
        (1) Load electricity prices time series file\n
        (2) Inspect current substation selected for calculations\n
        (3) Change current substation selection for calculations\n
        (4) Return to the main menu\n"""
        self.run_interactive_loop(arg_dict, prompt_string)

    def peakhours_loop(self):
        '''
        View and select hours of day (out of 24) that are peak & off-peak
        '''
        arg_dict = {"1": self.peak.get_peak_hours,
                    "2": self.peak.set_peak_hours,
                    "3": self.return_to_menu}
        prompt_string = """Select one:\n
        (1) Review current peak/off peak hour selection\n
        (2) Adjust current peak/off peak hour selection\n
        (3) Return to the main menu\n"""
        self.run_interactive_loop(arg_dict, prompt_string)

    def revenue_loop(self):
        '''
        Calculate 12 month x 2 (peak,off-peak) gross revenue
        Pretty-print tables to screen
        Save tables to files on disk
        '''
        arg_dict = {"1": self.rev.get_gross_revenue,
                    "2": self.return_to_menu}
        prompt_string = """Select one:\n
        (1) Calculate gross revenue with current selections
         and save results to file\n
        (2) Return to the main menu\n"""
        self.run_interactive_loop(arg_dict, prompt_string)