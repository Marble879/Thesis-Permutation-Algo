#TODO: MAKE ACCESS SPECIFIC X COORDINATE OF current/next coordinate!!!!!!!!

# 1. Does x go down from previous point?
def check_coordinate_decrease(currentCoordinate, nextCoordinate):
    return currentCoordinate > nextCoordinate 

# 2. Does x go up from previous point?
def check_coordinate_increase(currentCoordinate, nextCoordinate):
    return currentCoordinate < nextCoordinate 

# 3. Does x remain the same from previous point?
def check_coordinate_same(currentCoordinate, nextCoordinate):
    return currentCoordinate == nextCoordinate 