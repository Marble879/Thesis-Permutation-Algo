import numpy as np

# TODO:  
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
