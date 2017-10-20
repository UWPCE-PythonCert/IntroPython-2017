#!/usr/bin/env python

def string_formatting(a_tuple):
    arg1 = "file_"+"{0:03}".format(a_tuple[0])+":"
    arg2 = "\t"+"{:.2f}".format(a_tuple[1])
    arg3 = ", "+"{:.2e}".format(a_tuple[2])
    arg4 = ", " +"{:.2e}".format(a_tuple[3])
    print(arg1+arg2+arg3+arg4)


def formatter(a_tuple):
    ''' for an arbitrary number of values in 
    the input tuple, list all of them, formatted
    as single digits '''
    num_digs = len(a_tuple)
    fs = "The {} numbers are: "
    fs += ",".join(num_digs * ["{:d}"])
    print(fs.format(num_digs,*a_tuple))

### This alternate approach works
    # arg1 = "the {0} numbers are: ".format(num_digs)
    # form_string = "{:d},"*num_digs
    # form_string = form_string[:-1]
    # arg2=form_string.format(*a_tuple)
    # print(arg1+arg2)

if __name__=="__main__":
    string_formatting(( 2, 123.4567, 10000, 12345.67))
    formatter((2,3,5,7,9))