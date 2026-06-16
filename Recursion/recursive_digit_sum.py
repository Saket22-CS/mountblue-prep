#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Recursive Digit Sum
# Platform: HackerRank
# Difficulty: Medium
# Topic: Recursion, Mathematics, Digit Sum
#
# Time Complexity: O(len(n))
# Space Complexity: O(log N)
#

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):

    initial_sum = sum(int(digit) for digit in n) * k

    def find_super_digit(num):
        if num < 10:
            return num

        digit_sum = 0

        while num:
            digit_sum += num % 10
            num //= 10

        return find_super_digit(digit_sum)

    return find_super_digit(initial_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()