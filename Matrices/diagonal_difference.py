#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Diagonal Difference
# Platform: HackerRank
# Difficulty: Easy
# Topic: 2D Arrays / Matrices
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    primary_diagonal = 0
    secondary_diagonal = 0

    n = len(arr)

    for i in range(n):

        # Left-to-right diagonal
        primary_diagonal += arr[i][i]

        # Right-to-left diagonal
        secondary_diagonal += arr[i][n - 1 - i]

    # Return absolute difference
    return abs(primary_diagonal - secondary_diagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()