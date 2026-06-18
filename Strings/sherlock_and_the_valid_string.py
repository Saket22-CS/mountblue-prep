#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Problem: Sherlock and the Valid String
# Platform: HackerRank
# Difficulty: Medium
# Topic: Hashing, Frequency Counting
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):

    char_freq = Counter(s)
    freq_count = Counter(char_freq.values())

    # All characters already have the same frequency
    if len(freq_count) == 1:
        return "YES"

    # More than two different frequencies cannot be fixed by one deletion
    if len(freq_count) > 2:
        return "NO"

    (f1, c1), (f2, c2) = sorted(freq_count.items())

    # Case 1:
    # One character occurs once and can be removed entirely
    if f1 == 1 and c1 == 1:
        return "YES"

    # Case 2:
    # One character has frequency exactly one more than others
    if f2 == f1 + 1 and c2 == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()