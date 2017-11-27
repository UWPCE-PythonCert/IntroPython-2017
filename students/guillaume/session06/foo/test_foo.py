def test_foo():
    import sys
    from foo import foo
    from io import StringIO

    saved_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        foo()
        output = out.getvalue().strip()
        assert output == 'hello world!'
    finally:
        sys.stdout = saved_stdout
