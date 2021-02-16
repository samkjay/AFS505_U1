""" AFS505 Unit 1 class project

.. module:: Class projectU1
    :platform: Windows
    :synopsis: This program would enable to run the "Game of life" with user specified inital conditions and number
    of iteration. The grid size has being defined by the programmer to be 30 x 80.

.. moduleauthor:: Sam Jayasinghe (samodyajayasinghe@wsu.edu)
"""


from sys import argv

def count_neighbors(input_array, neighbor_sum, num_row, num_col):
    """This is a function to count 'on' neighbors for each cell in the array,
        and saving each count to a second array that has the same number of rows and columns

     :param input_array: a 2D list(array) defined within the main function
     :type input_array:  a 2D list containing 0 or 1 values

     :param neighbor_sum: a 2D list(array) storing the output of the function,the number of 'on(1)' neighbors for each cell in input array
     :type neighbor_sum:  a 2D list containing integers

     :param num_row: number of rows in input_array, the value is defined within the main function
     :type num_row: integer

     :param col_row: number of columns in input_array, the value is defined within the main function
     :type col_row: integer

     """
    for i in range(num_col):
        for j in range(num_row):
                # to check the neighbor square to north
                if j == 0: # because this row does not have neighbors to the north, this line skips counting it
                   continue
                else:
                   #This line in each if statements adds '1' or '0' to the neighbor cell count of the tested cell, based on if it's 'on' or 'off'
                   neighbor_sum[j][i] += input_array[j-1][i]
                # to check the neighbor square to south
                if j == (num_row-1): #because this row does not have neighbors to the south, this line skips counting it
                   continue
                else:
                   neighbor_sum[j][i] += input_array[j+1][i]
                # to check the neighbor square to west
                if  i== 0: #because this row does not have neighbors to the west, this line skips counting it
                   continue
                else:
                   neighbor_sum[j][i] += input_array[j][i-1]
                # to check the neighbor square to east
                if i == (num_col-1): #because this row does not have neighbors to the east, this line skips counting it
                   continue
                else:
                   neighbor_sum[j][i] += input_array[j][i+1]
                # to check the neighbor square to north east
                if j == 0 or i == (num_col-1): #because this row and column does not have neighbors to the north east, this line skips counting it
                   continue
                else:
                   neighbor_sum[j][i] += input_array[j-1][i+1]
                # to check the neighbor square to south east
                if j == (num_row-1) or i == (num_col-1): #because this row and column does not have neighbors to the south east, this line skips counting it
                   continue
                else:
                   neighbor_sum[j][i] += input_array[j+1][i+1]
                # to check the neighbor square to north west
                if j == 0 or i == 0: #because this row and column does not have neighbors to the north west,this line skips counting it
                   continue
                else:
                   neighbor_sum[j][i] += input_array[j-1][i-1]
                # to check the neighbor square to south west
                if j ==  (num_row-1) or i == 0: #because this row and column does not have neighbors to the south west, this line skips counting it
                   continue
                else:
                   neighbor_sum[j][i] += input_array[j+1][i-1]

def apply_rules(input_array, neighbor_sum, num_row, num_col):
   """This is a function to define the rules of the "game of life" to each cell in the input_array,
       based on number of 'on' or 'off' neighboring cells following the previous iteration of the input input_array

    :param input_array: a 2D list(array) defined within the main function
    :type input_array:  a 2D list containing 0 or 1 values

    :param neighbor_sum: a 2D list(array) containg the total count of "on" neighbor cells for each cell in the input_array
    :type neighbor_sum:  a 2D list containing integers

    :param num_row: number of rows in input_array, the value is defined within the main function
    :type num_row: integer

    :param col_row: number of columns in input_array, the value is defined within the main function
    :type col_row: integer

    """

   for i in range(num_col):
         for j in range(num_row):
            #the following part of the if loop considers an "on" cell
            if input_array[j][i] == 1:
               #if the number of 'on' neighbor cells is less than 2,
               if neighbor_sum[j][i] < 2:
                  #the the cell is turned off
                  input_array[j][i] = 0
               #if the number of 'on' neighbor cells is greater than 3,
               elif neighbor_sum[j][i]  > 3:
                  #the the cell is turned off
                  input_array[j][i] = 0
                  #if both above arguments are false, the cell stays 'on'
               else:
                  input_array[j][i] = 1
            #the following part of the if loop considers and initially 'off' cell
            else:
                #if the number of 'on' neighbor cells is equal exactly to 3
                if neighbor_sum[j][i] == 3:
                  #the the cell is turned 'on'
                  input_array[j][i] = 1
                #if not the cell stays 'off'
                else:
                  input_array[j][i] = 0

#function to repeatedly pritn the 2D list(array) after each iteration
def print_grid(input_array, num_row, num_col):
    """This is a function to print the 2D list(array) after each iteration

     :param input_array: a 2D list(array) defined within the main function
     :type input_array:  a 2D list containing 0 or 1 values

     :param num_row: number of rows in input_array, the value is defined within the main function
     :type num_row: integer

     :param col_row: number of columns in input_array, the value is defined within the main function
     :type col_row: integer

     """
    #an array is defined to convert '1' and '0' values in the input_array to 'x' and '-'
    arr_prnt = [["-" for i in range(num_col)] for j in range(num_row)]
    #read values in each cell in each row
    for i in range(num_col):
        for j in range(num_row):
            #if the value in the input array is '1' (cell is turned on) then print an X
            if input_array[j][i] == 1:
                arr_prnt[j][i] = 'X'
            #if not print a '-'
            else:
                arr_prnt[j][i] = '-'
    # print the grid based on 'x' or '-' saved in the arr_prnt grid
    for num_row in arr_prnt:
        print(*num_row, sep ='', end = '\n')
    #printing a line break to have some space between each iteration
    print("\n")

#defining the main function
def main():
    """This is the main executable function of this script

     this function reads in the initial conditions specifies by the user for the game of life.
     splits the "coordinates " given by the user to read the column and row numbers seperately.
     the input_array is defined within this function as a 2D list(array)

     """
    #a string to count the number of all arguments that is given by the user. a specific number of arguments are not unpacked using argv.
    all_args = len(argv)
    #the script is the first element in argv
    script = argv[0]
    #the second element unpacked from argv provides the number of iterations for the program
    ticks = argv[1]
    #the 3rd to final arguments (all_args used as the length may vary) indicated the 'coordinates; of the cells that are 'on' initially
    initial = argv[2:all_args]

    # make a grid - as a 2D list/array (30 X 80) :
    rows, cols = (30, 80)
    #defining the initial array
    arr = [[0 for i in range(cols)] for j in range(rows)]

    # initialize the array(2D list)
    for i in initial:
        #split the given initial coordinate (separated by a ':') and save row and column coordinates separately
        row_coordinate = int(i.split(":")[0])
        column_coordinate = int(i.split(":")[1])
        #cell in the top-left has  to have an index of 1:1, meaning every given coordinate(index) has to be reduced by 1
        arr[row_coordinate-1][column_coordinate-1] = 1
    # call in the print_grid function to print the starting point, using user defined conditions
    print_grid(arr, rows, cols)


    #definint a string to count in the number of iterations
    count = 0
# a while loop to repeat the program for the number of “ticks” that was initially specified
    while count <= int(ticks)-1:
         #initializing the neighbor_sum array to save the number of 'on' neighbor cells for each cell in the array
         neighbor_sum = [[0 for i in range(cols)] for j in range(rows)]
         #calling in count_neighbors function
         count_neighbors(arr, neighbor_sum, rows, cols)
         #apply the rules to the grid using apply_rules function based on cell counts in neighbor_sum array
         apply_rules(arr, neighbor_sum, rows, cols)
         #count in the number of iterations
         count += 1
         #printing the iteration number - for clarity
         print(f"Iteration Number -  {count}" )
         #print the grid after every iteration - calling in the print_grid function
         print_grid(arr, rows, cols)

#calling in main function
main()
