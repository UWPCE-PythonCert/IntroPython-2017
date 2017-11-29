"""
Kathryn Egan

"""


def count_evens(numbers):
    return len([n for n in numbers if n % 2 == 0])


assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# 1
output = \
    "{name} is from {city}, and he likes {cake} cake, " +\
    "{fruit} fruit, {salad} salad, and {pasta} pasta"

assert output.format(**food_prefs) == \
    "Chris is from Seattle, and he likes chocolate cake, " +\
    "mango fruit, greek salad, and lasagna pasta"

# 2-3
hexes = {num: hex(num) for num in range(16)}

# 4
a_prefs = {key: value.lower().count('a') for key, value in food_prefs.items()}

# 5
# a
s2 = {s for s in range(21) if s % 2 == 0}
s3 = {s for s in range(21) if s % 3 == 0}
s4 = {s for s in range(21) if s % 4 == 0}

# b
divisors = range(2, 11)
sets = []
for divisor in divisors:
    sets.append({s for s in range(21) if s % divisor == 0})

# c
sets2 = [{s for s in range(21) if s % divisor == 0} for divisor in divisors]

assert sets == sets2
