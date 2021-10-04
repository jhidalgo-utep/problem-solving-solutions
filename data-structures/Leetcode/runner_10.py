# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:38:44 2021

@author: joaqu
"""
import heapq
import numpy as np

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
    for i in range(1, len(nums)):
        dp[i] = max(nums[i] + dp[i-1], nums[i])
    return max(dp)


# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i+1
        right = len(nums)-1
        
        while left < right:
            
            tsum = nums[i] + nums[left] + nums[right]
            
            if tsum == 0:
                result.append( [nums[mid] + nums[left] + nums[right]] )
                left +=1 
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif tsum < 0:
                left += 1
            else:
                right -= 1
    return result
            

# Q4: best time to sell stock 1
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in 1 transaction
def best_time_to_sell_stock_1(nums):
    min1 = math.inf
    res = 0
    for i in nums:
        min1 = min(min1, i)
        profit = i - min1
        res = max(res, profit)
    return res


# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_sell_stock_2(nums):
    profit = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            profit += nums[i] - nums[i-1]
    return profit


# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
def reverse_integer(x):
    if x < 0:
        symbol = -1
        x = x*-1
    else:
        symbol = 1
    
    
    result = 0
    
    while x:
        result = result*10 + x%10
        x = x//10
    
    if result > math.pow(2,31):
        return 0
    return result * symbol


# Q7: is anagram
# input: 2 strings that represent words
# output: boolean checking if word 's' is anagram of word 't'
def anagram(s, t):
    if len(s) != len(t):
        return False
    
    d = dict()
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    
    for c in t:
        if c in d:
            d[c] -= 1
        else:
            return False
        
    for k,v in d.items():
        if v != 0:
            return False
    return True


  
# Q8: is palindrome
# input: string called 's' with spaces, nums, special chars
# output: return boolean if string is palindrome
def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
            
        while not s[right].isalnum() and left < right:
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


# Q9: climbing stairs
# input: integer of how many stairs there are
# output: integer of how many ways to reach the top by either taking 1 or 2 steps at a time
def climbing_stairs(n):
    # dp = [1] * n
    # dp[1] = 2
    # for i in range(2, n):
    #     dp[i] = dp[i-1] + dp[i-2]
    # return dp[n-1]
    forward = 1
    backward = 1
    for i in range(n-1):
        temp = forward
        forward = forward + backward
        backward = temp
    return forward


# Q10: fibonacci sequence (dp)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo(n):
    dp = [0] * (n+1)
    d[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# Q11: fibonacci sequence (o1 space)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo2(n):
    forward = 1
    backward = 0
    for i in range(n-1):
        temp = forward
        forward = forward + backward
        backward = temp
    return forward


# Q12: house robber
# input: 1-d array of integers that represent how much money each house has acording to its position
# output: integer, the maximum money that can be stolen not robing house directly next to each other
def house_robber(nums):
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    d[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
    return max(dp)


# Q13: roman string to integer
# input: string that is written in roman
# output: integer of the roman string in numbers
def roman_to_int(s):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    if len(s) == 1:
        return roman[s[0]]
    
    res = 0
    for i in range(len(s) ):
        if i+1 < len(s) and s[i] < s[i+1]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res


# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def int_to_roman(num):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numeral = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
 
    res = ''
    for i in range(len(int_val) ):
        result = (num//int_val[i]) * numeral[i]
        num = num%int_val[i]
        
    return res
        
        
# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triangle(rows):
    result = [ [1] ]
    queue = []
    
    i = 1
    while i < rows:
        temp = []
        prev = [0] + result[-1]  [0]
        for j in range(len(result[-1])+1 ):
            temp.append(prev[j] + prev[j+1])
        result.append(temp)
        
        i += 1
    return result


# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def find_missing_number(nums):
    n = len(nums)
    tsum = sum(nums)
    
    return ((n*(n+1)) // 2) - tsum


# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def contain_most_water(nums):
    left = 0
    right = len(nums) - 1
    max_w = -math.inf
    
    while left < right:
        if nums[left] < nums[right]:
            max_w = max(max_w, nums[left]*(right-left) )
            left += 1
        else:
            max_w = max(max_w, nums[right]*(right-left) )
            right -= 1
            
    return max_w
        

        
# Q18: set matrix zeros across col's and row's
# input: 2-d 'matrix' array of 1's and 0's
# output: None, edit 'matrix' in-place replacing the whole row and col where '0' are found
def set_zeros_matrix(matrix):
    rowz = [0] * len(matrix)
    colz = [0] * len(matrix[0] )
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rowz[i] = 1
                colz[i] = 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rowz[i] == 1 or colz[j] == 1:
                matrix[i][j] = 0


# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
def longest_palindrome(s):
    res = ''
    longest = 0
    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > longest:
                longest = r-l+1
                res = = s[l:r+1]
            l -= 1
            r += 1
            
        
        l = i
        r = i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > longest:
                res = s[l:r+1]
                longest = r-l+1
            l -= 1
            r += 1
            
    return result
        


# Q20: median integer of data stream
# input: 1-D array of integers called 'nums'
# output: return the median integer of the data stream
# MAX heap     -       MIN Heap
#9, 8, 4, 2    -     10, 14, 15, 17



# 15, 3        -   22
def median_data_stream(nums):
    hmin = hmax = []
    
    for i in nums:
        heapq.heappush(hmax, -1*i)
        
        if len(hmax) > 0 and len(hmin) > 0 and -1*hmax[0] > hmin[0]:
            val = -1*heapq.heappop(hmax)
            heapq.heappush(hmin, val)
        
        if len(hmax) > len(hmin) + 1:
            val = -1*heapq.heappop(hmax)
            heapq.heappush(hmin, val)
        
        if len(hmax) + 1 < len(hmin):
            val = heapq.heappop(hmin)
            heapq.heappush(hmax, -1*val)
            


# Q21: word search
# input: 2-d array of char's called board and a string called 'word'
# output: return boolean if word was found in board moving up,down,left,right 
def word_search(board, word):
    stack = []
    path = set()
    def dfs_board(i,j, cur_len):
        if i < 0 or i >= len(board) or j < 0 or j>= len(board[0]) or board[i][j] != word[cur_len] or (i,j) in path:
            return False
        
        if cur_len == len(word):
            return True
        
        path.add( (i,j))
        res = ( dps_board(i-1, j, cur_len +1) or
            dps_board(i+1, j, cur_len +1) or
            dps_board(i, j-1, cur_len +1) or
            dps_board(i, j+1, cur_len +1) )
        path.remove( (i,j))
        return res
        
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs_board(i,j, 0):
                return True
    return False
        


# Q22: count words with 1 iterator
# input: string of char's and space's
# output: return integer of how many words found in string1
def count_words(string1):
    res = 0
    in_word = False
    
    for c in string1:
        if c != ' ' and in_word == False:
            res += 1
            in_word = True
        elif c == ' ' and in_word == True:
            in_word = False
            
    return res
    

# Q23: t9 text letter possibility combinations
# input: a string representing a number
# output: a list of string combinations made from the input representing a number
def t9_combo(string1):
    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    stack = []
    stack.append((0,"") )
    result = []
    
    while stack:
        cur_len, combo = stack.pop()
        
        if len(string1) == cur_len:
            result.append(combo)
        else:
            next_digit = string1[cur_len]
            children = d[next_digit]
            for child in children:
                stack.append( (cur_len+1, combo+child) )
                
    return result


# Q24: find kth largest element
# input: 1-d array of integers called nums and integer k, representing the kth largest item
# output: integer from nums array that is the kth largest item in nums
def find_kth_largest(nums, k):
    h1 = []
    
    for i in nums:
        heapq.heappush(h1, i)
    
    res = heapq.nlargest(k, h1)
    return res[-1]
    


# Q25: top k frequent items
# input: 1-d array 'nums' of integers that may contain duplicates and integer k 
# output: return a list of integers of len k, that apear the most frequent in 'nums'
def top_k_freq_items(nums, k):
    d= dict()
    h1 = []
    
    for i in nums:
        if i in d:
            d[i] -= 1
        else:
            d[i] = -1
            
    for k,v in d.items():
        heapq.heappush(h1, (v,k))
    
    count = 0
    res = []
    while count < k:
        res.append(heapq.heappop(h1) )
        count += 1
    return res


# Q26: find peak of mountain
# input: 1-d int array called nums of heights of mounain that go in a straight line
# output: integer index of the peak of the mountain found in nums array
def find_peak(nums):
    left = nums
    right = len(nums) - 1
    
    while left < right:
        mid = (right + left) // 2
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left


# Q27: unique num of path
# input: integer represent rows 'm', and integer representing num of columns 'n'
# output: integer of the possible ways to reach the bottom right of game board (m x n) only moving 1 right or down
def unique_paths(m,n):
    temp = np.zeros( (m,n), dtype = int)+1
    
    for i in range(1, m):
        for j in range(1, n):
            temp[i][j] = temp[i-1][j] + temp[i][j-1]
            
    return temp[m-1][n-1]
    
            
        
# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increase_subseq(nums):
    
    longest = 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j])
    return max(dp)


# Q30: rotate array
# input: 1-d int array of numbers and k the amount to be rotated
# output: nothing, edit in-place array rotating to the right by 'k' times
def rotate_array(nums, k):
    #nums.sort()
    reverse(nums, 0, len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums, k, len(nums)-1)
    
def reverse(nums, l, r):
    
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l+=1
        r -= 1
        

# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def right_side_BST(root):
    queue = []
    queue.append(root)
    result = []
    
    while queue:
        cur_len = len(queue)
        right_side = None
        
        for i in range(cur_len):
            curr = queue.pop(0)
            if curr:
                right_side = curr
                queue.append(curr.left)
                queue.append(curr.right)
        
        if right_side:
            result.append(right_side.val)
    return result
        
        


        