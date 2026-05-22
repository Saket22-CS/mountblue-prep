#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Subarray Division
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / Sliding Window
#
# Time Complexity: O(n * m)
# Space Complexity: O(1)
#

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):

    count = 0

    # Traverse all possible subarrays of length m
    for i in range(len(s) - m + 1):

        segment = s[i:i + m]

        # Check if segment sum equals d
        if sum(segment) == d:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()