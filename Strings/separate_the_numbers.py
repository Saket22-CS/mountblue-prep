#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Separate the Numbers
# Platform: HackerRank
# Difficulty: Medium
# Topic: Strings
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):

    n = len(s)

    # Single digit cannot form sequence
    if n == 1:
        print("NO")
        return

    # Try all possible first number lengths
    for length in range(1, n // 2 + 1):

        first = s[:length]

        # Leading zero not allowed
        if first[0] == '0':
            continue

        number = int(first)

        formed = first

        while len(formed) < n:
            number += 1
            formed += str(number)

        if formed == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):

        s = input()

        separateNumbers(s)