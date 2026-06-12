#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Counting Sort 2
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Counting Sort
#
# Time Complexity: O(n + k)
# Space Complexity: O(k)
# where k = 100 (fixed range of values)
#

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):

    freq = [0] * 100

    for num in arr:
        freq[num] += 1

    result = []

    for value in range(100):
        result.extend([value] * freq[value])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()