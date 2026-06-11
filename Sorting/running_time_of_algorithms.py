#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Running Time of Algorithms
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Insertion Sort
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):

    shifts = 0

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1

        arr[j + 1] = key

    return shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()