#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Flipping Bits
# Platform: HackerRank
# Difficulty: Easy
# Topic: Bit Manipulation
#
# Time Complexity: O(1)
# Space Complexity: O(1)
#

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):

    # 32-bit unsigned integer maximum value
    return 2**32 - 1 - n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()