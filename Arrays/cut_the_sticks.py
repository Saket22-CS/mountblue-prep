#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Cut the Sticks
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / Simulation
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):

    arr.sort()

    result = []
    n = len(arr)

    result.append(n)

    for i in range(1, n):

        # New stick length encountered
        if arr[i] != arr[i - 1]:
            result.append(n - i)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()