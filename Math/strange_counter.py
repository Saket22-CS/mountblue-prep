#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Strange Counter
# Platform: HackerRank
# Difficulty: Easy
# Topic: Math, Simulation
#
# Time Complexity: O(log t)
# Space Complexity: O(1)
#

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):

    cycle = 3

    while t > cycle:
        t -= cycle
        cycle *= 2

    return cycle - t + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()