#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Problem: Happy Ladybugs
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings, Greedy
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):

    counts = Counter(b)

    # Any color appearing only once can never be made happy
    for color, freq in counts.items():
        if color != '_' and freq == 1:
            return "NO"

    # If there is an empty cell, rearrangement is possible
    if '_' in b:
        return "YES"

    # No empty cells: check if every ladybug is already happy
    n = len(b)

    for i in range(n):
        left_same = (i > 0 and b[i] == b[i - 1])
        right_same = (i < n - 1 and b[i] == b[i + 1])

        if not (left_same or right_same):
            return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()