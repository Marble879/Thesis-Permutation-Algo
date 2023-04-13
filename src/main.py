from Grid import Grid
from GridTest import GridTest
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
    gridA = Grid(minX=1.6, maxX=1.62, minY=0, maxY=0.18, xRes=0.001, yRes=0.01) 
    gridB = Grid(minX=1.05, maxX=1.55, minY=0.19, maxY=0.47, xRes=0.001, yRes=0.01)
    gridC = Grid(minX=1.63, maxX=2.85, minY=0.48, maxY=0.76, xRes=0.001, yRes=0.01)
    gridD = Grid(minX=1.6, maxX=1.62, minY=0.77, maxY=0.95, xRes=0.01, yRes=0.01)
    #print("----- GRID TEST ------")
    #gridTest = GridTest(minX=1.6, maxX=1.62, minY=0, maxY=0.18, xRes=0.01, yRes=0.01)



# TODO: Make grid creation dynamic (younis)
# TODO: Max bell shaped curve rules (gimmmmmmmy)
# TODO: make straight drive perm rules
# TODO: [evaluation] export (maybe csv files) and plot to see result

if __name__ == "__main__":
    main()