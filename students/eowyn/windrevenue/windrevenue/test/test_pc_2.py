#!/usr/bin/env python
from windrevenue.UI import UI
from windrevenue.power_curve_tool import PowerCurve

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

def test_load_powercurve(capsys):
    input_lines = ["1", "1", "Kenny Powers", "1000000", "3", "5"]
    input_feeder = InputFeeder(input_lines)
    from unittest import mock
    import builtins
    # with capsys.disabled():
    with mock.patch.object(Mailroom, 'get_user_input', input_feeder.get_user_input):
        mailroom = Mailroom(Transactions())
        import pytest
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            mailroom.mainloop()
            assert pytest_wrapped_e.type == SystemExit
            assert pytest_wrapped_e.value.code == 42
        captured = capsys.readouterr()
        assert "Thank you, Kenny Powers, for your generosity and recent gift of $1000000.00.\n" == captured.out
        assert "" == captured.err
        print(captured.out)

