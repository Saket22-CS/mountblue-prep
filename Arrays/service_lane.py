#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Service Lane
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays
#
# Time Complexity: O(t × segment_length)
# Space Complexity: O(t)
#

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n, cases):

    result = []

    for start, end in cases:
        minimum_width = min(width[start:end + 1])
        result.append(minimum_width)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()