#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Gemstones
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sets / Strings
#
# Time Complexity: O(n × m)
# Space Complexity: O(26)
#

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):

    # Convert first rock into set
    common_minerals = set(arr[0])

    # Find common minerals across all rocks
    for rock in arr[1:]:
        common_minerals &= set(rock)

    return len(common_minerals)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()