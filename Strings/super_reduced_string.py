#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Super Reduced String
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings / Stack
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):

    stack = []

    for char in s:

        # If top of stack matches current character
        if stack and stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    # Convert stack back to string
    reduced_string = ''.join(stack)

    # Return result
    return reduced_string if reduced_string else "Empty String"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()