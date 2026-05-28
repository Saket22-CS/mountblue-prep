#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Sequence Equation
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation / Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):

    # Store value -> position mapping
    position = {}

    for index, value in enumerate(p):
        position[value] = index + 1

    result = []

    # Find y such that p(p(y)) = x
    for x in range(1, len(p) + 1):

        first_position = position[x]

        y = position[first_position]

        result.append(y)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()