from utils import *
import numpy as np
from decimal import Decimal

def setup_boundary_grid(minX, maxX, minY, maxY, xRes, yRes, output):
    """
    Setsup the boundaries and grid to permutate on

    :param minX: Defines the lowest morton value for the grid (x-axis).
    :param maxX: Defines the maximum morton value for the grid (x-axis).
    :param minY: Defines the lowest timestamp value for the grid (y-axis). 
    :param maxY: Defines the maximum timestamp value for the grid (y-axis).
    :columns: Defines the number of columns to split the grid by
    :rows: Defines the number of rows to split the grid by
    """

    columns = int((maxX-minX)/xRes) + 1
    rows = int((maxY-minY)/yRes) + 1

    # define the grid for the scatter points
    grid = [[0 for i in range(columns)] for i in range(rows)]

    # Code adapted from https://stackoverflow.com/questions/6189956/easy-way-of-finding-decimal-places
    # Get the decimal places to help round the values properly to the chosen resolution.
    xAxisDp = int(Decimal(str(xRes)).as_tuple().exponent) * -1
    yAxisDp = int(Decimal(str(yRes)).as_tuple().exponent) * -1

    xAxis = prepare_x_axis(minX, maxX, xRes, columns, xAxisDp)
    yAxis = prepare_y_axis(minY, maxY, yRes, rows, yAxisDp)

    # output the grid and axis
    if output:
        print("grid: \n")
        for row in grid:
            print(row)
        print('-------------------')

        print("xAxis: \n") 
        print(xAxis)
        print('-------------------')
        
        print("yAxis: \n")
        for row in reversed(yAxis): 
            print(row)
        print('-------------------')
    return grid, xAxis, yAxis

def setup_boundary_grid_test(minX, maxX, minY, maxY, xRes, yRes, output):
    """
    Setsup the boundaries and grid to permutate on

    :param minX: Defines the lowest morton value for the grid (x-axis).
    :param maxX: Defines the maximum morton value for the grid (x-axis).
    :param minY: Defines the lowest timestamp value for the grid (y-axis). 
    :param maxY: Defines the maximum timestamp value for the grid (y-axis).
    :columns: Defines the number of columns to split the grid by
    :rows: Defines the number of rows to split the grid by
    """

    

    

    # Code adapted from https://stackoverflow.com/questions/6189956/easy-way-of-finding-decimal-places
    # Get the decimal places to help round the values properly to the chosen resolution.
    xAxisDecimalPlaces = int(Decimal(str(xRes)).as_tuple().exponent) * -1
    yAxisDecimalPlaces = int(Decimal(str(yRes)).as_tuple().exponent) * -1
    print(xAxisDecimalPlaces)
    print(yAxisDecimalPlaces)

    # Generate the values between the max and minimum x/y values based on the specific resolution.
    #TODO: precision issue!!!
    #xAxis = np.round(np.arange(minX, maxX + xRes, xRes), xAxisDecimalPlaces)
    #yAxis = np.round(np.arange(minY, maxY + yRes, yRes), yAxisDecimalPlaces)

    columns = len(xAxis)
    rows = len(yAxis)

    # define the grid for the scatter points
    grid = [[0 for i in range(columns)] for i in range(rows)]


    # output the grid and axis
    if output:
        print("grid: \n")
        for row in grid:
            print(row)
        print('-------------------')

        print("xAxis: \n") 
        print(xAxis)
        print('-------------------')
        
        print("yAxis: \n")
        for row in reversed(yAxis): 
            print(row)
        print('-------------------')
    return grid, xAxis, yAxis