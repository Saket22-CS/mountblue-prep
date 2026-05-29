#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Grid Challenge
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings / Sorting
#
# Time Complexity: O(n² log n)
# Space Complexity: O(n²)
#

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):

    # Sort each row alphabetically
    sorted_grid = [''.join(sorted(row)) for row in grid]

    rows = len(sorted_grid)
    cols = len(sorted_grid[0])

    # Check column ordering
    for col in range(cols):
        for row in range(1, rows):

            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()