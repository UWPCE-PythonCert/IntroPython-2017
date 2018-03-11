#!/usr/bin/env python3

import os
from windrevenue.power_curve_tool import PowerCurve

pcfile = os.path.abspath("../windrevenue/sample_data/power_curve.txt")


def test_powercurve_init_with_fname():
    pc = PowerCurve(fname=pcfile)
    power_curve = pc.power_curve
    assert power_curve[power_curve["WS"] == 2.5]["Pwr"].iloc[0] == 10

def test_powercurve_init_with_fname2():
    pc = PowerCurve(fname=pcfile)
    power_curve = pc.power_curve
    assert power_curve[power_curve["WS"] == 7]["Pwr"].iloc[0] == 1400



