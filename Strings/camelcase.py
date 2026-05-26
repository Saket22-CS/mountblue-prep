#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: CamelCase
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):

    # First word always exists
    word_count = 1

    for char in s:
        if char.isupper():
            word_count += 1

    return word_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()