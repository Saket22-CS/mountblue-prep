#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Maximizing XOR
# Platform: HackerRank
# Difficulty: Easy
# Topic: Bit Manipulation
#
# Time Complexity: O(log(r))
# Space Complexity: O(1)
#

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):

    xor = l ^ r
    max_xor = 1

    while xor:
        max_xor <<= 1
        xor >>= 1

    return max_xor - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()