#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Insertion Sort - Part 1
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Insertion Sort
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):

    value = arr[-1]

    i = n - 2

    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = value
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)