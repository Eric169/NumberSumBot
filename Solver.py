# Levels of intelligence
# 1. Pick the possible sums for rows and cols
# 2. (current) if a subset is valid and unique keep it
# 3. If a value appears in all the subset with correct sum keep it

def PrintGrid(grid):
    for row in grid:
        print(row)

def CheckResult(result, grid, row_targets, col_targets):
    n = len(grid)
    for i in range(n):
        sumRow = sumCol = 0
        for j in range(n):
            if result[i][j] == 2:
                sumRow += grid[i][j]
            if result[j][i] == 2:
                sumCol += grid[j][i]
        if sumRow != row_targets[i] or sumCol != col_targets[i]:
            return False
    return True

def SumSequence(i, s, usable, grid, result, row):
    # First count the correct values
    sum = 0
    for j in range(len(result)):
        if row and result[i][j] == 2:
            sum += grid[i][j]
        if not row and result[j][i] == 2:
            sum += grid[j][i]
    if i == 1:
        print('sum', sum)
    n = len(usable)
    for j in range(n):
        if (s & (1<<j)) != 0:
            sum += (grid[i][usable[j]] if row else grid[usable[j]][i])
    return sum

# Return position of valid numbers in a row/column
# Only count as usable the 'maybe' values
def GetUsable(result, i, row):
    usable=[]
    n = len(result)
    if row:
        for j in range(n):
            if result[i][j] == 1:
                usable.append(j)
    else:
        for j in range(n):
            if result[j][i] == 1:
                usable.append(j)
    return usable

def DoRows(result, grid, n, row_targets):
    print("Do rows")
    for i in range(n):
        # create list of values I can use
        usable = GetUsable(result, i, row=True)
        # print(i, 'usable', usable)
        new_result = [0] * n
        n_matches = 0
        # Try all permutations of usable values
        # LSB is row usable[0]
        for s in range(1, 1<<len(usable)):
            sumRow = SumSequence(i, s, usable, grid, result, row=True)
            # print('s', s, sumRow)
            if sumRow == row_targets[i]:
                n_matches += 1
                for j in range(len(usable)):
                    new_result[usable[j]] = (
                        1 if (s & (1<<j)) != 0 else new_result[usable[j]]
                    )
        
        # If I found only one match then it's the correct one
        if n_matches == 1:
            for j in range(len(new_result)):
                if new_result[j] == 1: new_result[j] = 2
        for j in range(n):
            result[i][j] = new_result[j] if result[i][j] != 2 else result[i][j]
        # print('new result')
        # PrintGrid(result)
    return result

def DoCols(result, grid, n, col_targets):
    print("Do cols")
    for i in range(n):
        # create list of values I can use
        usable = GetUsable(result, i, row=False)
        print(i, 'usable', usable)
        new_result = [0] * n
        n_matches = 0
        # Try all permutations of usable values
        for s in range(1, 1<<len(usable)):
            sumCol = SumSequence(i, s, usable, grid, result, row=False)
            if i == 1: print('s', s, 'sumcol',sumCol)
            if sumCol == col_targets[i]:
                n_matches += 1
                for j in range(len(usable)):
                    new_result[usable[j]] = (
                        1 if (s & (1<<j)) != 0 else new_result[usable[j]]
                    )
        # print('col result', new_result)

        # If I found only one match then it's the correct one
        if n_matches == 1:
            for j in range(len(new_result)):
                if new_result[j] == 1: new_result[j] = 2

        for j in range(len(usable)):
            result[usable[j]][i] = new_result[usable[j]]
        # print('new result')
        # PrintGrid(result)
    return result

def ResultConversion(result):
    n = len(result)
    solution = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            solution[i][j] = result[i][j] == 2
    return solution

def Solve(grid, row_targets, col_targets):
    n = len(grid)
    # Result contains 0 if value is not valid, 1 if could be, 2 if it's correct
    result = [[1] * n for _ in range(n)]
    i = 0
    while not CheckResult(result, grid, row_targets, col_targets) and i < 10:
        result = DoRows(result, grid, n, row_targets)
        PrintGrid(result)
        result = DoCols(result, grid, n, col_targets)
        PrintGrid(result)
        i += 1
        print(i)
    return ResultConversion(result)