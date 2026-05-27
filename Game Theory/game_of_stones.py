#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Game of Stones
# Platform: HackerRank
# Difficulty: Easy
# Topic: Game Theory
#
# Time Complexity: O(1)
# Space Complexity: O(1)
#

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n):

    # Losing positions occur when n % 7 is 0 or 1
    if n % 7 == 0 or n % 7 == 1:
        return "Second"

    return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()