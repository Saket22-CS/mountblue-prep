#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Anagram
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings / Hashing
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):

    n = len(s)

    # Odd length strings cannot be split equally
    if n % 2 != 0:
        return -1

    first = s[:n // 2]
    second = s[n // 2:]

    frequency = {}

    # Count characters in first half
    for ch in first:
        frequency[ch] = frequency.get(ch, 0) + 1

    changes = 0

    # Match characters from second half
    for ch in second:
        if frequency.get(ch, 0) > 0:
            frequency[ch] -= 1
        else:
            changes += 1

    return changes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()