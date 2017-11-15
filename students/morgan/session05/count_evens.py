count_evens1= ([2,1,2,3,4])
count_evens2=([2,2,0])
count_evens3=([1,3,5])
comp1 = [ num for num in count_evens1 if num % 2 == 0 ]
comp2 = [ num for num in count_evens2 if num % 2 == 0 ]
comp3 = [ num for num in count_evens3 if num % 2 == 0 ]
print(len(comp1))
print(len(comp2))
print(len(comp3))

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# food_prefs2 = food_prefs.copy()

food_prefs2 = {k:v.count('a') for k,v in food_prefs.items()}

print(food_prefs2)

print('{name} is from {city}, and he likes {cake} cake, {fruit}, {salad} salad, \
and {pasta} pasta'.format(**food_prefs))
        # name=food_prefs['name'], city=food_prefs['city'], cake=food_prefs['cake'],\
        # fruit=food_prefs['fruit'], salad=food_prefs['salad'],pasta=food_prefs['pasta']))

num_list = [i for i in range(16)]
# i = 0
# while i <=15:
#     num_list.append(i)
#     i += 1
print(num_list)

hex_dict = {k:hex(k) for k in num_list}
print(hex_dict)

s2 = set(i for i in range(21) if i % 2 == 0)
s3 = set(i for i in range(21) if i % 3 == 0)
s4 = set(i for i in range(21) if i % 4 == 0)

divisors = set([2,3,4,5,5,6,7,8,9,10])

answer_sets = [{i for i in range(21) if i % d ==0} for d in divisors]
print(answer_sets)


