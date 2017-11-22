'''This is my working out how pytest works myself..'''

def summit(a,b):
    try:
        c = int(a + b)
    except:
        c = -1
    return c
