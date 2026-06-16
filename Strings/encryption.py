#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Encryption
# Platform: HackerRank
# Difficulty: Medium
# Topic: Strings, Implementation
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):

    s = s.replace(" ", "")
    L = len(s)

    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))

    if rows * cols < L:
        rows += 1

    result = []

    for col in range(cols):
        word = []

        for row in range(col, L, cols):
            word.append(s[row])

        result.append(''.join(word))

    return ' '.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()