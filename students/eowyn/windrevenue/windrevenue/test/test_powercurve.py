#!/usr/bin/env python3

import os
import unittest
from windrevenue.power_curve_tool import PowerCurve

pcfile = os.path.abspath("../sample_data/power_curve.txt")
windbins = [2.5, 3.0, 3.5, 4.0,
            4.5, 5.0, 5.5, 6.0,
            6.5, 7.0, 7.5, 8.0,
            8.5, 9.0, 9.5, 10.0,
            10.5, 11.0, 11.5, 12.0,
            12.5, 13.0, 13.5, 14.0,
            14.5, 15.0, 15.5, 16.0,
            16.5, 17.0, 17.5, 18.0,
            18.5, 19.0, 19.5, 20.0]

def test_init_fname():
    pc = PowerCurve(fname=pcfile)
    assert pc.power_curve[2.5] == 10
    assert pc.power_curve[7] == 1400



