#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Intro to Tutorial Challenges
# Platform: HackerRank
# Difficulty: Easy
# Topic: Searching, Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):

    for i in range(len(arr)):
        if arr[i] == V:
            return i

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()