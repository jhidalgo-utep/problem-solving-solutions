import heapq
import numpy as np


# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_sum_equals_k(nums, k):
    prefix = 0
    counter = 0
    d = dict()
    d[0] = 1
    
    for i in nums:
        prefix += i
        
        diff = prefix - k
        if diff in d:
            counter += d[diff]
        
        if prefix in d:
            d[prefix] += 1
        else:
            d[prefix] = 1
    
    return counter


# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have at a time
# output: integer of the max length substring possible with k distict letters
def longest_substring_k_distinct_char(s, k):
    longest = 0
    left = 0
    d = dict()
    
    for right in range(len(s)):
        if s[right] in d:
            d[s[right]] += 1
        else:
            d[s[right]] = 1
        
        while left < right and len(d) > k:
            if d[s[left]] == 1:
                del d[s[left]]
            else:
                d[s[left]] -= 1
            left += 1
        
        longest = max(longest < right - left + 1)
        
    return longest




# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums 
def maximum_size_subarray_equals_k(nums, k):
    longest = 0
    prefix = 0
    d = dict()
    
    for i in range(len(nums)):
        prefix += nums[i]
        
        if prefix == k:
            longest = i + 1
        
        if prefix - k in d:
            longest = max(longest, i - d[prefix-k])
        
        if not prefix in d:
            d[prefix] = i
            
    return longest


# Q5: Top K frequent words
# input: 1-D array of string words and integer k for the amount of top freq. words
# output: a list of the top 'k' frequent words
def top_k_freq_words(words, k):
    h1 = []
    d = dict()
    res = []
    
    for word in words:
        if word in d:
            d[word] -= 1
        else:
            d[word] = -1
    
    for k,v in d.items():
        heapq.heappush(h1, (v,k))
    
    for i in range(k):
        freq, item = heapq.heappop(h1)
        res.append(item)
        
    return res
        

# Q6: is palidrome (integer)
# input: integer above zero
# output: boolean determining if integer is palidrome or not
def is_palindrome_int(x):
    if x < 0:
        return False
    
    if x != 0 and x%10 == 0:
        return False
    
    rev=0
    while x > rev:
        rev = (rev*10) + (x%10)
        x = x // 10
    
    return x == rev or rev // 10 == x



# Q1: max product of 3 integers
# input: int array of numbers that are + and -
# output: return an int, being the largest product produced by 3 int's
def max_product_of_3(nums):
    min1 = min2 = math.inf
    max1 = max2 = max3 = -math.inf
    
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
    for i in range(1, len(nums) ):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    return max(dp)


# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums)



    

if __name__ == "__main__":
    print('start')
    
    q3 = [1, 5, 2, 1, 8]
    target3 = 8
    
    print( subarray_sum_equals_k(q3, target3) )
        
    
    
    

