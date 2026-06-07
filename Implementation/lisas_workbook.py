#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Lisa's Workbook
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(total problems)
# Space Complexity: O(1)
#

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):

    special = 0
    page = 1

    for problems in arr:

        problem_num = 1

        while problem_num <= problems:

            start = problem_num
            end = min(problem_num + k - 1, problems)

            if start <= page <= end:
                special += 1

            problem_num += k
            page += 1

    return special


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()