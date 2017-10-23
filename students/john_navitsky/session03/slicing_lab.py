
def exchange(sequence):
    return sequence[-1:]+ sequence[1:-1] + sequence[:1]

def other(sequence):
    return sequence[::2]

def removed(sequence):
    return sequence[4:-4]

def reversed(sequence):
    return sequence[::-1]

def thirds(sequence):
	third=len(sequence)//3
	first=sequence[:third]
	last=sequence[third*2:]
	middle=sequence[third:third*2]
	return middle+last+first



a_string = "this is a string"
a_tuple = ( 2, 54, 13, 12, 5, 32)

assert exchange(a_string) == "ghis is a strint"
assert exchange(a_tuple) == (32, 54, 13, 12, 5, 2)

assert other(a_string) == "ti sasrn"
assert other(a_tuple) == (2, 13, 5)

assert removed(a_string) == " is a st"
assert removed(a_tuple) == ()

assert reversed(a_string) == "gnirts a si siht"
assert reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

assert thirds(a_string) == "is a stringthis "
assert thirds(a_tuple) == (13, 12, 5, 32, 2, 54)

