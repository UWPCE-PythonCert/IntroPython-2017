"""
Kathryn Egan
"""
import pytest
from SparseArray import SparseArray


def test_length():
    p = [1, 2, 3, 0, 0, 0, 0]
    a = SparseArray(p)
    assert len(a) == len(p)


def test_equals():
    array = [0, 1, 2, 3, 0, 0, 4, 0]
    a = SparseArray(array)
    assert a == array
    assert a == [0, 1, 2, 3, 0, 0, 4, 0]
    assert a != [0, 1, 2, 3, 0, 0, 4, 0, 0]
    assert a != [0, 1, 2, 3, 0, 0, 4]
    assert a != [1, 2, 3, 4]
    assert a != [0, 0, 0, 0]
    assert a != [1, 2, 3, 0, 0, 4]
    array.reverse()
    a2 = SparseArray(array)
    assert a != a2


def test_comparisons():
    lt = [
        [],
        [0, 1],
        [0, 0],
        [0, 1, 2, 3]]

    gt = [
        [0, 2],
        [1, 1],
        [0, 1, 2, 3, 0, 0]]

    le = lt[::]
    le.append([0, 1, 2, 3, 0])
    ge = gt[::]
    ge.append([0, 1, 2, 3, 0])
    array = [0, 1, 2, 3, 0]
    a = SparseArray(array)
    assert a == array

    for temp in lt:
        assert temp < a
        assert not a < temp
        assert temp != a
        assert a != temp

    for temp in le:
        assert temp <= a
        assert not a < temp
    assert not a < a

    for temp in gt:
        assert a < temp
        assert not temp < a
        assert temp != a
        assert a != temp

    for temp in ge:
        assert a <= temp
        assert not temp < a
    assert not a > a


def test_tuple():
    p = (0, 1, 2, 3, 0, 0, 4)
    a = SparseArray(p)
    assert a == p


def test_string():
    p1 = []
    a1 = SparseArray()
    assert str(a1) == str(p1)
    p2 = [1, 0, 0, 0, 4, 5, 0, 0]
    a2 = SparseArray(p2)
    assert str(a2) == str(p2)


def test_getter():
    p = [1, 0, 0, 0, 5]
    a = SparseArray(p)
    assert a[0] == p[0]
    assert a[1] == p[1]
    assert a[-1] == p[-1]
    with pytest.raises(IndexError):
        a[6]
        a[-7]


def test_setter():
    p = [1, 2, 3, 4, 5]
    a = SparseArray(p)
    a[0] = 0
    p[0] = 0
    assert a == p
    assert len(a) == 5
    assert len(a.data) == 4  # do not store zero
    a[0] = 0
    a[-1] = 6
    p[-1] = 6
    assert a == p
    assert len(a) == len(p)
    assert len(a.data) == 4
    a[-3] = 0
    p[-3] = 0
    assert len(a) == len(p)
    assert len(a.data) == 3
    a[-3] = 5
    p[-3] = 5
    assert len(a.data) == 4
    with pytest.raises(IndexError):
        a[6] = 0
    with pytest.raises(IndexError):
        a[-8] = 1


def test_delete():
    p = [1, 0, 0, 0, 4, 0]
    a = SparseArray(p)
    del a[0]
    del p[0]
    assert a == p
    assert len(a) == len(p)
    del a[2]
    del p[2]
    assert a == p
    assert len(a) == len(p)
    del a[-2]
    del p[-2]
    assert a == p
    assert len(a) == len(p)
    with pytest.raises(IndexError):
        del a[10]


def test_append():
    a = SparseArray()
    p = []
    a.append(1)
    p.append(1)
    assert a == p
    assert len(a) == len(p)
    a.append(0)
    p.append(0)
    assert a == p
    assert len(a) == len(p)
    assert len(a.data) == 1


def test_plus():
    p1 = [1]
    temp = [4, 5, 6]
    a1 = SparseArray(p1)
    a1 = a1 + temp
    p1 = p1 + temp
    assert a1 == p1
    p2 = [7, 0, 0]
    a2 = SparseArray(p2)
    a2 = a1 + a2
    p2 = p1 + p2
    assert a2 == p2
    assert a1 == p1
    temp = [4, 0, 0]
    a2 += temp
    p2 += temp
    print(a2)
    print(p2)
    assert a2 == p2
    assert len(a2.data) == 6


def test_multiply():
    p1 = [1, 2, 3]
    a1 = SparseArray(p1)
    a2 = a1 * 3
    p2 = p1 * 3
    assert a1 == p1
    assert a2 == p2
    p3 = [0, 0, 0]
    a3 = SparseArray(p3)
    a3 *= 2
    p3 *= 2
    assert a3 == p3
    a3 = 2 * a3
    p3 = 2 * p3
    assert a3 == p3
    with pytest.raises(TypeError):
        a3 * 1.2


def test_reversed():
    p1 = [0, 0, 0, 1, 1, 0]
    a1 = SparseArray(p1)
    a1 = list(reversed(a1))
    p1 =list(reversed(p1))
    print(a1)
    print(p1)
    assert a1 == p1
    p2 = []
    a2 = SparseArray()
    assert list(reversed(a2)) == list(reversed(p2))


def test_reverse():
    p1 = [0, 0, 0, 1, 1, 0]
    a1 = SparseArray(p1)
    a1.reverse()
    p1.reverse()
    assert a1[0] == p1[0]
    print(a1)
    print(p1)
    assert a1 == p1
    a1.reverse()
    p1.reverse()
    assert a1 == p1
    a2 = SparseArray()
    a2.reverse()
    p2 = []
    p2.reverse()
    assert a2 == p2


def test_iterate():
    p = [0, 0, 0, 1, 1, 0]
    a = SparseArray(p)
    temp = [element for element in a]
    assert temp == p
    for i, value in enumerate(a):
        assert a[i] == value


def test_extend():
    p = [0]
    a = SparseArray(p)
    extension = [1, 2, 3, 0, 0, 0]
    a.extend(extension)
    p.extend(extension)
    assert a == p
    assert len(a) == len(p)
    assert len(a.data) == 3


def test_contains():
    a1 = SparseArray()
    assert 0 not in a1
    a2 = SparseArray([1])
    assert 0 not in a2
    a3 = SparseArray([1, 2, 3, 0, 0, 1, 0])
    assert 0 in a3
    assert 1 in a3
    assert 3 in a3
    assert 5 not in a3


def test_slicing():
    p = [0, 1, 2, 3, 4, 5]
    a = SparseArray(p)
    tests = [None] + list(range(-7, 7))
    with pytest.raises(ValueError):
        a[::0]
    for start in tests:
        for stop in tests:
            for step in tests:
                if step == 0:
                    continue
                assert a[start:stop:step] == p[start:stop:step]
    a.reverse()
    p.reverse()
    for start in tests:
        for stop in tests:
            for step in tests:
                if step == 0:
                    continue
                assert a[start:stop:step] == p[start:stop:step]


def test_index():
    p = [1, 2, 0, 5, 0]
    a = SparseArray(p)
    assert a.index(1) == p.index(1)
    assert a.index(0) == p.index(0)
    with pytest.raises(ValueError):
        a.index(6)


def test_insert():
    p = [1, 2, 3, 0, 4]
    a = SparseArray(p)
    p.insert(0, 1)  # [1, 1, 2, 3, 0, 4]
    a.insert(0, 1)
    assert a == p
    assert len(a.data) == 5
    p.insert(2, 0)  # [1, 1, 0, 2, 3, 0, 4]
    a.insert(2, 0)
    assert a == p
    assert len(a.data) == 5
    p.insert(100, 77)  # [1, 1, 0, 2, 3, 0, 4, 77]
    a.insert(100, 77)
    assert a == p
    assert len(a.data) == 6
    assert len(a) == len(p)
    p.insert(-3, 5)
    a.insert(-3, 5)
    assert a == p
    p.insert(-100, 99)
    a.insert(-100, 99)
    assert a == p
    p = []
    a = SparseArray(p)
    p.insert(4, 2)
    a.insert(4, 2)
    assert a == p
    p.insert(1, 0)
    a.insert(1, 0)
    assert a == p
    p.insert(2, 0)
    a.insert(2, 0)
    assert a == p


def test_count():
    p1 = [1, 1, 1, 2, 2, 0, 0, 0, 0]
    a1 = SparseArray(p1)
    for i in range(4):
        assert a1.count(i) == p1.count(i)
    p2 = [0, 0, 0]
    a2 = SparseArray(p2)
    for i in range(4):
        assert a2.count(i) == p2.count(i)


def test_iforward():
    s1 = SparseArray([0, 1, 2, 3, 4])
    assert s1._iforward(-1) == 4
    assert s1._iforward(-5) == 0
    assert s1._iforward(-6) == -1
    assert s1._iforward(1) == 1
    assert s1._iforward(7) == 7
    s2 = SparseArray()
    assert s2._iforward(-1) == -1
    assert s2._iforward(0) == 0


def test_ilimit():
    s1 = SparseArray([0, 1, 2, 3])
    assert s1._ilimit(-6) == 0
    assert s1._ilimit(7) == 4
    assert s1._ilimit(0) == 0
    assert s1._ilimit(2) == 2


def test_ireverse():
    s1 = SparseArray([0, 1, 2, 3])
    assert s1._ireverse(0) == 3
    assert s1._ireverse(-1) == 4
    assert s1._ireverse(4) == -1
