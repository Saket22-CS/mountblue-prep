#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: A Very Big Sum
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):

    total = 0

    for num in ar:
        total += num

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()