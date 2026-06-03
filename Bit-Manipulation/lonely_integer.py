#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Lonely Integer
# Platform: HackerRank
# Difficulty: Easy
# Topic: Bit Manipulation
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):

    unique = 0

    for num in a:
        unique ^= num

    return unique


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()