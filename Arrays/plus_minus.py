#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Plus Minus
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    positive_count = 0
    negative_count = 0
    zero_count = 0

    total = len(arr)

    # Count positive, negative, and zero elements
    for num in arr:

        if num > 0:
            positive_count += 1

        elif num < 0:
            negative_count += 1

        else:
            zero_count += 1

    # Calculate ratios
    positive_ratio = positive_count / total
    negative_ratio = negative_count / total
    zero_ratio = zero_count / total

    # Print with 6 decimal places
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)