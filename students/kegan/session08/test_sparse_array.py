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


def test_tuple():
    a = SparseArray((0, 1, 2, 3, 0, 0, 4))
    assert a == [0, 1, 2, 3, 0, 0, 4]


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


def test_plus():
    a1 = SparseArray([1])
    a1 = a1 + [4, 5, 6]
    assert a1 == [1, 4, 5, 6]
    a2 = SparseArray([7, 0, 0])
    a2 = a1 + a2
    assert a2 == [1, 4, 5, 6, 7, 0, 0]
    assert a1 == [1, 4, 5, 6]
    a2 += [4, 0, 0]
    assert a2 == [1, 4, 5, 6, 7, 0, 0, 4, 0, 0]


def test_multiply():
    a1 = SparseArray([1, 2, 3])
    a2 = a1 * 3
    assert a1 == [1, 2, 3]
    assert a2 == [1, 2, 3, 1, 2, 3, 1, 2, 3]
    a3 = SparseArray([0, 0, 0])
    a3 *= 2
    assert a3 == [0, 0, 0, 0, 0, 0]
    a3 = 2 * a3
    assert a3 == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


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


def test_slicing():
    a = SparseArray([0, 0, 1, 2, 0, 7])
    assert a[2:5] == [1, 2, 0]
    assert a[2:] == [1, 2, 0, 7]
    assert a[2::2] == [1, 0]
    assert a[:10] == [0, 0, 1, 2, 0, 7]
    assert a[::3] == [0, 2]
    assert a[::] == [0, 0, 1, 2, 0, 7]
    assert a[0:1] == [0]
    assert a[0:0] == []
    assert a[::-1] == [7, 0, 2, 1, 0, 0]
    assert a[::-2] == [7, 2, 0]
    with pytest.raises(TypeError):
        a['hello':'goodbye']
    with pytest.raises(IndexError):
        a[100:101]
    assert a[:2, 4:] == [0, 0, 0, 7]


def test_index():
    a = SparseArray([1, 2, 0, 5, 0])
    assert a.index(1) == 0
    assert a.index(0) == 2
    with pytest.raises(ValueError):
        a.index(6)
