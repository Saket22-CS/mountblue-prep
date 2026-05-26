#!/bin/python3

import os
import sys

#
# Problem: Electronics Shop
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(n × m)
# Space Complexity: O(1)
#

#
# Complete the getMoneySpent function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY keyboards
#  2. INTEGER_ARRAY drives
#  3. INTEGER b
#

def getMoneySpent(keyboards, drives, b):

    max_cost = -1

    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive

            if total <= b:
                max_cost = max(max_cost, total)

    return max_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()