def isXmas(grid, i, j, iOffset, jOffset): 
    for m, c in enumerate("XMAS"):
        checkI = i + iOffset*m
        checkJ = j + jOffset*m
        if checkI < 0 or checkJ < 0 or checkI >= len(grid) or checkJ >= len(grid[i]) or grid[checkI][checkJ] != c:
            return 0
    return 1

def check(grid, i, j):
    score = 0
    for (iOffset, jOffset) in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        score += isXmas(grid, i, j, iOffset, jOffset)
    return score


def part_one(input_str: str):
    grid = input_str.split("\n") 
    score= 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            score += check(grid,i ,j)
    return score

def checkXmas(grid, i, j):
    if i - 1 < 0 or j - 1 < 0 or i + 1 >= len(grid) or j + 1 >= len(grid[i]):
        return 0
    
    word1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
    word2 = grid[i+1][j-1] + grid[i][j] + grid[i-1][j+1]

    if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
        return 1
    return 0


        
def part_two(input_str: str):
    grid = input_str.split("\n") 
    score= 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            score += checkXmas(grid,i ,j)
    return score
