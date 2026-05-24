#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Library Fine
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(1)
# Space Complexity: O(1)
#

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):

    # Returned in a later year
    if y1 > y2:
        return 10000

    # Returned in the same year but later month
    if y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)

    # Returned in the same month and year but later day
    if y1 == y2 and m1 == m2 and d1 > d2:
        return 15 * (d1 - d2)

    # Returned on time or early
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()