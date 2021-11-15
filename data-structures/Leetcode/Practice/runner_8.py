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
    result = []
    nums.sort()

    for i in range(len(nums)-1 ):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i+1
        right = len(nums)-1
        while left < right:
            t_sum = nums[i] +nums[left] +nums[right]
            if t_sum == 0:
                 result.append( [nums[i] +nums[left] +nums[right]] )
                 left += 1
                 while left < right and nums[left] == nums[left+1]:
                     left += 1
                     
            elif t_sum < 0:
                left += 1
            
            else:
                right -= 1
    return result



# Q4: best time to sell stock 1
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in 1 transaction
def best_time_to_sell_stock_1(nums):
    max_p = -math.inf
    min_p = math.inf
    
    for n in nums:
        min_p = min(min_p, n)
        temp_p = n - min_p
        max_p = max(max_p, temp_p)
        
    return max_p


# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_to_sell_stock_2(nums):
    profit = 0
    
    for i in range(1,len(nums)):
        if nums[i] > nums[i-1]:
            profit += num[i] - nums[i-1]
    return profit


# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
def reverse_integer(x):
    if x<0:
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
    
    return symbol*result



# Q7: is anagram
# input: 2 strings 's' and 't' that represent words
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
    
    for v in d.values():
        if v != 0:
            return False
    
    return True


# Q8: is palindrome
# input: string called 's' with spaces, nums, special chars
# output: return boolean if string is palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        while not s.isalnum() and left < right:
            left +=1 
        
        while not t.isalnum() and left < right:
            right -= 1
    
        if s[left].lower() == t[right].lower():
            left += 1
            right -= 1
        else:
            return False
    return True




# Q9: climbing stairs
# input: integer of how many stairs there are
# output: integer of how many ways to reach the top by either taking 1 or 2 steps at a time
def climbing_stairs(n):
    # if n <= 2:
    #     return n
    
    # dp = [0] * (n+1)
    # dp[1] = 1
    # dp[2] = 2
    
    # for i in range(3, (n+1)):
    #     dp[i] = dp[i-1] + dp[i-2]
        
    # return dp[n]
    if n <= 2:
        return n
    
    forward = backward = 1
    
    for i in range(n-1):
        temp = forward
        forward = backward+forward
        backward = temp
    
    return forward
        

# Q10: fibonacci sequence (dp)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo_sequence(n):    
    result = [0] * (n+1)
    result[0] = 0
    result[1] = 1
    
    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]


# Q11: fibonacci sequence (o1 space)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo(n):
    if n <= 1:
        return n
    
    forward = 1
    backward = 0
    
    for i in range(n-1):
        temp = forward
        forward = backward+forward
        backward = temp
    
    return forward


# Q12: house robber
# input: 1-d array of integers that represent how much money each house has acording to its position
# output: integer, the maximum money that can be stolen not robing house directly next to each other
def house_robber(nums):
    dp = [0] * len(nums) 
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    max_p = 0
    
    for i in range(2,len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
    return max(dp)


# Q13: roman string to integer
# input: string that is written in roman
# output: integer of the roman string in numbers
def roman_to_integer(s):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000}
    
    if len(s) == 1:
        return roman[s[0] ]
    
    result = 0
    for i in range(len(s) ):
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]  
    return result

# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def int_to_roman(num):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numeral = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    result = ""
    i = 0
    
    while num:
        result += (num // int_val[i]) * numeral[i]
        num = num % int_val[i]
        i = i + 1
    return result



# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triangle(row):
    result = [ [1] ]
    
    for i in range(row-1):
        row = []
        prev = [0] + result[-1] + [0]
        
        for j in range( len(result[-1] + 1) ):
            row.append( prev[j] + prev[j+1] )
            
        result.append(row)
    return result



    
# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def find_missing_num(nums):
    
    t_sum = sum(nums)
    n = len(nums)
    
    return ((n*(n+1)) // 2 ) - t_sum
    

# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def container_with_most_water(nums):
    left = 0
    right = len(nums) - 1
    max_water = -math.inf
    
    while left < right:
        if nums[left] > nums[right]:
            max_water = max( max_water, nums[right] * (right-left) )
            right -= 1
        else:
            max_water = max( max_water, nums[left] * (right-left) )
            left += 1
    return max_water


# Q18: set matrix zeros across col's and row's
# input: 2-d 'matrix' array of 1's and 0's
# output: None, edit 'matrix' in-place replacing the whole row and col where '0' are found
def set_zeros_matrix(matrix):
    col_z = [0]* len(matrix[0])
    row_z = [0] * len(matrix)
    
    for i in range(len(matrix) ):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_z[i] = 1
                col_z[i] = 1
    
    for i in range(len(matrix) ):
        for j in range(len(matrix[0])):
            if row_z[i] == 1 or col_z[j] == 1:
                matrix[i][j] = 0
    
    
# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
def longest_palindrome(s):
    result = ''
    longest = 0
    for i in range(len(s)):
        #odd
        left = right = i
        
        while [left] == s[right] and left >= 0 and right < len(s):
            if right-left+1 > longest:
                longest = right-left+1
                result = s[left:right+1]
            left += 1
            right -= 1
        
        
        #even
        left = i
        right = i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right-left+1 > longest:
                longest = right-left+1
                result = s[left:right+1]
            left += 1
            right -= 1
    
    return result
            


# Q20: median integer of data stream
# input: 1-D array of integers called 'nums'
# output: return the median integer of the data stream
# MAX heap     -       MIN Heap
#9, 8, 4, 2    -     10, 14, 15, 17
def median_data_stream(nums):
    hmin = hmax = []
    
    for i in nums:
        heapq.heappush(hmax, -1*i)
            
        if len(hmax) > 0 and len(hmin) > 0 and hmax[0] > hmin[0]:
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
    path = set()
    
    def dfs_board(i,j, c_len):
        if c_len == len(word):
            return True
        
        if i< 0 or i>= len(word) or j < 0 or j>= len(word) or board[i][j] != word[c_len] or (i,j) in path:
            return False
        
        path.add((i,j) )
        res = (dfs_board(i-1,j, c_len + 1) or
               dfs_board(i+1,j,c_len+1) or
               dfs_board(i,j-1,c_len+1) or
               dfs_board(i,j+1,c_len+1) )
        path.remove( (i,j) )
        return res
        
    for i in range(len(board) ):
        for j in range(len(board[0])):
            if dfs_board(i,j, 0):
                return True
    return False



# Q22: count words with 1 iterator
# input: string of char's and space's
# output: return integer of how many words found in string1
def count_words(string1):
    in_word = False
    count = 0
    
    for c in string1:
        if c != ' ' and in_word == False:
            count += 1
            in_word = True
        
        elif ' ' and in_word == True:
            in_word = False
        
    return count


# Q23: t9 text letter possibility combinations
# input: a string representing a number
# output: a list of string combinations made from the input representing a number
def t9_combo(string1):
    if not string1:
        return
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
    
    result = ''
    stack = []
    stack.append((0, ""))
    
    while stack:
        c_len, combo = stack.pop()
        
        if c_len == len(string1):
                result.append(combo)
        else:
            next_digit = string1[c_len]
            children = d[next_digit]
            for child in children:
                stack.append( (c_len+1, combo+child))
                
    return result



# Q24: find kth largest element
# input: 1-d array of integers called nums and integer k, representing the kth largest item
# output: integer from nums array that is the kth largest item in nums
def kth_largest_element(nums, k):    
    h1 = []
    
    for i in nums:
        heapq.heappush(h1, -1*i)
    
    res = heapq.nlargest(k, h1)
    return res[-1]
    
    

# Q25: top k frequent items
# input: 1-d array 'nums' of integers that may contain duplicates and integer k 
# output: return a list of integers of len k, that apear the most frequent in 'nums'
def top_k_freq_items(nums, k):
    d = dict()
    
    for i in nums:
        if i in d:
            d[i] -= 1
        else:
            d[i] = -1
    
    h1 = []
    for k,v in d.items():
        heapq.heappush(h1, (v, k) )
    
    res = []
    count = 0
    
    while count < k:
        freq, n = heapq.heappop(h1)
        res.append(n)
        count += 1
        
    return result



# Q26: find peak of mountain
# input: 1-d int array called nums of heights of mounain that go in a straight line
# output: integer index of the peak of the mountain found in nums array
def find_peaks(nums):
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
def find_unique_path(m, n):
    dp = np.zeros( (m,n), dtype=int)+1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return np[m-1][n-1]



# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increasing_subsequence(nums):
    longest = 0
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j] )
                
    return max(dp)




# Q29: rotate image
# input: 2-d int array
# output: in-place, rotate the 2-d matrix 90 deg to the right
def rotate_image(matrix):
    n = len(matrix)
        
    cols = (len(matrix) // 2) 
    
    if len(matrix) % 2 == 0:
        rows = (len(matrix) // 2 )            
    else:
        rows = (len(matrix) // 2 ) + 1
    
    
    for i in range( rows ): #up and down
        for j in range(cols): # left and right (exclude middle)
            
            temp = matrix[i][j]  # save top left
            
            matrix[i][j] = matrix[n-1-j][i] #bottom left to top left
            
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]  #bottom right to bottom left
            
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i] #top right to bottom right
            
            matrix[j][n-1-i] = temp #temp to top right
            

# Q30: rotate array
# input: 1-d int array of numbers and k the amount to be rotated
# output: nothing, edit in-place array rotating to the right by 'k' times
def rotate_array(nums, k):
    left = 0 
    right = len(nums) - 1
    k = k% len*nums
    reverse(nums, left, right)
    reverse(nums, 0, k-1)
    reverse(nums, k, right)

def reverse(nums,l,r):
    while left < right:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l+=1
        r-=1
    

# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def get_right_side(root):
    result = []
    queue = []
    queue.append(root)
    
    while queue:
        row_len = len(queue)
        right_side = None
        
        for i in range(row_len):
            node = queue.pop(0)
            if node:
                stack.append(node.left)
                stack.append(node.right)
        if right_side:
            result.append(right_side.val)
    return result
        

    