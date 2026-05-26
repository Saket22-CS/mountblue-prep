#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Minimum Absolute Difference in an Array
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):

    arr.sort()

    min_diff = float('inf')

    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - 1])

    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()