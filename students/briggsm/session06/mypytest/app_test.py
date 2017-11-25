import app

def test_summit_1_1():
    assert app.summit(1,1) == 2

def test_summit_0_1():
    assert app.summit(0,1) == 1

def test_summit_mix_char():
    assert app.summit("a", "b") == -1

def test_summit_mix_type():
    assert app.summit("a", 5) == -1