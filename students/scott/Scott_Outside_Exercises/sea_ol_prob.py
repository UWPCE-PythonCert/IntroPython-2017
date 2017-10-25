#!/usr/bin/env python

"""
calculate the probability of a combination, n choose r
"""

# n = 10 (for my scenario it's basically hardcoded)
# r  (want to be able to change this to anything between 0 and n)

#prob_any_1 = 

#p1 * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)
#+ (1-p1) * p2 * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)
#+ (1-p1) * (1-p2) * p3 * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)
#+ (1-p1) * (1-p2) * (1-p3) * p4 * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)
#+ (1-p1) * (1-p2) * (1-p3) * (1-p4) * p5 * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)
#+ (1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * p6 * (1-p7) * (1-p8) * (1-p9) * (1-p10)
#+ (1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * p7 * (1-p8) * (1-p9) * (1-p10)
#+ (1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * p8 * (1-p9) * (1-p10)
#+ (1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * p9 * (1-p10)
#+ (1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * p10

# How to generalize the above?   for any r?
# the above problem is n = 10, r = 1









# the probabilities of each event happening

p1 = .409091
p2 = .421053
p3 = .421053
p4 = .222222
p5 = .115385
p6 = .115385
p7 = .120000
p8 = .120000
p9 = .120000
p10 = .120000

# the probabilities of each event NOT happening
not_p1 = 1-p1
not_p2 = 1-p2
not_p3 = 1-p3
not_p4 = 1-p4
not_p5 = 1-p5
not_p6 = 1-p6
not_p7 = 1-p7
not_p8 = 1-p8
not_p9 = 1-p9
not_p10 = 1-p10



# a function to generate the factorial of n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# a function to generate the # of total outcomes for r items out of n items
def factorial_outcomes(n, r):
	if n == 0:
		return 1
	else:
		return factorial(n) / (factorial(r) * ((factorial(n-r))))

# created lists for each probability set (happening and NOT happening)
yes_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
not_list = [not_p1, not_p2, not_p3, not_p4, not_p5, not_p6, not_p7, not_p8, not_p9, not_p10]


# this is the probability of all 10 events happening, just the product of all 10 probabilities

prob10 = p1 * p2 * p3 * p4 * p5 * p6 * p7 * p8 * p9 * p10

# this is the probability of none of the 10 events happening, just the product of all 10 NOT probabilities
prob0 = (1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)


# this the listed out formula for the probability of just 1 (any 1) of the 10 events happening.  This is the same formula from lines 12 through 21
prob_any_1 = (p1 * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)) + ((1-p1) * p2 * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)) + ((1-p1) * (1-p2) * p3 * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)) + ((1-p1) * (1-p2) * (1-p3) * p4 * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)) + ((1-p1) * (1-p2) * (1-p3) * (1-p4) * p5 * (1-p6) * (1-p7) * (1-p8) * (1-p9) * (1-p10)) + ((1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * p6 * (1-p7) * (1-p8) * (1-p9) * (1-p10)) + ((1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * p7 * (1-p8) * (1-p9) * (1-p10)) + ((1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * p8 * (1-p9) * (1-p10)) + ((1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * p9 * (1-p10)) + ((1-p1) * (1-p2) * (1-p3) * (1-p4) * (1-p5) * (1-p6) * (1-p7) * (1-p8) * (1-p9) * p10)
print(prob_any_1)

# now I'm stuck.  I don't know how to generalize the above.....ideally I can iterate through each list somehow.....



