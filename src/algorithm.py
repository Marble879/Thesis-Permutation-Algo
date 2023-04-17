import numpy as np
import itertools

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

# This method takes an empty 2D array as argument and returns a set of sets.
# Each set contains coordinates for random permutations within the array
# Uses recursion to only generate valid combinations according to the row constraint
# Time complexity: O(rows*2^columns) (to prove)
# Uses list containing set of coordinates
# Output sorted bottom to top
def generate_combinations_recursion(arr):
    rows, cols = arr.shape

    def backtrack(curr_row):
        nonlocal valid_combinations

        # if we've reached the last row, add the current combination to the list of valid combinations
        if curr_row == rows:
            valid_combinations.append([(j, i) for i in range(rows) for j in range(cols) if arr[i][j] == 1])
            return

        # try all possible combinations for the current row
        for j in range(cols):
            # check if the current cell is empty
            if arr[curr_row][j] == 0:
                # place a 1 in the current cell
                arr[curr_row][j] = 1

                # backtrack to the next row
                backtrack(curr_row+1)

                # remove the 1 from the current cell to explore other possibilities
                arr[curr_row][j] = 0

    # create a list to store the valid combinations
    valid_combinations = []

    # start backtracking from the first row
    backtrack(0)

    # sort the combinations from bottom right to top left
    valid_combinations.sort(key=lambda x: (-x[0][0], -x[0][1]))

    return valid_combinations


#x= ay^2+b
#each a and b combo, a new parabula
#each y (timestamp - row) -> x (morton value - column)
#return set of coordinates
#given the requirements above make into code
def generate_parabula(coeff, offset):
    plot = set
    return plot
