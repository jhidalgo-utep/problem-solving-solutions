# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:40:19 2021

@author: joaqu
"""

# Q1: max product of 3 integers
# input: int array of numbers that are + and -
# output: return an int, being the largest product produced by 3 int's
def max_three_int(nums):
    max1 = max2 = max3 = 0
    min1 = min2 = 0
    
    for i in nums:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2:
            max3 = max2
            max2 = i
        elif i > max3:
            max3 = i
        
        if i < min1:
            min2 = min1 
            min1 = i
        elif i < min2:
            min2 = i
    
    return max(min1*min2*max1, max1*max2*max3)



# Q2: max sum of subarray
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_sum_subarray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
        
    return max(dp)


# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    