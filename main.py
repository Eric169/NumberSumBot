from Solver import Solve, PrintGrid

test_grid_5 = [
    [1, 3, 7, 5, 9],
    [2, 8, 6, 7, 3],
    [1, 4, 4, 3, 2],
    [7, 6, 6, 1, 4],
    [8, 4, 3, 1, 7]
]
test_row_targets_5 = [1, 16, 7, 16, 9]
test_col_targets_5 = [9, 10, 12, 11, 7]


test_grid_7 = [
    [9, 9, 9, 3, 7, 4, 8],
    [7, 6, 2, 9, 6, 1, 7],
    [3, 2, 1, 6, 6, 2, 3],
    [8, 8, 2, 7, 2, 6, 6],
    [7, 8, 4, 2, 2, 1, 8],
    [1, 9, 9, 9, 4, 9, 1],
    [4, 6, 5, 9, 4, 6, 1]
]

test_row_targets_7 = [20, 23, 8, 9, 4, 27, 20]
test_col_targets_7 = [10, 11, 24, 30, 4, 17, 15]


test_grid_6 = [
    [8, 9, 3, 7, 2, 3],
    [5, 4, 8, 5, 7, 5],
    [3, 7, 8, 9, 2, 7],
    [2, 8, 9, 3, 9, 4],
    [9, 2, 8, 6, 8, 8],
    [5, 6, 3, 1, 2, 5]
]
test_row_targets_6 = [27, 10, 11, 21, 10, 5]
test_col_targets_6 = [18, 11, 20, 19, 11, 5]

if __name__=="__main__":
    grid = [
        [3, 1, 2],
        [1, 7, 6],
        [1, 5, 3]
    ]
    n = len(grid)
    row_targets = [4, 7, 3]
    col_targets = [3, 8, 3]

    # solution = Solve(grid, row_targets, col_targets)
    n = len(test_grid_7)
    solution = Solve(test_grid_7, test_row_targets_7, test_col_targets_7)
    PrintGrid(solution)
