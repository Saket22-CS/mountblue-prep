#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Cats and a Mouse
# Platform: HackerRank
# Difficulty: Easy
# Topic: Implementation
#
# Time Complexity: O(1)
# Space Complexity: O(1)
#

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):

    # Distance of Cat A from Mouse
    distA = abs(x - z)

    # Distance of Cat B from Mouse
    distB = abs(y - z)

    if distA < distB:
        return "Cat A"

    elif distB < distA:
        return "Cat B"

    else:
        return "Mouse C"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()