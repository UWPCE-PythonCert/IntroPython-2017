
""" A collection of functions to print user definable text squares. """

def print_grid(x_squares=1,y_squares=1,square_size=1):
    """ Print a grid given square size, number of x and y squares. """
    #print("x_squares:",x_squares,"y_squares:",y_squares,"square_size:",square_size)
    # number of y squares
    for y_row in range(y_squares):
        # print the top
        for top in range(x_squares):
            print("+" + "-" * square_size, end= "" )
        print("+")
        # print the middle lines
        for middle in range(square_size):
            for top in range(x_squares):
                print("|" + " " * square_size, end= "" )
            print("|")
    # print the bottom
    for bottom in range(x_squares):
        print("+" + "-" * square_size, end= "" )
    print("+")

def print_grid_fixed(square_size=3):
    """ Print a grid given square size. """
    print_grid(2,2,square_size)

def print_grid_cells(num_cells=2,square_size=2):
    """ Print a grid number of squares and square size. """
    print_grid(num_cells,num_cells,square_size)


#print_grid_cells(3,2)
#print_grid_fixed(2)
print_grid(4,3,2)
