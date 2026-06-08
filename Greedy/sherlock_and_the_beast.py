#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Sherlock and The Beast
# Platform: HackerRank
# Difficulty: Easy
# Topic: Greedy
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):

    fives = n

    while fives >= 0:

        threes = n - fives

        if fives % 3 == 0 and threes % 5 == 0:
            print("5" * fives + "3" * threes)
            return

        fives -= 5

    print(-1)


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):

        n = int(input().strip())

        decentNumber(n)