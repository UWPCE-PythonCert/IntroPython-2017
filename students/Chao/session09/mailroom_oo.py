#!/usr/bin/env python

class Donor:
    def __init__(self, name, amount):
        self.name = name
        self.amount = [amount]

    def new_donation(self, amount):
        self.amount.append(amount)

    @property
    def total_donation(self):
        return sum(self.amount)



