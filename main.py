from Solver import Solve, PrintGrid
from ScreenReader import read_numbers
from math import sqrt
import pyautogui
from ppocr.utils.logging import get_logger
import logging
import time

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

def HandMadeInputSolve():
    n = int(input('n: '))
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        grid[i] = [int(x) for x in input().split()]
    row_targets = [int(x) for x in input('row ').split()]
    col_targets = [int(x) for x in input('col ').split()]

    solution = Solve(grid, row_targets, col_targets)
    PrintGrid(solution)

def ChangeStatus():
    change_point = [630,1120]
    time.sleep(2)
    pyautogui.click(change_point[0], change_point[1])
    time.sleep(2)

def ClickNumbers(solution, boxes, select):
    for i,row in enumerate(solution):
        for j in range(len(row)):
            box = boxes[i*(len(solution)+1)+j+1]
            if row[j] == select:
                pyautogui.click(box[0]+x, box[1]+y, button='left')
                time.sleep(0.8)

def Play(solution, boxes, x, y):
    boxes = boxes[len(solution):]

    ClickNumbers(solution=solution, boxes=boxes, select=True)
    ChangeStatus()
    ClickNumbers(solution=solution, boxes=boxes, select=False)
                
if __name__=="__main__":
    x,y = 350,380

    # Avoid huge logging by the ocr.
    logger = get_logger()
    logger.setLevel(logging.ERROR)
    while True:
        [numbers, boxes] = read_numbers(x, y)
        n = int(sqrt(len(numbers)+1))-1
        col_targets = numbers[:n]
        row_targets = []
        numbers = numbers[n:]
        grid = []
        for i in range(n):
            row_targets.append(numbers[i*(n+1)])
            grid.append(numbers[i*(n+1) + 1:i*(n+1) + n + 1])
        PrintGrid(grid)
        print(col_targets)
        print(row_targets)

        solution = Solve(grid, row_targets, col_targets)
        PrintGrid(solution)
        Play(solution, boxes, x, y)
        input()
