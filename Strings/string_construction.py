#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: String Construction
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings / Hashing
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):

    unique_characters = set(s)

    return len(unique_characters)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()