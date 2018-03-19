#!/usr/bin/env python3

import pandas as pd
from unittest import mock
from windrevenue.peakhours import PeakHours

peak_default = pd.Series([i for i in range(0, 12)])
offpeak_default = pd.Series([i for i in range(12, 24)])


class TestPeakHours():

    def test_peak_init_no_args(self):
        q = PeakHours()
        assert (q.peak_hours == peak_default).all()
        assert (q.off_peak_hours == offpeak_default).all()

    def test_peak_init_peak_arg(self):
        q = PeakHours(peak=[0, 1, 3, 5, 8])
        assert (q.peak_hours == pd.Series([0, 1, 3, 5, 8])).all()
        assert (q.off_peak_hours == offpeak_default).all()

    def test_peak_init_offpeak_arg(self):
        q = PeakHours(offpeak=[0, 1, 3, 5, 8])
        assert (q.off_peak_hours == pd.Series([0, 1, 3, 5, 8])).all()
        assert (q.peak_hours == peak_default).all()

    def test_get_peak_hours(self):
        q = PeakHours(peak=[4, 5, 1, 10], offpeak=[2, 3, 1, 8, 9])
        val = q.get_peak_hours()
        assert (val[0] == [4, 5, 1, 10]).all()
        assert (val[1] == [2, 3, 1, 8, 9]).all()

    @mock.patch('builtins.input')
    def test_set_peak_hours(self, mocked_input):
        mocked_input.side_effect = ["1,3,5-9, 20-23"]
        peak = [1, 3, 5, 6, 7, 8, 9, 20, 21, 22, 23]
        offpeak = [2, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 24]
        q = PeakHours()
        q.set_peak_hours()
        assert (q.peak_hours == pd.Series(peak)).all()
        assert (q.off_peak_hours == pd.Series(offpeak)).all()




