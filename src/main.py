from Grid import Grid
from GridTest import GridTest
import numpy as np
#from algorithm import *
from PermutationVerifier import *
from algorithm import generate_combinations_right_bell_recursion
from algorithm import generate_combinations_left_bell_recursion
from algorithm import generate_straight
from algorithm import generate_boxes_permutations
from PermutationConverter import *

'''
PSEUDOCODE FOR ALGORITHM:
input: Grid


for i in rows
    randomCol = random(0, cols)
    grid[i][randomCol] = 1
for each row:
    make permutation
    get coordinates for each posiition of 1 (output is set of array indexes)


    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    run all of the rules
    if all rules pass, return/save set (saving can be done once we connect on monday, but could print some and see how they look)


output of algo at end: Morton and Timestamp for each of the lane changes. (after permutations)

'''

'''
PSEUDOCODE FOR RULES:
make function for each rule
can use a set to see if indexes of array respect the rules or not.

'''
def main():
    #gridA = Grid(minX=1.6, maxX=1.62, minY=0, maxY=0.18, xRes=0.01, yRes=0.01) # rows: 2 (0.0 -> 0.1), cols: 1 (1.6) #TODO (can incldue in thesis text if have to expalin graph): start 0.0 as its artificial time range. Ie lane change happens after certain time has occured, we just cut out as close to what we consider lane change
    #gridB = Grid(minX=1.05, maxX=1.55, minY=0.19, maxY=0.47, xRes=0.01, yRes=0.01) # rows: 3, cols: 5 (0.2 -> 0.5)
    #gridC = Grid(minX=1.63, maxX=2.85, minY=0.48, maxY=0.76, xRes=0.01, yRes=0.01)
    #gridD = Grid(minX=1.6, maxX=1.62, minY=0.77, maxY=0.95, xRes=0.01, yRes=0.01)

    gridA = Grid(minX=1.6, maxX=1.6, minY=0, maxY=0.1, rows=2, cols=1, dp=1) # rows: 2 (0.0 -> 0.1), cols: 1 (1.6) #TODO (can incldue in thesis text if have to expalin graph): start 0.0 as its artificial time range. Ie lane change happens after certain time has occured, we just cut out as close to what we consider lane change
    gridB = Grid(minX=1.1, maxX=1.5, minY=0.2, maxY=0.4, rows=3, cols=5, dp=1) # rows: 3, cols: 5 (0.2 -> 0.5)
    gridC = Grid(minX=1.7, maxX=2.8, minY=0.5, maxY=0.7, rows=3, cols=12, dp=1) # rows: 3, cols: 12
    gridD = Grid(minX=1.6, maxX=1.6, minY=0.8, maxY=0.9, rows=2, cols=1, dp=1) # rows: 2, cols: 1

    print(gridA.get_xAxis() , "|", gridA.get_yAxis())
    print(gridB.get_xAxis(), "|", gridB.get_yAxis())
    print(gridC.get_xAxis(), "|", gridC.get_yAxis())
    print(gridD.get_xAxis(), "|", gridD.get_yAxis())
    

    # run permutations for each red box
    gridA.set_permutations(generate_straight(gridA.grid))
    gridB.set_permutations(generate_combinations_left_bell_recursion(gridB.grid))
    gridC.set_permutations(generate_combinations_right_bell_recursion(gridC.grid))
    gridD.set_permutations(generate_straight(gridD.grid))

    # convert permutations to (morton, ts)
    gridA.set_converted_permutations(convert_permutations(gridA))
    gridB.set_converted_permutations(convert_permutations(gridB))
    gridC.set_converted_permutations(convert_permutations(gridC))
    gridD.set_converted_permutations(convert_permutations(gridD))

    # permutate all permutations of all boxes
    boxResult = generate_boxes_permutations(gridA.convertedPermutations, gridB.convertedPermutations, gridC.convertedPermutations, gridD.convertedPermutations)

    #print(boxResult)
    print(len(gridA.convertedPermutations))
    print(len(gridB.convertedPermutations))
    print(len(gridC.convertedPermutations))
    print(len(gridD.convertedPermutations))
    print("Lane changes: ", len(boxResult))



    #TODO: BUG WHEN TRYING THE FOLLOWING (X-AXIS OUTPUT IS [1.05, 1.2, 1.2, 1.4, 1.5, 1.55]):
    #gridTest = Grid(minX=1.05, maxX=1.55, minY=0.19, maxY=0.47, xRes=0.10, yRes=0.06)
    #print(gridTest.get_grid())
    #print(gridTest.get_xAxis())
    #print(gridTest.get_yAxis())
    #print("----- GRID TEST ------")
    #gridTest = GridTest(minX=1.6, maxX=1.62, minY=0, maxY=0.18, xRes=0.01, yRes=0.01)

######### Algorithm TESTS ##############
    # Algorithm test
    # generate combinations for a 2x2 array
    #rows = 8
    #cols = 8
    #grid = np.zeros((rows, cols), dtype=int)
    #result = generate_combinations_left_bell_recursion(grid)
    #print(result)

    #rows = 3
   # cols = 2
   # grid = np.zeros((rows, cols), dtype=int)
    #result = generate_combinations_right_bell_recursion(grid)
    #print(result)

    # TEST GENERATE PERMUTATIONS
  #  boxA = [[(0, 0), (0, 2)], [(1, 0), (1, 2)]]
   # boxB = [[(4, 5), (5, 4)], [(3, 4), (4, 3)]]
   # boxC = [[(6, 7), (7, 6)], [(8, 9), (9, 8)]]
    #boxD = [[(10, 11), (11, 10)], [(12, 13), (13, 12)]]
    
   # boxResult = generate_boxes_permutations(boxA, boxB, boxC, boxD)
   # print ("boxes result\n", boxResult)

    



    ######### RULE TESTS ##############
    ###### LEFT BELL #######
    #### 5x5####
    #ruleTestData = [[(4, 0), (3, 1), (2, 2), (3, 3), (4, 4)]] #VALID
    #ruleTestData = [[(4, 0), (3, 1), (3, 2), (3, 3), (4, 4)]] #VALID
    #ruleTestData = [[(4, 0), (3, 1), (3, 2), (3, 3), (4, 4)]] #VALID
    #ruleTestData = [[(2, 0), (1, 1), (0, 2), (1, 3), (2, 4)]] #VALID
    #ruleTestData = [[(2, 0), (1, 1), (2, 2), (3, 3), (4, 4)]] #VALID
    #ruleTestData = [[(4, 0), (1, 1), (1, 2), (2, 3), (3, 4)]] #VALID
    #ruleTestData = [[(4, 0), (3, 1), (0, 2), (3, 3), (4, 4)]] #VALID
    #ruleTestData = [[(4, 0), (3, 1), (0, 2), (2, 3), (3, 4)]] #VALID

    #ruleTestData = [[(4, 0), (3, 1), (4, 2), (3, 3), (4, 4)]] #INVALID
    #ruleTestData = [[(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]] #INVALID
    #ruleTestData = [[(0, 0), (1, 1), (2, 2), (1, 3), (0, 4)]] #INVALID
    #ruleTestData = [[(3, 0), (3, 1), (3, 2), (3, 3), (4, 4)]] #INVALID

    #### 3x3 ####
    #ruleTestData = [[(2, 0), (1, 1), (2, 2)]] #VALID
    #ruleTestData = [[(2, 0), (0, 1), (2, 2)]] #VALID
    #ruleTestData = [[(1, 0), (0, 1), (1, 2)]] #VALID

    #ruleTestData = [[(0, 0), (0, 1), (1, 2)]] #INVALID
    #ruleTestData = [[(1, 0), (2, 1), (1, 2)]] #INVALID
    #ruleTestData = [[(0, 0), (1, 1), (2, 2)]] #INVALID

    '''   
    ruleTestData = [
    [(4, 0), (3, 1), (2, 2), (3, 3), (4, 4)],
    [(4, 0), (3, 1), (3, 2), (3, 3), (4, 4)],
    [(4, 0), (3, 1), (3, 2), (3, 3), (4, 4)],
    [(2, 0), (1, 1), (0, 2), (1, 3), (2, 4)],
    [(2, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
    [(4, 0), (3, 1), (4, 2), (3, 3), (4, 4)],
    [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)],
    [(0, 0), (1, 1), (2, 2), (1, 3), (0, 4)],
    [(3, 0), (3, 1), (3, 2), (3, 3), (4, 4)]
    ]
    '''
    ###### RIGHT BELL #######
    #ruleTestData = [[(0, 0), (1, 1), (0, 2)]] #valid
    #ruleTestData = [[(4, 0), (10, 1), (0, 2)]] # valid 
    #ruleTestData = [[(6, 0), (8, 1), (1, 2)]] # valid 
    #ruleTestData = [[(6, 0), (8, 1), (11, 2)]] # invalid 
    #ruleTestData = [[(0, 0), (1, 1), (2, 2)]] # invalid
    #ruleTestData = [[(0, 0), (0, 1), (0, 2)]] # invalid
    #ruleTestData = [[(3, 0), (4, 1), (4, 2)]] # invalid
    #ruleTestData = [[(5, 0), (4, 1), (5, 2)]] # invalid

    #print(len(ruleTestData))
      # Filter sets to only contain sets that follows the right lane change (first C shape) definition
    #cleaned = []
    #for combination in ruleTestData:
    #    if verify_permutation_right_bell(combination):
    #       cleaned.append(combination)
    #print(len(cleaned))
# TODO: Make grid creation dynamic (younis)
# TODO: Max bell shaped curve rules (gimmmmmmmy)
# TODO: make straight drive perm rules
# TODO: [evaluation] export (maybe csv files) and plot to see result

if __name__ == "__main__":
    main()