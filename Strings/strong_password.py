#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Strong Password
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    missing_types = 0

    if not any(char in numbers for char in password):
        missing_types += 1

    if not any(char in lower_case for char in password):
        missing_types += 1

    if not any(char in upper_case for char in password):
        missing_types += 1

    if not any(char in special_characters for char in password):
        missing_types += 1

    return max(missing_types, 6 - n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()