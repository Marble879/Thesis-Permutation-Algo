from boundaryGenerator import setup_boundary_grid_test

class GridTest:

    grid = None
    xAxis = None
    yAxis = None 


    def __init__(self, minX, maxX, minY, maxY, xRes, yRes):
        self.grid, self.xAxis, self.yAxis = setup_boundary_grid_test(minX, maxX, minY, maxY, xRes, yRes, True)

    
    def get_grid():
        return self.grid

    def get_xAxis():
        return self.xAxis

    def get_yAxis():
        return self.yAxis