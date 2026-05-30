#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Big Sorting
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):

    # Sort by:
    # 1. Length of number
    # 2. Lexicographical order if lengths equal

    unsorted.sort(key=lambda x: (len(x), x))

    return unsorted


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()