
#!/bin/python3

import math
import os
import random
import re
import sys


# Given an array of integers, find the subset of *non-adjacent* elements with the maximum sum

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    # initialize dp array
    dp = [0] * len(arr)
    dp[0] = max(0, arr[0])
    dp[1] = max(dp[0], arr[1])

    for i in range(2, len(arr)):
        # the *non-adjacent* requirement means either we pick the current i and skip the previous sum 
        # or skip i and keep the previous sum
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])  
    
    return dp[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
