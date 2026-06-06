#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Find Digits
# Platform: HackerRank
# Difficulty: Easy
# Topic: Mathematics
#
# Time Complexity: O(d)
# Space Complexity: O(1)
# where d = number of digits in n
#

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):

    count = 0
    temp = n

    while temp > 0:

        digit = temp % 10

        if digit != 0 and n % digit == 0:
            count += 1

        temp //= 10

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()