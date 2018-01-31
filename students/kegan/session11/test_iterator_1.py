

from iterator_1 import IterateMe_1 as IM
import pytest


def test_iterate1():
    possibles = list(range(1, 20))
    for start in possibles:
        for stop in possibles:
            for step in possibles:
                mine = IM(start, stop, step)
                theirs = range(start, stop, step)
                for m, t in zip(mine, theirs):
                    assert m == t


def test_iterate2():
    possibles = list(range(1, 10))
    for start in possibles:
        for stop in possibles:
            for step in possibles:
                mine = IM(start, stop, step)
                theirs = range(start, stop, step)
                for m, t in zip(mine, theirs):
                    assert m == t
                    if m > 5:
                        break
                for m, t in zip(mine, theirs):
                    assert m == t


def test_parameters():
    mine = IM(10)
    assert mine.start == 0
    assert mine.stop == 10
    assert mine.current == 0
    assert mine.step == 1

    mine = IM(2, 10)
    assert mine.start == 2
    assert mine.stop == 10
    assert mine.current == 2
    assert mine.step == 1

    mine = IM(2, 10, 3)
    assert mine.start == 2
    assert mine.stop == 10
    assert mine.current == 2
    assert mine.step == 3


def test_reverse():
    possibles = list(range(-5, 5))
    for start in possibles:
        for stop in possibles:
            for step in possibles:
                if step == 0:
                    with pytest.raises(ValueError):
                        assert IM(start, stop, step)
                    continue
                mine = IM(start, stop, step)
                theirs = range(start, stop, step)
                assert mine.start == theirs.start
                assert mine.stop == theirs.stop
                assert mine.step == theirs.step
                for m, t in zip(mine, theirs):
                    assert m == t


