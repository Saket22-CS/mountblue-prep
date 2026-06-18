#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Gaming Array
# Platform: HackerRank
# Difficulty: Medium
# Topic: Game Theory, Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):

    moves = 0
    current_max = 0

    for num in arr:
        if num > current_max:
            current_max = num
            moves += 1

    return "BOB" if moves % 2 == 1 else "ANDY"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()