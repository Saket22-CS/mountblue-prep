#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Append and Delete
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings
#
# Time Complexity: O(min(len(s), len(t)))
# Space Complexity: O(1)
#

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):

    common_length = 0

    # Find longest common prefix
    while (common_length < len(s) and
           common_length < len(t) and
           s[common_length] == t[common_length]):
        common_length += 1

    # Minimum operations required
    operations_needed = (
        (len(s) - common_length) +
        (len(t) - common_length)
    )

    # If we can delete entire string and rebuild
    if k >= len(s) + len(t):
        return "Yes"

    # Exact operations or extra operations usable in pairs
    if k >= operations_needed and (k - operations_needed) % 2 == 0:
        return "Yes"

    return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t)

    fptr.write(result + '\n')

    fptr.close()