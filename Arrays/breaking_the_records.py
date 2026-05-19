#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Breaking the Records
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):

    highest_score = scores[0]
    lowest_score = scores[0]

    max_record_breaks = 0
    min_record_breaks = 0

    for score in scores[1:]:

        # Check for highest score record
        if score > highest_score:
            highest_score = score
            max_record_breaks += 1

        # Check for lowest score record
        elif score < lowest_score:
            lowest_score = score
            min_record_breaks += 1

    return [max_record_breaks, min_record_breaks]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()