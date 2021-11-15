# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:27:26 2021

@author: joaqu
"""

# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums 
def maximum_size_subarray_equals_k(nums, k):
    d= dict()
    prefix = 0
    longest = 0
    
    for i in range(len(nums) ):
        prefix += nums[i] 
        
        if prefix == k:
            longest = i+1
            
        if prefix - k in d:
            longest = max(longest, i - d[prefix-k])
        
        if prefix not in d:
            d[prefix] = i
            
    return longest


# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have at a time
# output: integer of the max length substring possible with k distict letters
def longest_k_distinct_substring(s, k):
    longest = 0
    left = 0
    d = dict()
    
    for right in range(len(s) ):
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
    
        longest = max(longest, right - left + 1)
    
    return longest



# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_sum_equals_k(nums, k):
    d = dict()
    d[0] = 1
    count = 0
    prefix = 0
    
    for i in nums:
        prefix += i
        
        if prefix - k in d:
            count += d[prefix-k]
        
        if prefix in d:
            d[prefix] += 1
        else:
            d[prefix] = 1
            
    return count


# Q5: Top K frequent words
# input: 1-D array of string words and integer k for the amount of top freq. words
# output: a list of the top 'k' frequent words
def top_freq_words(words, k):
    d = dict()
    
    for w in words:
        if w in d:
            d[w] -= 1
        else:
            d[w] = -1
        
    h = []
    
    for k in d.keys():
        heapq.heappush(h, (d[k], k) )
    
    res = []
    for i in range(k):
        freq, temp = heapq.heappop(h)
        res.append(temp)
    return res


# Q6: is palidrome (integer)
# input: integer above zero
# output: boolean determining if integer is palidrome or not
def is_palindrome(x):
    if x != 0 and x % 10 == 0:
        return False
    
    if x < 0:
        return False
        
    rev = 0
    while x > rev:
        rev = rev*10 + x%10
        x = x // 10
    
    if rev == x or rev // 10 == x:
        return True
    

####################################################################################
    
# Q2: max sum of subarray       #3 min
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_sum_subarray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums) ):
        dp[i] = max(dp[i-1] + nums[i], nums[i] )
    
    return max(dp)


# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    nums = nums.sort()
    res = []
    
    for i in range(len(nums) ):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                res.append( [nums[i] + nums[left] + nums[right] ] )
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
                
            else:
                right -= 1
                
    return res


# 1 Q21: word search
# input: 2-d array of char's called board and a string called 'word'
# output: return boolean if word was found in board moving up,down,left,right 
def word_search(board, word):
    path = []
    
    def dfs_board(i,j,pos):
        if i<0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in path or word[pos] != board[i][j]:
            return False
        if len(word) == pos:
            return True
        
        path.append( (i,j) )
        
        res = ( dfs_board(i-1,j,pos+1) or
               dfs_board(i+1,j,pos+1) or
               dfs_board(i,j-1,pos+1) or
               dfs_board(i,j+1,pos+1) )
        
        path.remove( (i,j) )
        return res
    
    
    for i in range(len(board) ):
        for j in range(len[board[0]] ):
            if dfs_board(i,j, 0):
                return True
    return False


# Q5: longest_substring_no_duplicates       #10min
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring_no_dup(s):
    longest = 0
    left = 0 
    letters = set()
    
    for right in range(len(s) ):
        while left < right and s[right] in letters:
            letters.remove(s[left] )
            left += 1
        letters.add(s[right])
        longest = max(longest, right-left+1)
        
    return longest
        
        
    
    
    
        
        
    
            
    




