#!/bin/python3

import math
import os
import random
import re
import sys

#
# Problem: Designer PDF Viewer
# Platform: HackerRank
# Difficulty: Easy
# Topic: Strings / Arrays
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):

    max_height = 0

    for char in word:
        index = ord(char) - ord('a')
        max_height = max(max_height, h[index])

    area = max_height * len(word)

    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()