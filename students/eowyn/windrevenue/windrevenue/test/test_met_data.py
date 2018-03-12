#!/usr/bin/env python3

import os
import sys
import pytest
from math import isclose
from windrevenue.parse_met_data import MetData
from windrevenue.power_curve_tool import PowerCurve

dirname = os.path.dirname(sys.modules["windrevenue"].__file__)
sample_data = os.path.join(dirname, "sample_data")
met_file_1 = os.path.join(sample_data, "sample_met.txt")
met_file_2 = os.path.join(sample_data, "sample_met2.txt")
power_curve_file = os.path.join(sample_data, "power_curve.txt")


@pytest.fixture
def sample_data():
    pcfile = power_curve_file
    fname = met_file_1
    pc = PowerCurve(fname=pcfile)
    met = MetData(fname=fname, pct=pc)
    return met


@pytest.fixture
def sample_data2():
    pcfile = power_curve_file
    fname = met_file_2
    pc = PowerCurve(fname=pcfile)
    met = MetData(fname=fname, pct=pc)
    return met


class TestMet():

    def test_data_length(self, sample_data):
        assert len(sample_data.get_met_timeseries()) == 127328

    def test_data_no_nan(self, sample_data):
        ts = sample_data.get_met_timeseries().isna().sum()
        assert ts.sum() == 0

    def test_select_correct_sensor(self, sample_data):
        ts = sample_data.get_met_timeseries().columns
        assert ts == "65m Anemometer Mean"

    def test_select_correct_sensor_sample2(self, sample_data2):
        ts = sample_data2.get_met_timeseries().columns.values[0]
        assert ts == "55m Anemometer Mean"

    def test_generation_size(self, sample_data):
        ts = sample_data.get_wind_and_generation()
        print(ts.shape)
        assert ts.shape == (127328, 2)

    def test_generation_data_spotcheck(self, sample_data):
        ts = sample_data.get_wind_and_generation()
        z = ts.iloc[400, :]
        assert isclose(z[0], 11.64, rel_tol=1e-04)
        assert isclose(z[1], 3114, rel_tol=1e-04)







