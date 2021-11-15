# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:59:27 2021

@author: joaqu
"""

# Q1: max product of 3 integers 
# input: int array of numbers that are + and -
# output: return an int, being the largest product produced by 3 int's
def max_product(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return nums[0]*nums[1]
    
    min1 = min2 = math.inf
    max1 = max2 = max3 = -math.inf
    
    for num in nums:
        if num >= max1:
            max3 = max2 
            max2 = max1
            max1 = num
            
        elif num >= max2:
            max3 = max2
            max2 = num
            
        elif num >= max3:
            max3 = num
        
        if num <= min1:
            min2 = min1
            min1 = num
        elif num <= min2:
            min2 = num
            
    return max(max1*max2*max3, min1*min2*max1)


# Q2: max sum of subarray
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_sum_subarray(nums):
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums)):
        dp[i] = max(dp[-1]+nums[i], nums[i])
    
    return max(dp)


# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i+1
        right = len(nums)-1
        
        while left < right:
            if nums[i] + num[left] + nums[right] == 0:
                res.append((nums[i] + num[left] + nums[right]))
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            
            elif nums[i] + num[left] + nums[right] < 0:
                left += 1
            elif nums[i] + num[left] + nums[right] > 0:
                right -= 1
                
    return res


# Q4: best time to sell stock 1
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in 1 transaction
def best_time_to_sell_stock_1(prices):
    maxp = 0
    min1 = math.inf
    
    for p in prices:
        if p < min1:
            min1 = p
        
        cur_profit = p - min1
        
        maxp = max(maxp, cur_profit)
        
    return maxp



# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_to_sell_stock_2(prices):
    maxp = 0
    
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            maxp += prices[i+1] - prices[i]
            
    return maxp



# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
def reverse_integer(num):
    if num < 0:
        symbol = -1
    else:
        symbol = 1
    
    rev = 0
    while num:
        rev = rev*10 + (num%10)
        num = num // 10
    
    if rev > math.pow(2,31):
        return 0
    
    return rev*symbol



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


# Q8: is palindrome          #2 min
# input: string called 's' with spaces, nums, special chars
# output: return boolean if string is palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left<right and not s[left].isalnum():
            left += 1
        
        while left<right and not s[right].isalnum():
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
    # if n == 0:
    #     return 0
    
    # dp = [0] * n
    # for i in range(2, n):
    #     if i == 0:
    #         dp[i] = 1
    #     elif i == 1:
    #         dp[i] = 2
    #     else:
    #         dp[i] = dp[i-2] + dp[i-1]
            
    # return dp[n-1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
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
    # if n == 0:
    #     return 0
    # if n== 1:
    #     return 1
    # return fibo(n-1) + fibo(n-2)
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[0] = 0
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
def house_robber(homes):
    dp = [0]*len(homes)
    dp[0] = homes[0]
    dp[1] = max(homes[0], homes[1])
    
    for i in range(2, len(homes) ):
        dp[i] = max(dp[i-2]+homes[i], dp[i-1])
    return max(dp)


# Q13: roman string to integer
# input: string that is written in roman
# output: integer of the roman string in numbers
def roman_to_integer(string1):
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
        if i + 1 < len(string1) and d[string1[i]] < d[string1[i + 1]]:
            res -= d[string1[i]]
        else:
            res += d[string1[i]]
    return res


# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def integer_to_roman(num):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    res = ''
    i = 0
    while num:
        res += (num//int_val[i]) * roman[i]
        num = num % int_val[i]
        i+= 1
        
    return res
        

# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triangle(rows):
    res = [ [1] ]
    
    for i in range(rows-1):
        temp = [0] + res[-1] + [0]
        r = []
        
        for i in range(len(res[-1])+ 1):
            r.append(temp[i] + temp[i+1] )
        
        res.append(r)
    return res


# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def find_missing_num(nums):
    tsum = sum(nums)
    n = len(nums)
    
    return ((n*(n+1))//2)-tsum



# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def container_most_water(nums):
    max_water = 0
    left = 0 
    right = len(nums) - 1
    
    while left < right:
        if nums[left] < nums[right]:
            max_water = max(max_water, nums[left]*(right-left) )
            left += 1
        else:
            max_water = max(max_water, nums[right]*(right-left) )
            right -= 1
    return max_water


# Q18: set matrix zeros across col's and row's
# input: 2-d 'matrix' array of 1's and 0's
# output: None, edit 'matrix' in-place replacing the whole row and col where '0' are found
def set_matrix_zeros(matrix):
    rowz = [0] * len(matrix)
    colz = [0] * len(matrix[0])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix == 0:
                rowz[i] = 1
                colz[i] = 1
                
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rowz[i] == 1 or colz[j] == 1:
                matrix[i][j] = 0


# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
            
        
    
    

    
    
    
    
    
