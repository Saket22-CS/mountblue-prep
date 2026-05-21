#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Bill Division
# Platform: HackerRank
# Difficulty: Easy
# Topic: Arrays / Math
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):

    # Remove the item Anna didn't eat
    total_bill = sum(bill) - bill[k]

    # Anna's actual share
    anna_share = total_bill // 2

    # Check if Brian charged correctly
    if b == anna_share:
        print("Bon Appetit")
    else:
        refund = b - anna_share
        print(refund)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)