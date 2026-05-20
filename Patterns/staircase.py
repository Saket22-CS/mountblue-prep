#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Staircase
# Platform: HackerRank
# Difficulty: Easy
# Topic: Loops / Patterns
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):

    for i in range(1, n + 1):

        # Print spaces + hashes
        spaces = " " * (n - i)
        hashes = "#" * i

        print(spaces + hashes)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)