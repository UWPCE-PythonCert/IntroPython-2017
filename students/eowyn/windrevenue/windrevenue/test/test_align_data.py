#!/usr/bin/env python3

import os
import numpy as np
import pytest
from windrevenue.UI import UI
from windrevenue.align_data import AlignData
from windrevenue.electricity_pricing import ElectricityPricing
from windrevenue.parse_met_data import MetData
from windrevenue.power_curve_tool import PowerCurve

met_file_1 = os.path.abspath("sample_data/sample_met.txt")
met_file_2 = os.path.abspath("sample_data/sample_met2.txt")
price_file = os.path.abspath("sample_data/sample_pricing.txt")
power_curve_file = os.path.abspath("sample_data/power_curve.txt")

@pytest.fixture
def sample_data():
    power_curve = PowerCurve(fname=power_curve_file)
    price_data = ElectricityPricing(fname=price_file)
    met_data = MetData(fname=met_file_1, pct=power_curve)

    align_data = AlignData(price_data=price_data, met_data=met_data)
    align_data.resample_timeseries()
    return align_data

@pytest.fixture
def sample_data2():
    power_curve = PowerCurve(fname=power_curve_file)
    price_data = ElectricityPricing(fname=price_file)
    met_data = MetData(fname=met_file_2, pct=power_curve)

    align_data = AlignData(price_data=price_data, met_data=met_data)
    align_data.resample_timeseries()
    return align_data

class InputFeeder():
    def __init__(self, input_lines):
        self.index = 0
        self.input_lines = input_lines

    def get_user_input(self, prompt_string):
        if self.index >= len(self.input_lines):
            return None
        else:
            value = self.input_lines[self.index]
            self.index = self.index + 1
            return value

# def test_align_data_with_ui(capsys):
#     input_lines = ["5", "1", "2", "6"]
#     input_feeder = InputFeeder(input_lines)
#     from unittest import mock
#     import builtins
#     # with capsys.disabled():
#     with mock.patch.object(UI, 'get_user_input', input_feeder.get_user_input):
#         ui = UI()
#         import pytest
#         with pytest.raises(SystemExit) as pytest_wrapped_e:
#             ui.mainloop()
#             assert pytest_wrapped_e.type == SystemExit
#             assert pytest_wrapped_e.value.code == 42
#         captured = capsys.readouterr()
#         assert "Reading power curve file" in captured.out
#         # assert "Thank you, Kenny Powers, for your generosity and recent gift of $1000000.00.\n" == captured.out
#         assert "" == captured.err
#         print(captured.out)

class TestAlignData():

    def test_align_data_not_empty(self,sample_data):
        sample_data.resample_timeseries()
        assert sample_data.power_hour is not None
        assert sample_data.met_hour is not None

    def test_aligned_data_size(self, sample_data2):
        q = sample_data2.align_data()
        print(q.shape)
        assert q.shape == (24390, 3)






