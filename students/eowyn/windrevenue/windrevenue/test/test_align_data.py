#!/usr/bin/env python3

import os
import sys
import pytest
from windrevenue.align_data import AlignData
from windrevenue.electricity_pricing import ElectricityPricing
from windrevenue.parse_met_data import MetData
from windrevenue.power_curve_tool import PowerCurve


dirname = os.path.dirname(sys.modules["windrevenue"].__file__)
sample_data = os.path.join(dirname, "sample_data")
met_file_1 = os.path.join(sample_data, "sample_met.txt")
met_file_2 = os.path.join(sample_data, "sample_met2.txt")
price_file = os.path.join(sample_data, "sample_pricing.txt")
price_file2 = os.path.join(sample_data, "sample_pricing2.txt")
power_curve_file = os.path.join(sample_data, "power_curve.txt")

@pytest.fixture
def sample_data():
    power_curve = PowerCurve(fname=power_curve_file)
    price_data = ElectricityPricing(fname=price_file)
    met_data = MetData(fname=met_file_1, pct=power_curve)

    align_data = AlignData(price_data=price_data, met_data=met_data)
    return align_data

@pytest.fixture
def sample_data2():
    power_curve = PowerCurve(fname=power_curve_file)
    price_data = ElectricityPricing(fname=price_file2)
    met_data = MetData(fname=met_file_2, pct=power_curve)

    align_data = AlignData(price_data=price_data, met_data=met_data)
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


class TestAlignData():

    def test_align_data_not_empty(self, sample_data):
        sample_data.resample_timeseries()
        assert sample_data.power_hour is not None
        assert sample_data.met_hour is not None

    def test_resample_no_nan(self, sample_data):
        sample_data.resample_timeseries()
        q = sample_data.power_hour.isna().sum()
        print(q)
        assert q.sum() == 0
        q = sample_data.met_hour.isna().sum()
        print(q)
        assert q.sum() == 0

    def test_aligned_data_size2(self, sample_data2):
        q = sample_data2.align_data()
        assert q.shape == (8760, 3)

    def test_aligned_data_size(self, sample_data):
        q = sample_data.align_data()
        print(q.head())
        print(q.tail())
        print(q.shape)
        assert q.shape == (8760, 3)

    def test_start_end_aligned_data1(self, sample_data):
        q = sample_data.align_data()
        assert q.index[0].dayofyear == 1
        assert q.index[-1].dayofyear == 365

    def test_start_end_aligned_data2(self, sample_data2):
        q = sample_data2.align_data()
        assert q.index[0].dayofyear == 1
        assert q.index[-1].dayofyear == 365

    def test_data_nonans1(self, sample_data):
        q = sample_data.align_data().isna().sum()
        print(sample_data.align_data().isna().sum())
        assert q.sum() == 0

    def test_data_nonans2(self, sample_data2):
        q = sample_data2.align_data().isna().sum()
        print(sample_data2.align_data().isna().sum())
        assert q.sum() == 0







