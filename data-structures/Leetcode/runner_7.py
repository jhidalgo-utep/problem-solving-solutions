# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:59:27 2021

@author: joaqu
"""
import heapq

# Q1: max product of 3 integers
# input: int array of numbers that are + and -
# output: return an int, being the largest product produced by 3 int's
def max_product_of_3(nums):
    max1 = max2 = max3 = -math.inf
    min1 = min2 = math.inf
    
    for i in nums:
        if i >= max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i >= max2:
            max3 = max2
            max2 = i
        elif i >= max3:
            max3 = i
        
        if i <= min1:
            min2 = min1
            min1 = i
        elif i <= min2:
            min2 = i
    
    return max(max1*max2*max3, min1*min2*max1)


# Q2: max sum of subarray
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_sum_subarray(nums):
    result = [0] * len(nums)
    result[0] = nums[0]
    
    for i in range(1, len(nums) ):
        result[i] = max(nums[i-1] + nums[i], nums[i])
    
    return max(result)



# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums)-1 ):
        if i > 0 and nums[i] == nums[i-1]:
            continue #skip to avoid duplicates
        
        left = i+1
        right = len(nums)-1
        
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                result.append( [nums[i], nums[left], nums[right] ] )
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left+=1
            
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
                
            else:
                right -= 1
                
    return result


# Q4: best time to sell stock 1
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in 1 transaction
def best_time_to_sell_stock_1(nums):
    max_profit = max1
    min1 = math.inf
    
    for i in nums:
        min1 = min(i, min1)
        profit = i - min1
        max_profit = max(max_profit, max1-min1)
        
    return max_profit
            

# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_to_sell_stock_2(nums):
    profit = 0
    for i in range(len(nums) ):
        
        if nums[i] > nums[i]:
            profit += nums[i] - nums[i+1]
            
        return profit
        


# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
def reverse_integer(x):
    if x < 0:
        symbol = -1
        x = -1 * x
    else:
        symbol = 1
    
    result = 0
    
    while x:
        result = (result * 10) + (x % 10)
        x = x // 10
    
    if result > math.pow(2,31):
        return 0
    
    return symbol * result



# Q7: is anagram
# input: 2 strings that represent words
# output: boolean checking if word 's' is anagram of word 't'
def anagram(string1, string2):
    d = dict()
    
    if len(string1) != len(string2):
        return False
    
    for c in string1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    
    for c in string2:
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
    left = 0
    right = len(s) - 1
    
    while left < right:
        while not left.isalnum() and left<right:
            left += 1
        
        while not right.isalnum() and left<right:
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
        
        left +=1
        right -=1
        
    return True



# Q9: climbing stairs
# input: integer of how many stairs there are
# output: integer of how many ways to reach the top by either taking 1 or 2 steps at a time
def climbing_stairs(x):
    forward = backward = 1
    
    for i in range(x-1):
        temp = forward
        forward = backward + forward
        backward = temp
    
    return forward

    # if n== 1 or n == 2:
    #     return n
    
    # dp = [0] * (n+1)
    
    # dp[1] = 1
    # dp[2] = 2
    
    # if n <0:
    #     return
    
    # for i in range(3, n+1):
    #     dp[i] = dp[i-1] + dp[i-2]
    
    # return dp[n]
    
    

# Q10: fibonacci sequence (dp)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo_num(n):
    # if n <= 1:
    #     return n
    
    # return fibo(n-1) + fibo(n-2)
    
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]



# Q11: fibonacci sequence (o1 space)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo2(n):
    if n<=1:
        return n
    
    forward = backward = 1
    
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
    
    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 2:
        return max(nums[0], nums[1] )
    
    dp = [0] * (len(nums) + 1)
    d[1] = nums[0]
    d[2] = max(nums[0], nums[1] )
    
    for i in range(3, len(nums)+1):
        dp[i] = max(dp[i-2] + dp[i], dp[i-1] )
    
    return max(dp )


# Q13: roman string to integer
# input: string that is written in roman
# output: integer of the roman string in numbers
def roman_to_integer(string1):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    result = 0
    for c in range(len(string1)-1 ):
        if c+1 < len(string1) and roman[c] < roman[c+1]:
            result -= roman[string1[c] ]
        else:
            result += roman[string1[c] ]
    return result


# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def integer_to_roman(num):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numeral = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    result = 0
    i = 0
    
    while num:
        result += (num//int_val[i]) * numeral[i]
        num = num % int_val[i]
        i+=1
        
    return result
    


# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triangle(num_rows):
    result = [ [1] ]
    
    for i in range(num_rows-1):
        prev_row = [0] + result[-1] + [0]
        temp_row = []
        
        for j in range(len(result[-1]) + 1):
            temp_row.append(prev_row[j]+prev_row[j+1])
        result.append(temp_row)
    
    return result



# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def find_missing_number(nums):
    t_sum = sum(nums)
    return (( len(nums)* (len(nums)+1) ) // 2) - t_sum



# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def contain_most_water(nums):
    max_contain = -math.inf
    
    left = 0
    right = len(nums)-1
    
    while left < right:
        
        if nums[left] <= nums[right]:
            max_contain = max(max_contain, (right-left)*nums[left] )
            left += 1
            
        elif nums[left] > nums[right]:
            max_contain = max(max_contain, (right-left)*nums[right] )
            right -= 1
    
    return max_contain



# Q18: set matrix zeros across col's and row's
# input: 2-d 'matrix' array of 1's and 0's
# output: None, edit 'matrix' in-place replacing the whole row and col where '0' are found
def set_matrix_zeros(matrix):
    m = len(matrix)
    n = len(matrix[0] )
    
    row_z = m * [0]
    col_z = n * [0]
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_z[i] = 1
                col_z[j] = 1
    
    for i in range(m):
        for j in range(n):
            if row_z[i] == 1 or col_z[j] == 1:
                matrix[i][j] = 0
    


# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
def longest_palindrome(s):
    result = ''
    res_len = 0
    
    for i in range(len(s) ):
        #odd
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > res_len:
                res_len = r-l+1
                result = s[l:r+1]
            left -= 1
            right += 1
        
        
        #even
        l = i
        r = i+1
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res_len = r - l + 1
                result = s[l:r+1]
            l -= 1
            r += 1
        
    return result


# Q20: median integer of data stream
# input: 1-D array of integers called 'nums'
# output: return the median integer of the data stream
# MAX heap     -       MIN Heap
#9, 8, 4, 2    -     10, 14, 15, 17
def median_data_stream(nums):
    hmax = hmin = []
    
    for i in range(len(nums) ):
        heapq.heappush(hmin, nums[i])
        
        if len(hmax) != 0 and len(hmin) != 0 and (-1*hmax[0] > hmin[0]):
            val = -1*heapq.heappop(hmax)
            heapq.heappush(hmin, val)
            
        if len(hmax) > len(hmin) + 1:
            val = -1*heapq.heappop(hmax)
            heapq.heappush(hmin, val)
        
        if len(hmax) + 1 < len(hmin):
            val = heapq.heappop(hmin)
            heapq.heappush(hmax, -1*val)
        
    
    if len(nums) % 2 == 0:
        val = ( (-1*heapq.heappop(hmax)) + heapq.heappop(hmin) ) / 2
        return val
    else:
        if len(hmax) > len(hmin):
            return -1*heapq.heappop(hmax)
        else:
            return heapq.heappop(hmin)
            
        

# Q21: word search
# input: 2-d array of char's called board and a string called 'word'
# output: return boolean if word was found in board moving up,down,left,right 
def word_search(board, word):
    rows = len(board)
    cols = len(board[0])
    path = set()
    
    def dfs_board(r,c,i):
        if i == len(word):
            return True
        
        if r<0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c] or (r,c) in path:
            return False
        
        path.add((r,c) )
        
        res = (dfs_board(r+1, c, i+1) or
            dfs_board(r-1), c, i+1 or
            dfs_board(r, c-1, i+1) or
            dfs_board(r, c+1, i+1))
        
        path.remove((r,c) )
        
        return res
        
    for i in range(rows):
        for j in range(cols):
            if dfs_board(i,j, 0):
                return True
    return False
        


# Q22: count words with 1 iterator
# input: string of char's and space's
# output: return integer of how many words found in string1
def count_words(words):
    result = 0
    in_word = False
    
    for c in words:
        if c != ' ' and in_word == False:
            result += 1
            in_word = True
        
        elif c == ' ' and in_word == True:
            in_word = False
            
    return result


# Q23: t9 text letter possibility combinations
# input: a string representing a number
# output: a list of string combinations made from the input representing a number
def t9_text(string1):

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
    
    result = []
    stack = []
    stack.append((0,"") )
    
    while stack:
        curr_len, combo = stack.pop()
        
        if curr_len == len(string1):
            result.append(combo)
        
        else:
            next_digit = string1[curr_len]
            children = d[next_digit]
            for child in children:
                stack.append(curr_len + 1, combo+child)
    return result



# Q24: find kth largest element
# input: 1-d array of integers called nums and integer k, representing the kth largest item
# output: integer from nums array that is the kth largest item in nums
def find_k_largest(nums, k):
    h1 = []
    
    for i in nums:
        heapq.heappush(h1, i)
    
    res = heapq.largest(k,h1)
    
    return res[-1]


# Q25: top k frequent items
# input: 1-d array 'nums' of integers that may contain duplicates and integer k 
# output: return a list of integers of len k, that apear the most frequent in 'nums'
def freq_k_items(nums, k):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return nums[0]
    
    d = dict()
    for i in nums:
        if i in d:
            d[i] -= 1
        else:
            d[i] = -1
    
    h1 = []
    
    for k,v in d.items():
        heapq.heappush(h1, (v,k))
        
    res = []
    count = 0
    while count < k:
        freq, word = heapq.heappop(h1)
        res.append(word)
        count+= 1
    
    return res




# Q26: find peak of mountain
# input: 1-d int array called nums of heights of mounain that go in a straight line
# output: integer index of the peak of the mountain found in nums array
def find_peaks(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left+right) // 2
        
        if nums[mid] >= nums[mid+1]:
            right = mid
        else:
            left = mid + 1
            
    return left
    


# Q27: unique num of path
# input: integer represent rows 'm', and integer representing num of columns 'n'
# output: integer of the possible ways to reach the bottom right of game board (m x n) only moving 1 right or down
def unique_path(m,n):
    temp = np.zeros( (m,n), dtype=int)+1
    
    for i in range(1,m):
        for j in range(1,n):
            temp[i][j] = temp[i-1][j] + temp[i][j-1]
    
    return temp[m-1][n-1]



# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increasing_subseq(nums):
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, len(nums) ):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1+dp[j] )
                
    return max(dp)


# Q29: rotate image
# input: 2-d int array
# output: in-place, rotate the 2-d matrix 90 deg to the right
def rotate_image(arr):
    arr_len = len(arr)
    
    cols = arr_len // 2
    
    if arr_len % 2 == 0:
        rows = arr_len // 2
    else:
        rows = arr_len // 2
    
    for i in range(m):
        for j in range(n):
            temp = arr[i][j]  #save top left
            
            arr[i][j] = arr[arr_len - 1 - j][i] #bottom left to top left
            
            arr[arr_len - 1 - j][i] = arr[arr_len-1-i][arr_len-1-j] #bottom right to bottom left
            
            arr[arr_len-1-i][arr_len-1-j] = arr[j][arr_len-1-i] #top right to bottom right
            
            arr[j][arr_len-1-i] = temp #top left to top right
            
            

# Q30: rotate array
# input: 1-d int array of numbers and k the amount to be rotated
# output: nothing, edit in-place array rotating to the right by 'k' times
def rotate_array(nums):
    k = k % len(nums)
    
    if len(nums) <= 1 or k == 0:
        return
    
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1 )

def reverse(nums, l, r):
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1
    
    

# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def right_side_BST(root):
    queue = []
    res = []
    queue.append(root)
    
    while queue:
        row_len = len(queue)
        right_side = None
        
        for i in range(row_len):
            node = queue.pop(0)
            if node:
                right_side = node
                queue.append(root.left)
                queue.append(root.right)
            
        if right_side:
            res.append(right_side.val)
            
    return res
        
            
        
# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums
def maximum_size_subarray(nums, k):
    longest = 0
    prefix_sum = 0
    d = dict()
    
    for i in range(len(nums) ):
        prefix_sum += nums[i]
        
        if prefix_sum == k:
            longest = i+1
        
        if prefix_sum - k in d:
            longest = max(longest, i - d[prefix_sum - k] )
        
        if prefix_sum not in d:
            d[prefix_sum] = i
            
    return longest



# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have in dict
# output: integer of the max length substring possible with k distict letters
def longest_substring_k_distinct_letter(s, k):
    n = len(s)
    if n*s == 0:
        return 0
    
    left = 0
    d = dict()
    max_len = 1
    
    for right in range(n):
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
        
        max_len = max(max_len, right-left+1)
    return max_len


# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_sum_equals_k(nums, k):
    d = dict()
    d[0] = 1
    
    prefix_sum = 0
    count = 0
    
    for i in range(len(nums) ):
        prefix_sum += nums[i]
        
        if prefix_sum - k in d:
            count += d[prefix_sum - k]
        
        if prefix_sum in d:
            d[prefix_sum] += 1
        else:
            d[prefix_sum] = 1
    
    return count
        

# Q4: Sliding Window Maximum
# input: 1-d array of integers and integer 'k' that is the size of the window
# output: integer array of the all the maximum int's at each combination subarray of size k
def sliding_window_max(nums, k):
    left = 0
    result = []
    dq = []
    
    for right in range(len(nums) ):
        while dq and nums[dq[-1] ] <= nums[right]:
            dq.pop(-1)
    
        dq.append(right)
        
        if left > dq[0]:
            dq.pop(0)
        
        if right+1 >= k:
            result.append(nums[dq[0]] )
            left += 1
            
    return result


# Q5: Top K frequent words
# input: 1-D array of string words and integer k for the amount of top freq. words
# output: a list of the top 'k' frequent words
def top_k_words(words, k):
    d = dict()
    
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[q] = 1
    
    h1 = []
    for key in d:
        heapq.heappush(h1, (-1*d[key], key) )
    
    result = []
    for i in range(k):
        freq, word = heapq.heappop(h1)
        result.append(word)
        
    return result
    

# Q6: is palidrome (integer)
# input: integer above zero
# output: boolean determining if integer is palidrome or not
def is_palindrome_integer(x):
    if x < 0:
        return False
    if x%10 == 0 and x != 0:
        return False
    
    reverted_num = 0
    
    while reverted_num < x:
        reverted_num = reverted_num*10 + x%10
        x = x//10
    
    if x == reverted_num or x == reverted_num // 10:
        return True
    return False
    
if __name__ == "__main__":
    print('start\n')
    
    print( climbing_stairs() )