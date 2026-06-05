#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Funny String
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):

    reverse_s = s[::-1]

    for i in range(len(s) - 1):

        original_diff = abs(ord(s[i]) - ord(s[i + 1]))
        reverse_diff = abs(ord(reverse_s[i]) - ord(reverse_s[i + 1]))

        if original_diff != reverse_diff:
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()