#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Drawing Book
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(1)
# Space Complexity: O(1)
#

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):

    # Pages turned from the front
    front_turns = p // 2

    # Pages turned from the back
    back_turns = (n // 2) - (p // 2)

    return min(front_turns, back_turns)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()