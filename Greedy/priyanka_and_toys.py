#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Priyanka and Toys
# Platform: HackerRank
# Difficulty: Easy
# Topic: Greedy, Sorting
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):

    w.sort()

    containers = 0
    i = 0
    n = len(w)

    while i < n:
        containers += 1

        limit = w[i] + 4

        while i < n and w[i] <= limit:
            i += 1

    return containers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()