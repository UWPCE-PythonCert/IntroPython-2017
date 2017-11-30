"""
Kathryn Egan
"""
import pytest
from SparseArray import SparseArray


def test_length():
    a = SparseArray([1, 2, 3, 0, 0, 0, 0])
    assert len(a) == 7


def test_equals():
    array = [0, 1, 2, 3, 0, 0, 4, 0]
    a = SparseArray(array)
    assert a == array
    assert a == [0, 1, 2, 3, 0, 0, 4, 0]
    assert a != [1, 2, 3, 4]
    assert a != [0, 0, 0, 0]
    assert a != [1, 2, 3, 0, 0, 4]
    array.reverse()
    a2 = SparseArray(array)
    assert a != a2


def test_string():
    a1 = SparseArray()
    assert str(a1) == '[]'
    a2 = SparseArray([1, 0, 0, 0, 4, 5, 0, 0])
    assert str(a2) == '[1, 0, 0, 0, 4, 5, 0, 0]'


def test_getter():
    a = SparseArray([1, 0, 0, 0, 5])
    assert a[0] == 1
    assert a[1] == 0
    assert a[-1] == 5
    with pytest.raises(IndexError):
        a[6]
        a[-7]


def test_setter():
    a = SparseArray([1, 2, 3, 4, 5])
    a[0] = 0
    assert a[0] == 0
    a[-1] = 6
    assert a[4] == 6
    assert len(a) == 5
    with pytest.raises(IndexError):
        a[6] = 0


def test_delete():
    a = SparseArray([1, 0, 0, 0, 4, 0])
    print(a)
    del a[0]  # [0, 0, 0, 4, 0]
    print(a)
    assert a[0] == 0
    assert len(a) == 5
    del a[2]  # [0, 0, 4, 0]
    print(a)
    assert a[2] == 4
    assert len(a) == 4
    del a[-2]  # [0, 0, 0]
    print(a)
    assert a[-2] == 0
    assert len(a) == 3
    with pytest.raises(IndexError):
        del a[10]


def test_append():
    a = SparseArray()
    a.append(1)
    assert a[0] == 1
    assert len(a) == 1
    a.append(0)
    assert a[0] == 1
    assert a[1] == 0
    assert len(a) == 2


def test_reversed():
    a = SparseArray([0, 0, 0, 1, 1, 0])
    rev = reversed(a)
    assert rev == [0, 1, 1, 0, 0, 0]
    a2 = SparseArray()
    rev2 = reversed(a2)
    assert rev2 == []


def test_reverse():
    a = SparseArray([0, 0, 0, 1, 1, 0])
    a.reverse()
    assert a == [0, 1, 1, 0, 0, 0]


def test_iterate():
    a = SparseArray([0, 0, 0, 1, 1, 0])
    temp = [element for element in a]
    assert a == temp
    for i, value in enumerate(a):
        assert a[i] == value


def test_extend():
    a = SparseArray([0])
    print(a)
    a.extend([1, 2, 3, 0, 0, 0])
    print(a)
    assert a == [0, 1, 2, 3, 0, 0, 0]
    assert len(a) == 7


def test_contains():
    a = SparseArray()
    assert 0 not in a
    a.extend([1, 2, 3, 0, 0, 1, 0])
    assert 0 in a
    assert 1 in a
    assert 3 in a
    assert 5 not in a
    a2 = SparseArray([1])
    assert 0 not in a2


def test_sort():
    a = SparseArray([0, 3, 0, 1, 1, 0])
    s = sorted(a)
    assert s == [0, 0, 0, 1, 1, 3]
    assert type(s) == SparseArray  # fails
