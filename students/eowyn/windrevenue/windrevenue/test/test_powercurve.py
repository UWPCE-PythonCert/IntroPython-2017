#!/usr/bin/env python3

import os
import sys
from windrevenue.power_curve_tool import PowerCurve

dirname = os.path.dirname(sys.modules["windrevenue"].__file__)
sample_data = os.path.join(dirname, "sample_data")
power_curve_file = os.path.join(sample_data, "power_curve.txt")

pcfile = power_curve_file


def test_powercurve_init_with_fname():
    pc = PowerCurve(fname=pcfile)
    power_curve = pc.power_curve
    assert power_curve[power_curve["WS"] == 2.5]["Pwr"].iloc[0] == 10


def test_powercurve_init_with_fname2():
    pc = PowerCurve(fname=pcfile)
    power_curve = pc.power_curve
    assert power_curve[power_curve["WS"] == 7]["Pwr"].iloc[0] == 1400

