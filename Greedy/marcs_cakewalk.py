#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Marc's Cakewalk
# Platform: HackerRank
# Difficulty: Easy
# Topic: Greedy
#
# Time Complexity: O(n log n)
# Space Complexity: O(1)
#

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):

    # Eat highest-calorie cupcakes first
    calorie.sort(reverse=True)

    miles = 0

    for i in range(len(calorie)):
        miles += (2 ** i) * calorie[i]

    return miles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()