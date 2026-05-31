#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Maximum Perimeter Triangle
# Platform: HackerRank
# Difficulty: Easy
# Topic: Greedy
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):

    # Sort sticks in ascending order
    sticks.sort()

    # Check triplets from largest values
    for i in range(len(sticks) - 1, 1, -1):

        a = sticks[i - 2]
        b = sticks[i - 1]
        c = sticks[i]

        # Triangle condition
        if a + b > c:
            return [a, b, c]

    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()