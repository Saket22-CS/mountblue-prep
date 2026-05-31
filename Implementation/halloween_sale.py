#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Halloween Sale
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(number of games bought)
# Space Complexity: O(1)
#

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):

    games = 0
    current_price = p

    while s >= current_price:

        s -= current_price
        games += 1

        current_price = max(m, current_price - d)

    return games


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()