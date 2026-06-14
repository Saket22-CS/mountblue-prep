#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Jim and the Orders
# Platform: HackerRank
# Difficulty: Easy
# Topic: Sorting, Greedy
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)
#

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):

    delivery = []

    for i, (order, prep) in enumerate(orders, start=1):
        delivery.append((order + prep, i))

    delivery.sort()

    return [customer for _, customer in delivery]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()