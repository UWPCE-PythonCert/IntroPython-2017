import iterator_1

def test_IteratorMe_2():
    it = IterateMe_2(2, 20, 2)
    for i in it:
        if i > 10:  break
        print(i)
    assert False