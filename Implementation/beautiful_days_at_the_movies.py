#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Beautiful Days at the Movies
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(n × d)
# Space Complexity: O(1)
#
# where:
# n = number of days
# d = number of digits in each number
#

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):

    beautiful_count = 0

    for day in range(i, j + 1):

        reversed_day = int(str(day)[::-1])

        difference = abs(day - reversed_day)

        if difference % k == 0:
            beautiful_count += 1

    return beautiful_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()