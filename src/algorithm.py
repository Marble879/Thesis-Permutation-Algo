import numpy as np
import itertools

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