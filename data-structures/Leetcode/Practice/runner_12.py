# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:19:08 2021

@author: joaqu
"""

# Q2: max sum of subarray
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_sub_subarray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], dp[i-1])
    return max(dp)


# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    nums.sort()
    res= []
    
    for i in range(len(nums) ):
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        
        left = i+1
        right = len(nums) - 1
        
        while left<right:
            
            if nums[i] + nums[left] + nums[right]:
                res.append( nums[i] + nums[left] + nums[right])
                left += 1
                while nums[left] == nums[left-1]:
                    left += 1
            
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
                
            elif nums[i] + nums[left] + nums[right] > 0:
                right -=1
    return res
                
                
# Q4: best time to sell stock 1
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in 1 transaction
def best_time_to_sell_stock_1(nums):
    min1 = math.inf
    max_p = 0
    
    for i in nums:
        min1 = min(min1, i)
        profit = i - min1
        max_p = max(max_p, profit)
        
    return max_p


# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_to_sell_stock_2(nums):
    profit = 0
    
    for i in range(1,len(nums) ):
        if nums[i] > nums[i-1]:
            profit += nums[i] - nums[i-1]
    return profit


# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
def reverse_int(x):
    if x < 0:
        symbol = -1
        x = x*-1
    else:
        symbol = 1
    
    res = 0
    while x:
        res = res*10 + x%10
        x = x//10
        
    if res > math.pow(2,31):
        return 0
    return res * symbols
        
    
# Q7: is anagram
# input: 2 strings that represent words
# output: boolean checking if word 's' is anagram of word 't'
def anagram(s,t):
    if len(s) != len(t):
        return False
    
    d= dict()
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
    left = 0 
    right = len(s) - 1
    
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        
        while not s[right].isalnum() and left < right:
            right -= 1
        
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True
        

# Q9: climbing stairs
# input: integer of how many stairs there are
# output: integer of how many ways to reach the top by either taking 1 or 2 steps at a time
def climbing_stairs(n):    
    if n == 0:
        return 0
    
    dp = [1] * n
    dp[1] = 2
    
    if n == 1:
        return dp[0]
    elif n == 2:
        return dp[1]
    
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n-1]

    # forward = backward = 1
    # for i in range(n-1):
    #     temp = forward
    #     forward = forward + backward
    #     backward = temp
    # return forwward
    
    
# Q10: fibonacci sequence (dp)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo(n):
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# Q11: fibonacci sequence (O(1) space)
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
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1] )
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums))
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
    return max(dp)
                    


# Q13: roman string to integer
# input: string that is written in roman
# output: integer of the roman string in numbers
def roman_to_int(string1):
    d = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    res = 0
    
    for i in range(len(string1)):
        if i + 1 < len(string1) and d[string1[i]] < d[string1[i+1]]:
            res -= d[ string1[i] ]
        else:
            res += d[ string1[i] ]
    return res
    
    
# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def integer_to_roman(x):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    res = ''
    i = 0
    while x:
        res += (x//int_val[i]) * roman[i]
        x = x % int_val[i]
        i+=1
    return res
            

# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triangle(rows):
    res = [ [1] ]
    for i in range(len(rows)-1 ):
        row = []
        cur_len = len(res[-1])
        temp = [0] + res[-1] + [0]
        
        for j in range(cur_len + 1):
            row.append(temp[j] + temp[j+1])
            
        res.append(row)
        
    return res

# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def missing_number(nums):
    n = len(nums)
    t_sum = sum(nums)
    return ((n*(n+1))//2) - t_sum



# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def container_with_most_water(nums):
    left = 0
    right = len(nums) - 1
    water = 0
    
    while left<right:
        if nums[left] < nums[right]:
            water = max(water, nums[left]*(right-left) )
            left += 1
        else:
            water = max(water, nums[right]*(right-left) )
            right -= 1
            
    return water


# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
def longest_palinfrome(s):
    # ODD
    res =''
    longest = 0
    
    for i in range(len(s) ):
        left = right = i
        
        while left > 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > longest:
                longest = right - left + 1
                res = s[left:right+1]
            left -= 1
            right +=1
                
        
        # EVEN
        left = i
        right = left + 1
        
        while left > 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > longest:
                    longest = right - left + 1
                    res = s[left:right+1]
            left -= 1
            right += 1
    return res


# Q20: median integer of data stream
# input: 1-D array of integers called 'nums'
# output: return the median integer of the data stream
#    hmax    :    hmin 
def median_data_stream(nums):
    hmax = hmin = []
    
    for i in nums:
        heapq.heappush(hmax, i)
        
        if len(hmax) > 0 and len(hmin) > 0 and -1*hmax[0] > hmin[0]:
            val = -1*heaq.heappop(hmax)
            heapq.heappush(hmin, val)
        
        if len(hmax) + 1 < len(hmin):
            val = heapq.heappop(hmin)
            heapq.heappush(hmax, -1*val)
        
        if  len(hmax) > len(hmin) + 1:
            val = -1 * heapq.heappop(hmax)
            heapq.heappush(hmin, val)
            
    if len(hmin) == len(hmax):
        v1 = heapq.heappop(hmin)
        v2 = -1*heapq.heappop(hmax)
        return (v1 + v2) // 2
    else:
        if len(hmin) > len(hmax):
            return heapq.heappop(hmin)
        else:
            return -1*heapq.heappop(hmax)
        
# Q21: word search
# input: 2-d array of char's called board and a string called 'word'
# output: return boolean if word was found in board moving up,down,left,right 
def word_search(board, word):
    path = set()
    
    def dfs_board(i,j, cur_len):
        if cur_len == len(word):
            return True
        
        if i <0 or i >= len(board) or j < 0 or j < len(board[0] ) or word[cur_len] != board[i][j] or (i,j) in path:
            return False
        
        path.add( (i,j))
        res = ( dfs_board(i-1,j,cur_len + 1) or
               dfs_board(i+1,j,cur_len + 1) or
               dfs_board(i,j-1,cur_len + 1) or
               dfs_board(i,j+1,cur_len + 1) )
        path.remove( (i,j))
        return res
        
        
        
    for i in range(len(board) ):
        for j in range(len(board[0]) ):
            if dfs_board(i,j, 0):
                return True
    return False


# Q22: count words with 1 iterator
# input: string of char's and space's
# output: return integer of how many words found in string1
def count_words(string1):
    count = 0
    in_word = False
    
    for c in string1:
        if c != " " and in_word == False:
            count += 1
            in_word = True
        elif c == ' ' and in_word == True:
            in_word = False
    return count



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
    res = []
    
    while stack:
        cur_len, combo = stack.pop()
        
        if cur_len == len(string1):
            res.append(combo)
        else:
            next_digit = string1[cur_len]
            children = d[next_digit]
            for child in children:
                stack.append(cur_len+1, combo+child)
                
    return res
    
    
# Q24: find kth largest element
# input: 1-d array of integers called nums and integer k, representing the kth largest item
# output: integer from nums array that is the kth largest item in nums
def find_kth_largest(nums, k):
    h1 = []
    
    for i in nums:
        heapq.heappush(h1, -1*i)
    
    val = 0
    for i in range(k):
        val = heapq.heappop(h1)
    return val*-1


# Q25: top k frequent items
# input: 1-d array 'nums' of integers that may contain duplicates and integer k 
# output: return a list of integers of len k, that apear the most frequent in 'nums'
def top_k_items(nums, k):
    res = []
    d = dict()
    h1 = []
    
    for i in nums:
        if i in d:
            d[i] -= 1
        else:
            d[i] = -1
    
    for k,v in d.items():
        heapq.heappush(h1, (v,k) )
    
    for i in range(k):
        freq, word = heapq.heappop(h1) 
        res.append(word)
        
    return res


# Q26: find peak of mountain
# input: 1-d int array called nums of heights of mounain that go in a straight line
# output: integer index of the peak of the mountain found in nums array
def find_peak(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (right+left) // 2
        
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid + 1
    return left


# Q27: unique num of path
# input: integer represent rows 'm', and integer representing num of columns 'n'
# output: integer of the possible ways to reach the bottom right of game board (m x n) only moving 1 right or down
def unique_path(m, n):
    dp = np.zeros( (m,n), dtype = int)+1
    
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[m-1][n-1]



# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increasing_subsequence(nums):
    longest = 0
    dp = [0] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
            
    
# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def right_side(root):
    queue = []
    queue.append(root)
    res = []
    
    while queue:
        right_side = None
        node_len = len(queue)
        
        for i in range(node_len):
            curr = queue.pop(0)
            if curr:
                right_side = curr
                queue.append(curr.left)
                queue.append(curr.right)
                
        if right_side:
            res.append(right_side)
    return res


# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_equals_k(nums, k):
    d = dict()
    d[0] = 1
    
    count = 0
    prefix = 0
    for i in nums:
        prefix += i
        
        diff = prefix - k
        if diff in d:
            count += d[diff]
        
        if prefix in d:
            d[prefix ] += 1
        else:
            d[prefix] = 1
    return count
        



# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums 
def maximum_size_subarray_equals_k(nums, k):
    longest = 0
    prefix = 0
    d = dict()
    
    for i in range(len(nums)):
        prefix += 1
        
        if prefix == k:
            longest = i+1
        
        if prefix - k in d:
            longest = max(longest, i - d[prefix-k])
        
        if prefix not in d:
            d[prefix] = i
            
    return longest


# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have in dict
# output: integer of the max length substring possible with k distict letters
def longest_substring_k_distinct_char(s, k):
    d = dict()
    left = 0
    max_len = 0
    
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
        
        max_len = max(max_len, right - left + 1)
    return max_len
    
    
        
    