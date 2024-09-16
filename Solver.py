# Levels of intelligence
# 1. Pick the possible sums for rows and cols
# 2. If a subset is valid and unique keep it
# 3. (current) If a value appears in all the subset with correct sum keep it

def PrintGrid(grid):
    for i,row in enumerate(grid):
        print(i+1, end=' ')
        for val in row:
            print(val, end='\t')
        print('\n')

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
    # First count the correct values.
    sum = 0
    for j in range(len(result)):
        if row and result[i][j] == 2:
            sum += grid[i][j]
        if not row and result[j][i] == 2:
            sum += grid[j][i]

    n = len(usable)
    for j in range(n):
        if (s & (1<<j)) != 0:
            sum += (grid[i][usable[j]] if row else grid[usable[j]][i])
    return sum

# Return position of valid numbers in a row/column.
# Only count as usable the 'maybe' values.
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

def DoIter(result, grid, n, targets, row):
    for i in range(n):
        # create list of values I can use.
        usable = GetUsable(result, i, row=row)
        new_result = [0] * n
        n_matches = 0

        # If a value appears in all matches it's correct
        valueOccurance = [0] * len(usable)

        # Try all permutations of usable values.
        for s in range(1, 1<<len(usable)):
            sumTarget = SumSequence(i, s, usable, grid, result, row=row)
            if sumTarget == targets[i]:
                n_matches += 1
                for j in range(len(usable)):
                    if (s & (1<<j)) != 0:
                        new_result[usable[j]] = 1
                        valueOccurance[j] += 1

        # Set as correct all the values that appear in all possible solutions.
        if n_matches != 0:
            for j in range(len(usable)):
                if valueOccurance[j] == n_matches:
                    new_result[usable[j]] = 2
        if row:
            for j in range(len(usable)):
                result[i][usable[j]] = new_result[usable[j]]
        else:
            for j in range(len(usable)):
                result[usable[j]][i] = new_result[usable[j]]
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
    # Result contains 0 if value is not valid, 1 if could be, 2 if it's correct.
    result = [[1] * n for _ in range(n)]
    i = 0
    max_iter = 20
    while (not CheckResult(result, grid, row_targets, col_targets)
            and i < max_iter):
        result = DoIter(result, grid, n, row_targets, row=True)
        result = DoIter(result, grid, n, col_targets, row=False)
        i += 1

    # If solution is not found do nothing
    if i == max_iter:
        print("Solution not found")
        print(result)
        exit()
    PrintGrid(result)
    return ResultConversion(result)