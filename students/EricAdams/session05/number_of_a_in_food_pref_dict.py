#! /usr/bin/env python
""" Make a dictionary with the the number of a's in each value
use the dict:
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
"""

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

food_prefs_a_count = {}


def food_prefs_count_the_a():
    for dict_key in food_prefs:
        food_prefs_a_count.setdefault(dict_key, 0)
        for character in food_prefs[dict_key]:
            if character == 'a':
                food_prefs_a_count[dict_key] += 1


if __name__ == "__main__":
    food_prefs_count_the_a()
    print(food_prefs_a_count)
