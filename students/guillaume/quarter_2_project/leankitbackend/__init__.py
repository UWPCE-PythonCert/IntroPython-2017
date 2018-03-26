from util import import_data
from os import listdir, getcwd
'''
print(__name__)

print(getcwd())
print(listdir())
global Leankit_input
Leankit_input = import_data('input.json')
# print(globals())
print(Leankit_input)
print(set(Leankit_input))

needed_key = {"username",
              "company",
              "limit",
              "description",
              "password",
              "board",
              "output",
              "cron_data"}

print(list(globals().keys()))
assert needed_key <= set(Leankit_input)
assert 'Leankit_input' in globals()
'''