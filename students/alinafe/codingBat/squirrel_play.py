#!/usr/bin/env python3
"""
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
"""
def squirrel_play(temp, is_summer):
    return (temp >= 60 and temp <= 90) if not is_summer else (temp >= 60 and temp <= 100)

if __name__ == "__main__":
    # some tests
    assert squirrel_play(70, False) is	True
    assert squirrel_play(95, False) is	False
    assert squirrel_play(95, True) is	True
    assert squirrel_play(90, False) is	True
    assert squirrel_play(90, True) is	True
    assert squirrel_play(50, False) is	False
    assert squirrel_play(50, True) is	False
    assert squirrel_play(100, False) is	False
    assert squirrel_play(100, True) is	True
    assert squirrel_play(105, True) is	False
    assert squirrel_play(59, False) is	False
    assert squirrel_play(59, True) is	False
    assert squirrel_play(60, False) is	True

    print("All tests passed")
