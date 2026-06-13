#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Closest Numbers
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Arrays
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):

    arr.sort()

    min_diff = float('inf')
    result = []

    for i in range(len(arr) - 1):

        diff = arr[i + 1] - arr[i]

        if diff < min_diff:
            min_diff = diff
            result = [arr[i], arr[i + 1]]

        elif diff == min_diff:
            result.extend([arr[i], arr[i + 1]])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()