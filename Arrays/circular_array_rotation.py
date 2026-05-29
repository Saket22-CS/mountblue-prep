#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Circular Array Rotation
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays
#
# Time Complexity: O(n + q)
# Space Complexity: O(n)
#

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):

    n = len(a)

    # Reduce unnecessary rotations
    k = k % n

    # Perform rotation
    rotated = a[-k:] + a[:-k]

    result = []

    for index in queries:
        result.append(rotated[index])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()