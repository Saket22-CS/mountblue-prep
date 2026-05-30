#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Equalize the Array
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / Frequency Counting
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    max_frequency = max(frequency.values())

    return len(arr) - max_frequency


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()