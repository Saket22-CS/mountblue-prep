#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Problem: Missing Numbers
# Platform: HackerRank
# Difficulty: Easy
# Topic: Hash Map, Frequency Counting
#
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
#

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):

    freq_arr = Counter(arr)
    freq_brr = Counter(brr)

    result = []

    for num in sorted(freq_brr):
        if freq_brr[num] > freq_arr.get(num, 0):
            result.append(num)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()