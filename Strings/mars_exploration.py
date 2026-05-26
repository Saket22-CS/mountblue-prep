#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Mars Exploration
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):

    expected = "SOS"
    changed = 0

    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            changed += 1

    return changed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()