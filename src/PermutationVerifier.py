from PermutationRules import *


def verify_permutation(permutationOfPoints) -> bool:

    # instantiate key point trackers.
    # Will be used to verify that all key points
    # are included in order to confirm if the curve
    # is a valid curve. 
    entryPoint = 0 # set to 1 as first point will always be entry point
    peakPoint = 0
    exitPoint = 0
    # Loop through each coordiante point.
    # Stop one index early to prevent out of bounds error.
    for i in range(len(permutationOfPoints)-1):
        #print("(",permutationOfPoints[i][0],"|",permutationOfPoints[i+1][0],")") # TESTING CODE
        # Check if we are still in an entry point
        if check_coordinate_decrease(permutationOfPoints[i][0], permutationOfPoints[i+1][0]):
            if exitPoint > 0 or peakPoint > 0:
                return False
            entryPoint+=1 # Increment as potential peak found
        # Check if we are going into an exit point and we have not had an entry, or peak yet
        elif check_coordinate_increase(permutationOfPoints[i][0], permutationOfPoints[i+1][0]) and entryPoint > 0:
            exitPoint+=1
            peakPoint+=1
        # Check if we are in a same point
        elif check_coordinate_same(permutationOfPoints[i][0], permutationOfPoints[i+1][0]):
            peakPoint+=1
    
    if not exitPoint or not peakPoint or not entryPoint:
        return False
    else:
        return True


           

        
    # Define Entry detection, Peak detection, Exit detection variables
    # Increment entry detection (first value is always entry)
    # check if the next values go up in y axis and down in x axis.
        # NO: return false 
        # YES: Increment  Peak by 1
            # Check if next values go down or same in xaxis:
                # No: check if x axis increase and go up in yaxis
                # Yes: keep peak same
                    #: No:         
    # at end of iterations, must have at least 1 peak, 1 entract and 1 exit MINIMUM