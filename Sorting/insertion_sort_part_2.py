#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Insertion Sort - Part 2
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Insertion Sort
#
# Time Complexity: O(n²)
# Space Complexity: O(1)
#

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):

    for i in range(1, n):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)