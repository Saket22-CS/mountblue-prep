#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Sansa and XOR
# Platform: HackerRank
# Difficulty: Easy
# Topic: Bit Manipulation, XOR
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):

    n = len(arr)

    result = 0

    for i in range(n):
        occurrences = (i + 1) * (n - i)

        if occurrences % 2 == 1:
            result ^= arr[i]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()