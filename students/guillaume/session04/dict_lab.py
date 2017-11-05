#!/usr/bin/env python3


def dictionnaries_1():
    '''
    Playing with a dic key name, values city & cake
    '''

    d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(d)
    del d['cake']
    print(d)
    d['fruit'] = 'Mango'
    print(d.keys())
    print(d.values())
    print('cake' in d.keys())
    print('Mango' in d.values())
    return d


def dictionnaries_2():
    '''
    Mod values in dic
    '''
    d = dictionnaries_1()

    for x in d:
        d[x] = d[x].count('t')
    print(d)


def sets():
    s2 = set(x for x in range(0, 21, 2))
    s4 = set(x for x in s2 if x % 4 == 0)
    s3 = set(x for x in range(21) if x % 3 == 0)
    print(type(s2))
    print(s2)
    print(s3)
    print(s4)
    print(s3.issubset(s2))
    print(s4.issubset(s2))


def sets2():
    sp = set('Python')
    print(sp)
    sp.update('i')
    print(sp)
    sm = frozenset('marathon')
    print(sp.union(sm))
    print(sp.intersection(sm))


if __name__ == '__main__':
    dictionnaries_2()
    sets()
    sets2()
