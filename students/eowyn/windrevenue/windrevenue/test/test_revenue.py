#!/usr/bin/env python3

import os
import pandas as pd
import pytest
from math import isclose
from windrevenue.revenue import GrossRevenue
from windrevenue.peakhours import PeakHours
from windrevenue.align_data import AlignData
from windrevenue.electricity_pricing import ElectricityPricing
from windrevenue.parse_met_data import MetData
from windrevenue.power_curve_tool import PowerCurve

peak_default = pd.Series([i for i in range(0, 12)])
off_peak_default = pd.Series([i for i in range(12, 24)])

met_file_1 = os.path.abspath("sample_data/sample_met.txt")
met_file_2 = os.path.abspath("sample_data/sample_met2.txt")
price_file = os.path.abspath("sample_data/sample_pricing.txt")
price_file2 = os.path.abspath("sample_data/sample_pricing2.txt")
power_curve_file = os.path.abspath("sample_data/power_curve.txt")


@pytest.fixture
def sample_data():
    power_curve = PowerCurve(fname=power_curve_file)
    price_data = ElectricityPricing(fname=price_file)
    met_data = MetData(fname=met_file_1, pct=power_curve)
    align_data = AlignData(price_data=price_data, met_data=met_data)
    return align_data.align_data()


@pytest.fixture
def sample_data2():
    power_curve = PowerCurve(fname=power_curve_file)
    price_data = ElectricityPricing(fname=price_file2)
    met_data = MetData(fname=met_file_2, pct=power_curve)
    align_data = AlignData(price_data=price_data, met_data=met_data)
    return align_data.align_data()


class TestRevenue():

    def test_revenue_init_default_peak_hours(self, sample_data):
        rev = GrossRevenue(aligned_data=sample_data)
        val = rev.peak_hours.get_peak_hours()
        assert (val[0] == peak_default).all()
        assert (val[1] == off_peak_default).all()

    def test_revenue_init_defined_peak_hours(self, sample_data):
        pkhrs = PeakHours(peak=[4, 5, 1, 10], offpeak=[2, 3, 1, 8, 9])
        rev = GrossRevenue(aligned_data=sample_data, peak_hours=pkhrs)
        val = rev.peak_hours.get_peak_hours()
        assert (val[0] == [4, 5, 1, 10]).all()
        assert (val[1] == [2, 3, 1, 8, 9]).all()

    def test_revenue_init_aligned_data_na_size(self, sample_data):
        rev = GrossRevenue(aligned_data=sample_data)
        assert rev.aligned_data.isna().sum().all() == 0
        assert rev.aligned_data.shape == (8760, 3)

    def test_add_revenue_column_na_size(self, sample_data):
        rev = GrossRevenue(aligned_data=sample_data)
        rev.add_revenue_column()
        assert rev.aligned_data.isna().sum().all() == 0
        assert rev.aligned_data.shape == (8760, 4)

    def test_add_revenue_value_spot_check(self, sample_data):
        rev = GrossRevenue(aligned_data=sample_data)
        rev.add_revenue_column()
        z = rev.aligned_data.iloc[42, :]
        assert isclose(z[0], 9.14, rel_tol=1e-04)
        assert isclose(z[1], 2517.049924, rel_tol=1e-04)
        assert isclose(z[2], 25.164100, rel_tol=1e-04)
        assert isclose(z[3], 6.333930, rel_tol=1e-04)

    def test_subset_data(self, sample_data):
        rev = GrossRevenue(aligned_data=sample_data)
        rev.add_revenue_column()
        subdf = rev.subset_data(subset_on="peak")
        print("Peak")
        oncount = subdf.isna().sum()
        offcount = subdf.notnull().sum()
        for elem in oncount:
            assert elem == 4380
        for elem in offcount:
            assert elem == 4380
        subdf = rev.subset_data(subset_on="off-peak")
        print("Off-Peak")
        oncount = subdf.isna().sum()
        offcount = subdf.notnull().sum()
        for elem in oncount:
            assert elem == 4380
        for elem in offcount:
            assert elem == 4380



