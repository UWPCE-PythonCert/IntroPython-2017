import os

where = os.path.dirname(os.path.realpath('__file__'))
loco = "E:\\MB\Better-Butter\\Projects\\BaseLinter\\baselinter\\baselinter"

print(where)
if loco == str(where):
    print("Yes")