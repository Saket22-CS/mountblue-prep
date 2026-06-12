#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Largest Permutation
# Platform: HackerRank
# Difficulty: Medium
# Topic: Greedy, Hashing, Swapping
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):

    n = len(arr)

    # Store current position of every value
    pos = {value: idx for idx, value in enumerate(arr)}

    for i in range(n):

        if k == 0:
            break

        desired = n - i

        if arr[i] == desired:
            continue

        swap_idx = pos[desired]

        # Update positions
        pos[arr[i]] = swap_idx
        pos[desired] = i

        # Swap elements
        arr[i], arr[swap_idx] = arr[swap_idx], arr[i]

        k -= 1

    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()