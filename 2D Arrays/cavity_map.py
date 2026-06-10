#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Cavity Map
# Platform: HackerRank
# Difficulty: Easy
# Topic: 2D Arrays, Simulation
#
# Time Complexity: O(n²)
# Space Complexity: O(n²)
#

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):

    n = len(grid)

    result = [list(row) for row in grid]

    for i in range(1, n - 1):
        for j in range(1, n - 1):

            current = grid[i][j]

            if (current > grid[i - 1][j] and
                current > grid[i + 1][j] and
                current > grid[i][j - 1] and
                current > grid[i][j + 1]):

                result[i][j] = 'X'

    return [''.join(row) for row in result]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()