#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Greedy Florist
# Platform: HackerRank
# Difficulty: Medium
# Topic: Greedy, Sorting
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#

#
# Complete the getMinimumCost function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY c
#

def getMinimumCost(k, c):

    c.sort(reverse=True)

    total_cost = 0

    for i in range(len(c)):
        total_cost += (i // k + 1) * c[i]

    return total_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()