#!/usr/bin/env python
def exchange_first_last(seq):
    ''' return copy of sequence with first and last items exchanged 
     exploit fact that slices are sequences but single references are not'''
    return seq[-1:]+seq[1:-1]+seq[:1]

def remove_odd_items(seq):
    ''' remove every other item from sequence'''
    return seq[::2]

def remove_endfours_odd_items(seq):
    '''first and last 4 items removed, and every other item in between'''
    return seq[4:-4:2]

def reverse(seq):
    ''' with the elements reversed (just with slicing)'''
    return seq[::-1]

def swap_middle(seq):
    '''with the middle third, then last third, then the first third in the new order
    and for strings with n_chars not a multiple of three, shorten the end third'''
    third = round(len(seq)/3)
    return seq[third:-third]+seq[-third:]+seq[:third]


if __name__=="__main__":
    assert exchange_first_last("this is a string") == "ghis is a strint"
    assert exchange_first_last([1,2,3,4]) == [4,2,3,1]
    assert exchange_first_last((1,2,3,4)) == (4,2,3,1)

    assert remove_odd_items((1,2,3,4,5)) == (1,3,5)
    assert remove_odd_items([1,2,3,4]) == [1,3]
    assert remove_odd_items("remove") == "rmv"

    assert reverse("hello") == "olleh"
    assert reverse([1,2,3])==[3,2,1]
    assert reverse((1,2,3))==(3,2,1)

    assert swap_middle("hello")=="llohe"
    assert swap_middle("burtsbees") == "tsbeesbur"
    assert swap_middle([1,2,3,4,5,6]) == [3,4,5,6,1,2]
    assert swap_middle((1,2,3,4,5,6)) == (3,4,5,6,1,2)

    assert remove_endfours_odd_items("abcdefghijk") == ("eg")
    assert remove_endfours_odd_items((0,1,2,3,4,5,6,7,8,9,10))==(4,6)
    assert remove_endfours_odd_items([0,1,2,3,4,5,6,7,8,9,10])==[4,6]
