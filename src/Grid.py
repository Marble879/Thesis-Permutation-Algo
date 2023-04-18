from boundaryGenerator import setup_boundary_grid
from boundaryGenerator import setup_boundary_grid_row_col

class Grid:

    grid = None
    xAxis = None
    yAxis = None 
    permutations = None
    convertedPermutations = None


    def __init__(self, minX, maxX, minY, maxY, rows, cols, dp):
        #self.grid, self.xAxis, self.yAxis = setup_boundary_grid(minX, maxX, minY, maxY, xRes, yRes, output=False)
        self.grid, self.xAxis, self.yAxis = setup_boundary_grid_row_col(minX, maxX, minY, maxY, rows, cols, dp, output=False)

    
    def get_grid(self):
        return self.grid

    def get_xAxis(self):
        return self.xAxis

    def get_yAxis(self):
        return self.yAxis

    def set_permutations(self, permutations):
        self.permutations = permutations

    def get_permutations(self):
        return self.permutations

    def set_converted_permutations(self, convertedPermutations):
        self.convertedPermutations = convertedPermutations
        print(self.permutations)
        print("--------------------------------------")
        print(self.convertedPermutations)
        print("====================================")

    def get_converted_permutations(self):
        return self.convertedPermutations

    