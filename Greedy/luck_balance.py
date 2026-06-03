#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Luck Balance
# Platform: HackerRank
# Difficulty: Easy
# Topic: Greedy
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):

    total_luck = 0
    important = []

    for luck, importance in contests:

        if importance == 0:
            total_luck += luck

        else:
            important.append(luck)

    important.sort(reverse=True)

    # Lose top k important contests
    total_luck += sum(important[:k])

    # Win remaining important contests
    total_luck -= sum(important[k:])

    return total_luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()