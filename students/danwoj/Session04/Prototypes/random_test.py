lists=dict(animals=["dog","cat","shark"],
           things=["desk","chair","pencil"],
           food=["spaghetti","ice-cream","potatoes"])

import random

which_list, item = random.choice([(name, value) 
                                     for name, values in lists.items() 
                                         for value in values])

print('which_list: ', which_list)
print('item: ', item)