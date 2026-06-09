#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Counting Sort 1
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(100) ≈ O(1)
#

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):

    frequency = [0] * 100

    for num in arr:
        frequency[num] += 1

    return frequency


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()