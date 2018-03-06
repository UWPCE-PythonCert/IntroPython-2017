#!/usr/bin/env python3

import os
import unittest

from windrevenue.UI import UI
from windrevenue.power_curve_tool import PowerCurve

pcfile = os.path.abspath("../windrevenue/sample_data/power_curve.txt")
windbins = [2.5, 3.0, 3.5, 4.0,
            4.5, 5.0, 5.5, 6.0,
            6.5, 7.0, 7.5, 8.0,
            8.5, 9.0, 9.5, 10.0,
            10.5, 11.0, 11.5, 12.0,
            12.5, 13.0, 13.5, 14.0,
            14.5, 15.0, 15.5, 16.0,
            16.5, 17.0, 17.5, 18.0,
            18.5, 19.0, 19.5, 20.0]

def test_powercurve_init_with_fname():
    pc = PowerCurve(fname=pcfile)
    assert pc.power_curve[2.5] == 10
    assert pc.power_curve[7] == 1400

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

def test_load_powercurve_with_ui(capsys):
    input_lines = ["2", "3", pcfile, "4", "6"]
    input_feeder = InputFeeder(input_lines)
    from unittest import mock
    import builtins
    # with capsys.disabled():
    with mock.patch.object(UI, 'get_user_input', input_feeder.get_user_input):
        ui = UI()
        import pytest
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            ui.mainloop()
            assert pytest_wrapped_e.type == SystemExit
            assert pytest_wrapped_e.value.code == 42
        captured = capsys.readouterr()
        assert "Reading power curve file" in captured.out
        # assert "Thank you, Kenny Powers, for your generosity and recent gift of $1000000.00.\n" == captured.out
        assert "" == captured.err
        print(captured.out)


