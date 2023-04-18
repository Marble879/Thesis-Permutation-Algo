def convert_permutations(grid):
    convertedPermutations = []
    for permutations in grid.get_permutations():
        convertedCoords = []
        for coordinate in permutations:
            convertedCoords.append((grid.xAxis[coordinate[0]], grid.yAxis[coordinate[1]]) )
        convertedPermutations.append(convertedCoords)
    return convertedPermutations