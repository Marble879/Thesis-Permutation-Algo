from boundaryGenerator import setup_boundary_grid

class Grid:

    grid = None
    xAxis = None
    yAxis = None 


    def __init__(self, minX, maxX, minY, maxY, xRes, yRes):
        self.grid, self.xAxis, self.yAxis = setup_boundary_grid(minX, maxX, minY, maxY, xRes, yRes, output=False)

    
    def get_grid():
        return self.grid

    def get_xAxis():
        return self.xAxis

    def get_yAxis():
        return self.yAxis