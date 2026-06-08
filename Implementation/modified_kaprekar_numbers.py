#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Modified Kaprekar Numbers
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(q - p)
# Space Complexity: O(k)
#

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):

    result = []

    for num in range(p, q + 1):

        square = str(num * num)

        digits = len(str(num))

        left = square[:-digits]
        right = square[-digits:]

        left_num = int(left) if left else 0
        right_num = int(right) if right else 0

        if left_num + right_num == num:
            result.append(str(num))

    if result:
        print(" ".join(result))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':

    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)