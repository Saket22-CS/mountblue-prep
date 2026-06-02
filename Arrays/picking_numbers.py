#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Picking Numbers
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / Frequency Counting
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):

    frequency = [0] * 101

    for num in a:
        frequency[num] += 1

    maximum_length = 0

    for i in range(100):

        current_length = frequency[i] + frequency[i + 1]

        if current_length > maximum_length:
            maximum_length = current_length

    return maximum_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()