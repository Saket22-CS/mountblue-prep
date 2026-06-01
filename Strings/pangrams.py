#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Pangrams
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings / Sets
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):

    letters = set()

    for char in s.lower():

        if char.isalpha():
            letters.add(char)

    if len(letters) == 26:
        return "pangram"

    return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()