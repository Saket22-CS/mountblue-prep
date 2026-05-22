#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Migratory Birds
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / HashMap
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):

    # Frequency count for bird types 1 to 5
    frequency = [0] * 6

    # Count occurrences
    for bird in arr:
        frequency[bird] += 1

    max_count = max(frequency)

    # Return smallest bird ID with maximum frequency
    for bird_type in range(1, 6):

        if frequency[bird_type] == max_count:
            return bird_type


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()