# Module to help perform digital logic calculations
# Micah Tseng
# tseng.micah@gmail.com

# Requites numpy
import numpy as np

'''
Things to Implement:
    - More standard arrays
    - A function to output the data to a csv file
    - More flip flop application tables
    - logic units for flip flops? 
'''
# Define standard arrays
two = np.array([[0],
                [1]])

four = np.array([[0,0],
                [0,1],
                [1,0],
                [1,1]])

eight = np.array([[0,0,0],
                [0,0,1],
                [0,1,0],
                [0,1,1],
                [1,0,0],
                [1,0,1],
                [1,1,0],
                [1,1,1]])

sixteen = np.array([[0,0,0,0],
                    [0,0,0,1],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,1,0,0],
                    [0,1,0,1],
                    [0,1,1,0],
                    [0,1,1,1],
                    [1,0,0,0],
                    [1,0,0,1],
                    [1,0,1,0],
                    [1,0,1,1],
                    [1,1,0,0],
                    [1,1,0,1],
                    [1,1,1,0],
                    [1,1,1,1]])
'''
TPRINT
    Parameters
        data        A tuple, holding the set of arrays to be printed. Rows must be equal.
        labels      A list of each label in the order of left to right
    Returns
        nothing...just pretty printing

Note: If things look off, it's probably because you didn't enter something in correctly...
'''

def tprint(data, labels):
    # list of the spacing for each row
    spacing = []
    # The total sum of the above spacing
    total_pad = 0
    # total number of data columns
    columns = 0

    # Get all thel spacing for the labels
    for i in range(0,len(labels)):
        # Start a spacing variable 
        spacing.append(0)
        # Check to see if you need to print the deviding line
        for n in labels[i]:
            # Print the label, incromenting the spac counter to find the spacing
            spacing[i] += 1

        total_pad += spacing[i]

    # Take care of the possiblity the user was lazy and didn't want to label every coumn
    # first get the total number of columns in the data
    for data_set in data:
        columns += data_set.shape[1]
    # Compare the columns with the number of the spacing entries and make ammends
    while len(spacing) < columns:
        labels.append(' ')
        spacing.append(1)
        total_pad += 1

    # Print out the top bar
    for i in range(0, total_pad + len(spacing) +  2 * len(data)):
        print("=", end = '', flush=True)
    print("=")

    # Print out the label header
    print("| ", end = '', flush = True)
    # i is the iterator through the labels
    i = 0
    for data_set in data:
        for k in range(0, data_set.shape[1]):
            for n in labels[i]:
                # Print the label, incromenting the spac counter to find the spacing
                print(n, end = '', flush = True)
            print(' ', end = '', flush = True)
            i += 1
        print("| ", end = '', flush = True)
    print('')
    

    # Print out the deviding bar
    for i in range(0, total_pad + len(spacing) +  2 * len(data)):
        print("-", end = '', flush=True)
    print("-")

    # Prinit out the data
    # Iterate over each row in the first data set...is this good? No. But I'm lazy
    for i in range(0, data[0].shape[0]):
        # k is the iterator through the spacing
        k = 0
        # Go through each data set
        for data_set in data:
            print("| ", end = '', flush = True)
            # Print out the appropriate row with the correct spacing
            for n in range(0, data_set.shape[1]):
                if data_set[i,n] == 9:
                    print('-' ,end = '', flush = True)
                elif data_set[i,n] == 8:
                    print('F' ,end = '', flush = True)
                else:
                    print(str(data_set[i,n].tolist()).strip('[],').replace(',', '') ,end = '', flush = True)
                for a in range(0,spacing[k]):
                    print(" ", end = '', flush = True)
                k += 1
           
        print("| ", end = '\n', flush = True)

  
    # Print out the bottom bar
    for i in range(0, total_pad + len(spacing) +  2 * len(data)):
        print("=", end = '', flush=True)
    print("=")



'''
APP_TABLE
    Parameters: 
        ff          The type of flip flop: jk
        present_s   An array with the values of the present state
        next_s      An array with the values of the next state
    Returns:
        An appropriatly sized array with the application table of the respective flip flop state tables

Due to the nature of integer arrays and my own lazyness, the following is the key for the returning 
values. If you use tprint() to print them, ignore this:
        0 -> 0
        1 -> 1
        8 -> forbidden
        9 -> Don't care
'''
def app_table(ff, present_s, next_s):

    if present_s.shape != next_s.shape:
        print("********************************")
        print("The present state and next state\narrays are of mismatched shape.")
        print("This won't work. Fix it.\n********************************")

        return

    if ff == 'jk' or ff == 'JK':
        (row, column) = present_s.shape
        jk = np.zeros((row, 2 * column), dtype = int)

        for x in range(0,row):
            for y in range(0,column):
                
                if present_s[x,y] == 0 and next_s[x,y] == 0:
                    jk[x,2*y] = 0
                    jk[x,2*y+1] = 9 
                elif present_s[x,y] == 0 and next_s[x,y] == 1:
                    jk[x,2*y] = 1
                    jk[x,2*y+1] = 9
                elif present_s[x,y] == 1 and next_s[x,y] == 0:
                    jk[x,2*y] = 9 
                    jk[x,2*y+1] = 1
                elif present_s[x,y] == 1 and next_s[x,y] == 1:
                    jk[x,2*y] = 9 
                    jk[x,2*y+1] = 0

        return jk 
    else:
        print("Either the type of FF you are asking for is not implemented or you screwed up typing")
        return np.zeros(present_s.shape, dtype=int)

'''
Due to the fact that numpy stores int arrays as signed 8 bit arrays and the ~ funciton in python takes
the 2' complement, it is necesary to create a function (this one) that can take the one's comp of an 
array of one bit values.

'''
def b(base):
    # Get the shape of the inputed array
    shape = base.shape
    # instatiate a new array of the same shape
    comp = np.zeros(shape, dtype = int)

    # This iteration uses the nditter numpy function to go through the array see:
    # https://docs.scipy.org/doc/numpy/reference/arrays.nditer.html 
    it = np.nditer(base, flags=['multi_index'])
    while not it.finished:
        if it[0] == 0:
            comp[it.multi_index] = 1
        else:
            comp[it.multi_index] = 0

        it.iternext()

    # Return the new array
    return comp


    
# testing
inputs = eight
outputs = eight
if __name__ == "__main__": 
    label = ['A', 'B', 'C', 'A+', 'B+', 'C+', 'j', 'k', 'j', 'k', 'j', 'k'  ]
    tprint((inputs, b(outputs), app_table('jk', inputs, b(outputs))), label)
#    print(app_table('jk', sixteen, sixteen))


