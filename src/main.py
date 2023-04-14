from Grid import Grid
from GridTest import GridTest
from algorithm import *
from PermutationVerifier import *
#from algorithm import create_bell_shape

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
    #gridA = Grid(minX=1.6, maxX=1.62, minY=0, maxY=0.18, xRes=0.001, yRes=0.01) 
    #gridB = Grid(minX=1.05, maxX=1.55, minY=0.19, maxY=0.47, xRes=0.001, yRes=0.01)
    #gridC = Grid(minX=1.63, maxX=2.85, minY=0.48, maxY=0.76, xRes=0.001, yRes=0.01)
    #gridD = Grid(minX=1.6, maxX=1.62, minY=0.77, maxY=0.95, xRes=0.01, yRes=0.01)

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
    rows = 5
    cols = 5
    grid = np.zeros((rows, cols), dtype=int)
    result = generate_combinations_recursion(grid)
    print(result)

    ######### RULE TESTS ##############
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
    ]'''

   # print(len(ruleTestData))
      # Filter sets to only contain sets that follows the right lane change (first C shape) definition
   # cleaned = []
   # for combination in ruleTestData:
   #     if verify_permutation(combination):
   #        cleaned.append(combination)
   # print(len(cleaned))
# TODO: Make grid creation dynamic (younis)
# TODO: Max bell shaped curve rules (gimmmmmmmy)
# TODO: make straight drive perm rules
# TODO: [evaluation] export (maybe csv files) and plot to see result

if __name__ == "__main__":
    main()