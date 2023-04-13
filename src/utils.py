def prepare_x_axis(minX, maxX, xRes, columns, dp):
    """
    Setsup the x-axis for a grid based on the maximum axis values and number of columns 

    :param minX: Defines the lowest morton value for the grid (x-axis).
    :param maxX: Defines the maximum morton value for the grid (x-axis).
    :columns: Defines the number of columns to split the axis by
    :xRes: Defines the resolution/scale of the xAxis, from which the values between minX and maxX are calculated
    """
    # Create a single array to represent the X-axis
    xAxis = [0 for i in range(columns)]
    xAxis[0] = minX # Assign lowest bound of morton value
    xAxis[columns-1] = maxX # Assign highest bound of morton value

    # Subtract the first and last column to determine how many columns need to be assigned an axis value
    numOfBetweenColumns = columns-2 
    # Calculate the interval between the max and minimum value so that axis in between can be filled
    #interval = (maxX - minX) / (len(xAxis) - 1)
    # Fill axis between max and minimum
    for i in range(len(xAxis) - 1):
        if xAxis[i] == 0:
            xAxis[i] = round(minX + (i*xRes), dp)
    return xAxis


def prepare_y_axis(minY, maxY, yRes, rows, dp):
    """
    Setsup the y-axis for a grid based on the maximum axis values and number of columns 

    :param minY: Defines the lowest timestamp value for the grid (y-axis). 
    :param maxY: Defines the maximum timestamp value for the grid (y-axis).
    :rows: Defines the number of rows to split the axis by
    """
    # Create a single array to represent the Y-axis
    yAxis = [0 for i in range(rows)]
    yAxis[0] = minY # Assign lowest bound of morton value
    yAxis[rows-1] = maxY # Assign highest bound of morton value
    
    # Subtract the first and last row to determine how many rows need to be assigned an axis value
    numOfBetweenRows = rows-2 
    # Calculate the interval between the max and minimum value so that axis in between can be filled
    #interval = (maxY - minY) / (len(yAxis) - 1)
    # Fill axis between max and minimum
    for i in range(len(yAxis) - 1):
        if yAxis[i] == 0:
            yAxis[i] = round(minY + (i*yRes), dp)
    
    return yAxis