#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Caesar Cipher
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):

    k %= 26
    encrypted = []

    for char in s:

        if char.islower():
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            encrypted.append(new_char)

        elif char.isupper():
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            encrypted.append(new_char)

        else:
            encrypted.append(char)

    return ''.join(encrypted)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()