'''Utility Script to create a guide for the BaseLineter.'''

import uuid

def create_guide(filename):
    ''' '''
    try:
        lines = list(open(filename))
    except FileNotFoundError:
        print("Issue trying to find file.")

    out = "{\n "
    for l in lines:
        items = ""
        r_items = l.split(",")
        for i in r_items:
            items = items + '"{}",'.format(i.strip())
        items = items[:-1]
        row = '"{}" : [{}],\n'.format(str(uuid.uuid4()), items)
        out = out + row
    out = out[:-2] + " \n}"

    return out

def create_file(oufilename, outstring):
    ''' '''
    with open(oufilename, 'w') as f:
        f.write(outstring)

def main():
    '''The main routine for the create a guide.'''
    print("Create a guide for the BaseLinter.")
    filename = input("Type file to input. > ")
    output = create_guide(filename)
    oufilename = input("Type the name of the file. > ")
    create_file(oufilename, output)
    print("Thanks")


if __name__ == "__main__":
    main()