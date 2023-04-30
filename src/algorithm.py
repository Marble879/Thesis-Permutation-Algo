import numpy as np
import itertools
from PermutationVerifier import *

# This method takes an empty 2D array as argument and returns a set of sets.
# Each set contains coordinates for random permutations within the array
# Uses recursion to only generate valid combinations according to the row constraint
# Time complexity: O(rows*2^columns)
# Uses list containing set of coordinates
# Output sorted bottom to top
def generate_combinations_bell_recursion(arr, bellSide):

    # define number of rows and columns
    rows, cols = arr.shape

    # backtracking function that traverses all rows
    def backtrack(currentRow):
        # list of combinations (declared after backtrack function)
        nonlocal combinations

        # if we've reached the last row, add the current combination to the list of all combinations
        if currentRow == rows:
            combinations.append([(j, i) for i in range(rows) for j in range(cols) if arr[i][j] == 1])
            return

        # iterate through columns
        for j in range(cols):
            # check if the current cell is empty
            if arr[currentRow][j] == 0:
                # place a 1 in the current cell
                arr[currentRow][j] = 1

                # proceed to the next row
                backtrack(currentRow + 1)

                # remove the 1 from the current cell to explore other possibilities
                arr[currentRow][j] = 0

    # create a list to store the valid combinations
    combinations = []

    # start backtracking from the first row
    backtrack(0)

    # sort the combinations from bottom right to top left
    combinations.sort(key=lambda x: (-x[0][0], -x[0][1]))

    # TODO: for testing
    print("BEFORE RULES: ")
    print(len(combinations))
    print("--------------------------------")
    
    # list containing valid combinations
    validCombinations = []
   
   # check which bell to validate combinations for
    if bellSide == "left":
        # iterate through combinations
        for combination in combinations:
            # check if current combination follows rules
            if verify_permutation_left_bell(combination):
                # add to list of valid combinations
                validCombinations.append(combination)
    elif bellSide == "right":
        for combination in combinations:
            if verify_permutation_right_bell(combination):
                validCombinations.append(combination)   
    
    # TODO: for testing
    print("AFTER RULES: ")
    print(len(validCombinations))

    return validCombinations


# This method takes a 2D array as argument and returns a set of combinations
# Each combination contains a straight driving coordinate pattern 
# Time complexity: O(columns*rows)
def generate_straight(arr):
    
    rows, cols = arr.shape

    combinations = []

    # Iterate through columns
    for i in range(cols):
        # Iterate through rows and append to combinations set
        combinations.append([(i, j) for j in range(rows)]) 
    
    return combinations
    
# This method takes 4 boxes (areas of interest) as argument
# Returns a list of all permutations that can be generated through connecting the 4 boxes
# Time complexity: O(n^y) 
#   where n = number of combinations per box (n is generic worst case), 
#         y = number of boxes (y= 4 in this case)
def generate_boxes_permutations(boxA, boxB, boxC, boxD):

    permutations = []

    # For each list from boxA (index i)
    for i in boxA:
        # For each list from boxB (index j)
        for j in boxB:
            # For each list from boxC (index k)
            for k in boxC:
                # For each list from boxD (index l)
                for l in boxD:
                    # Current permutation is the concatenation of the current combination from all boxes
                    currentPermutation = (i + j + k + l)
                    # Add current permutation to list of all permutations
                    permutations.append(currentPermutation)

    return permutations

### DIFFERENT APPROACH IDEAS BELOW - NOT IN USE ###

#x= a(y+k)^2+b
#each a and b combo, a new parabula
#each y (timestamp - row) -> x (morton value - column)
#return set of coordinates
#given the requirements above make into code
def generate_parabula(coeff, offset):
    plot = set
    return plot

### PREVIOUS IDEAS BELOW - NOT IN USE ###

# This method generates a C-shaped curve and returns it in an array
# Not used at the moment due to errors in the generation
def generate_c_shape(rows, cols, width, offset, position):
    arr = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if i == offset and j >= position and j < position + width:
                arr[i][j] = 1
            elif i > offset and i <= offset + width - 1 and j == position + width - 1:
                arr[i][j] = 1
            elif i == offset + width - 1 and j >= position and j < position + width - 1:
                arr[i][j] = 1
    return arr

# This method takes an empty 2D array as argument and returns a set of sets.
# Each set contains coordinates for random permutations within the array
# Time complexity: O(columns^rows)
# Output not sorted
# not used at the moment
def generate_combinations(arr):
    rows, cols = arr.shape

    # generate all possible combinations of 1's and 0's
    combinations = itertools.product([0, 1], repeat=rows*cols)

    # create a set to store the valid combinations
    valid_combinations = set()

    # loop through each combination and check if it satisfies the row constraint
    for c in combinations:
        # reshape the combination to a 2D array
        temp_arr = np.array(c).reshape((rows, cols))

        # check if the combination satisfies the row constraint
        if np.all(np.sum(temp_arr, axis=1) == 1):
            valid_combinations.add(frozenset((i, j) for i in range(rows) for j in range(cols) if temp_arr[i][j] == 1))

    return valid_combinations
