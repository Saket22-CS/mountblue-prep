#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Minimum Distances
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / Hashing
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):

    last_seen = {}

    minimum_distance = float('inf')

    for i in range(len(a)):

        if a[i] in last_seen:
            distance = i - last_seen[a[i]]
            minimum_distance = min(minimum_distance, distance)

        last_seen[a[i]] = i

    return minimum_distance if minimum_distance != float('inf') else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()