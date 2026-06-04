#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Misère Nim
# Platform: HackerRank
# Difficulty: Easy
# Topic: Game Theory
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s):

    xor_sum = 0

    for pile in s:
        xor_sum ^= pile

    # Special case:
    # If all piles contain exactly 1 stone
    if all(pile == 1 for pile in s):

        if len(s) % 2 == 0:
            return "First"
        else:
            return "Second"

    # Normal Nim logic otherwise
    if xor_sum == 0:
        return "Second"

    return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()