#! /usr/bin/env python


def print_food_prefs():
    """ Print the dict by passing it to a string format method
    """

    food_prefs = {"name": "Chris",
                  "city": "Seattle",
                  "cake": "chocolate",
                  "fruit": "mango",
                  "salad": "greek",
                  "pasta": "lasagna"}

    print('{name} is from {city} and he likes {cake}, {fruit}, \
{salad} salad, and {pasta} pasta.'.format(**food_prefs))


if __name__ == "__main__":
    print_food_prefs()
