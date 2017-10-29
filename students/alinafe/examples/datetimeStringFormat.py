#!/usr/bin/env python3
from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)

print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))

date = datetime.date(1991, 10, 12)
print(f'{date} was on a {date:%A}')
