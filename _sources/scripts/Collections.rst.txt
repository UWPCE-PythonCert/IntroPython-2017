:orphan:

.. _script_collections:

Collecitons Video
=================

With Rick Riehle


Intro
-----

https://docs.python.org/3/library/collections.html

*  Built-in data typs plus Collections data typs
*  Exploratory approach for this video

(as brew user)

$ mkvirtualenv -p python3 edu-collections
$ pip install --upgrade pip
$ pip install ipython


Counter
-------

https://docs.python.org/3/library/collections.html?highlight=counter#counter-objects

$ workon edu-collections
$ ipython

from random import SystemRandom
from string import ascii_letters as letters

bigstring = ''.join(SystemRandom().choice(letters) for _ in range(9999))
bigstring

from collections import Counter
counter = Counter(bigstring)
counter.elements
counter

counter['a']
counter['A']
counter.elements
counter.most_common

counter.keys()
counter.values()
sorted(counter.keys())


Named Tuple
-----------

https://docs.python.org/3/library/collections.html?highlight=counter#namedtuple-factory-function-for-tuples-with-named-fields

*  Tuples and databases

$ workon edu-collections
$ ipython

from collections import namedtuple

Contact = namedtuple('Contact', 'name, phone, email, city')

Contact?

Contact<tab>

Joe = Contact('Joe', phone='5551212', email='joe@uw.edu', city='Seattle')

Joe.name

Joe.city

# Will this work?
Fred = Contact('Fred', '1231234', 'fred@uw.edu')

# If not, what will?
Fred = Contact('Fred', '1231234', fred@uw.edu', 'Tacoma')

dir(Contact)

*  We can see the fields we defined
*  To prevent conflicts with field names, the method and attribute names start with an underscore.


Deque or deck
-------------

https://docs.python.org/3/library/collections.html#deque-objects

*  For when you need to impliment a stack or queue
*  Perhaps my favorite

from collections import deque

deque?
dir(deque)

my_queue = deque(range(9))
my_queue
my_queue.pop()
my_queue.popleft()
my_queue
my_queue.pop()
my_queue.pop()
my_queue
my_queue.popleft()
my_queue.popleft()
my_queue
my_queue.pop()
my_queue.pop()
my_queue.pop()
my_queue.pop()


Ordered Dict
------------

https://docs.python.org/3/library/collections.html?highlight=counter#ordereddict-objects ::

    $ workon edu-collections
    $ ipython

    from collections import OrderedDict
    OrderedDict?
    dir(OrderedDict)

    OrderedDict.pop?
    OrderedDict.popitem?

    from random import SystemRandom
    from string import ascii_letters as letters
    bigstring = ''.join(SystemRandom().choice(letters) for _ in range(9999))
    bigstring

    my_dict = dict.fromkeys(bigstring, 0)
    for letter in bigstring:
        my_dict[letter] += 1

    def by_value(x):
        return x[1]

    my_ordered_dict = OrderedDict(sorted(letters.items(), key=by_value))
    my_ordered_dict


Summary
-------

*  These collection types are handy and make your code more clear.
