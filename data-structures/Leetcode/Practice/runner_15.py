# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:51:17 2021

@author: joaqu
"""

# Q1: single number         #1min
# input: array of integers with all nums having a duplicate except 1
# output: the single number in array that has no duplicates
def single_number(nums):
    s = set()
    for i in nums:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    return s.pop()


# Q2: remove duplicates:        #7min
# input: array of int's Sorted w/ or w/o duplicates
# output: int of length of array w/o duplicates or list of array w/o duplicates
def remove_duplicates(nums):
    left = 1
    
    # for i in range(1, len(nums)):
    #     if nums[i-1] != nums[i]:
    #         nums[left] = nums[i]
    #         left+=1
    # return nums[:left]
    
    for i in range(len(nums) - 1):
        if nums[i] != nums[i+1]:
            nums[left] = nums[i+1]
            left += 1
    return nums[:left]



# Q3: remove element        #10min
# input: given array of integers and key_item to remove
# output: return int of length of new list w/o key_item's
def remove_element(nums, key):
    # left = 0
    # right = 0
    # while left <= right:
    #     if nums[left]== key:
    #         nums[left] = nums[right]
    #         right -= 1
    #     else:
    #         left += 1
    left = 0
    for right in nums:
        if right != key:
            nums[left] = nums[right]
            left += 1
    return nums[:left]
    


# Q4: two sum           #10min
# inputs: array of int's and target int
# output: return index of items from array that sum to target
def two_sum(nums, target):
    d = dict()
    
    for i in range(len(nums)):
        remain = nums[i] - target
        
        if remain in d:
            return d[remain], i
        
        else:
            d[nums[i]] = i
            
    return None
        


# Q5: longest_substring_no_duplicates       #10min
# input: string
# output: integer; length of longest non duplicated chars in string
def longest_substring_no_dup(string1):
    s = set()
    longest = 0
    left = 0
    
    for right in range(len(string1)):
        while string1[right] in s:
            s.remove(string1[left])
            left+=1
        s.add(string1[right])
        longest = max(longest, right - left + 1)
    return longest


# Q6: longest prefix
# input: 1-D array of words in a list
# output: string; longest prefix word
def longest_prefix(words):
    shortest = math.inf
    for w in words:
        shortest = min(shortest, len(w))
    
    res = ''
    for i in range(shortest):
        temp = words[0][i]
        for j in range(1, len(words)):
            if temp != words[j][i]:
                return res
        res += temp
    return res


# Q7: group anagrams
# input: 1-D array of strings
# output: a list of all anagrams grouped together correlated to each word/characters
def group_anagrams(words):
    d = dict()
    
    for w in words:
        temp = "".join(sorted(w))
        if temp in d:
            d[temp] += w
        else:
            d[temp] = w
            
    return d.values()


# Q8: valid parenthesis
# input: a string of brackets
# output: Boolean testing if string1 passed as parameter has valid parenthesis
def valid_parenthesis(string1):
    opened = ['(', '{', '[']
    closed = [')', '}', ']']
    stack = []
    
    for c in string1:
        if c in opened:
            stack.append(c)
        else:
            if stack and stack[-1] == opened[closed.index(c)]:
                stack.pop()
            else:
                return False
            
    return len(stack) == 0



# Q9: search rotated array
# input: array sorted than can be rotated left or right, and a target integer
# output: Boolean to see if target is inside the rotated array
def search_sorted_array(nums, target):
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = (right+left) // 2
        
        if nums[mid] == target:
            return True
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False



# Q10: sqrt
# input: integer x
# output: find the number that is the sqrt or closest sqrt of integer
def sqrt(x):
    left = 0
    right = x
    
    while left <= right:
        mid = (left+right) // 2
        
        if mid*mid <= x < (mid+1)*(mid+1):
            return mid
        
        elif mid*mid < x:
            left = mid + 1
        
        elif mid*mid > x:
            right = mid - 1
            
    return -1



# Q11: polish notation
# input: 1-D array of int's and operation symbols
# output: return the polish notation of the given expression
def polish_notation(nums):
    stack = []
    
    for i in nums:
        if i in "+-*/":
            left = stack.pop()
            right = stack.pop()
            
            if i == '+':
                stack.append(left+right)
            elif i == '-':
                stack.append(left-right)
            elif i == '*':
                stack.append(left*right)
            elif i == '/':
                stack.append(int(left//right))
        else:
            stack.append(int(i) )
    return stack.pop()
    

# Q12: two sum - sorted
# input: given a nums array sorted and a given target int
# output: return index of nums in array that equal to target result
def two_sum_sorted(nums, target):
    left = 0 
    right = len(nums) - 1
    
    while left < right:
        if nums[left] + nums[right] == target:
            return left, right
        
        elif nums[left] + nums[right] > target:
            right -= 1
            
        elif nums[left] + nums[right] < target:
            left += 1



# Q13: number of islands
# input: given a 2-D array of 1's and 0's that represent land - 1 and water - 0
# output: return the total number of islands where horizontal and vertical is islands
def num_of_islands(island):
    counter = 0
    
    for i in range(len(island)):
        for j in range(len(island[0])):
            if island[i][j] == 1:
                dfs_island(island, i, j)
                counter += 1
                
    return counter

def dfs_island(island, i, j):
    if i < 0 or i>= len(island) or j < 0 or j >= len(island) or island[i][j] != 1:
        return 
    
    island[i][j] = 0
    
    dfs_island(island, i-1, j)
    dfs_island(island, i+1, j)
    dfs_island(island, i, j-1)
    dfs_island(island, i, j+1)
                
            


# Q14: contains duplicates
# input: given an array of numbers
# output: return boolean if contains duplicate or not
def containes_duplicate(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False


# Q15: move zeros
# input: given an array of numbers
# output: move all zeros to the end and edit nums array in place
def move_zeros(nums):
    zeros = 0
    left = 0
    for right in range(len(nums) ):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
        else:
            zeros += 1
            
    for i in range(zeros):
        nums[-1-i] = 0
        


# Q16: reverse string
# input: 1-D array of letters in a list
# output: reverse all letters in array inplace
def reverse_string(word):
    left = 0
    right = len(word) - 1
    for i in range(len(word) // 2):
        temp = word[left]
        word[left] = word[right]
        word[right] = temp
        left += 1
        right -= 1
    



# Q17: intersection of arrays
# input: (2) 1-D arrays of integers
# output: list of intersecting nums from list1 and list2
def intersection_of_arrays(list1, list2):
    s = set(list1)
    res = []
    
    for i in list2:
        if i in s:
            res.append(i)
            s.remove(i)
            
    return res
            
            

# Q18: binary search
# input: 1-D array of integers and target goal
# output: boolean if found target within n
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (right+left) // 2
        
        if nums[mid] == target:
            return True
        
        if nums[mid] < target:
            left = mid - 1
        else:
            right = mid + 1
            
    return False
        


# Q19: first unique char
# input: given a string called string1 of letters
# output: return int index of first non-repeating char
def first_uniq_char(string1):
    d= dict()
    for c in string1:
        if c in d:
            d[c] += 1
        else:
            d[c] =  1
    
    for k,v in d.items():
        if v == 1:
            return string1.index(k)
    return -1



# Q20: decode string
# input: recieved a string of nums and letters and brackets [,]
# output: return string of decoded string
def decode_string(string1):
    res = ''
    cur_num = 0
    stack = []
    
    for c in string1:
        if c.is_digit():
            cur_num = int(c)
        elif c == '[':
            stack.append(res)
            stack.append(cur_num)
            res = ''
            cur_num = 0
        elif c == ']':
            prev_num = stack.pop()
            prev_str = stack.pop()
            res = prev_str + prev_num*res
        else:
            res += c
    return res



# #Q21: max consecutive one's
# input: 1-D array of 1's and 0's 
# output: integer of the highest amount of consecutive one's
def max_consec_ones(nums):
    longest = 0
    consec = 0
    for i in nums:
        if i == 1:
            consec += 1
        else:
            consec = 0
        longest = max(longest, consec)
    return longest



# Q22: find pivot
# input: takes in 1-D array of int's
# output: return int index that has the right and left side of pivot index equal each other
def find_pivot(nums):
    prefix = 0
    tsum = sum(nums)
    
    for i in nums:
        if prefix == tsum - i - prefix:
            return True
        prefix += i
    return False
            


# Q23: how many days until a hotter day
# input: 1-D array of integers of tempertures
# output: array that shows the days until a hotter days appears corelating to temperature index
def temperatures(nums):
    res = [0] * len(nums)
    stack = []
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]] :
            past = stack.pop()
            res[past] = i - past
        stack.add(i)
    return res
    


# Q24: largest number that is at least double than all others
# input: 1-D array of integers greater than zero
# output: return the index of item that is 2x as big as any other integer
def largest_double_num(nums):
    largest = -math.inf
    lindex = -1
    second = largest
    
    for i in range(len(nums)):
        if nums[i] > largest:
            second = largest
            lindex = i
            largest = nums[i]
        elif nums[i] > second:
            second = nums[i]
    if largest >= (2*second):
        return lindex
        


# Q25: jewels and stones
# input: string called jewels that contain char jewels and string called stones made of char's
# output: return integer of how many stones match the type of jewels
def jewels_and_stones(jewels,stones):
    s = set(jewels)
    counter = 0
    
    for i in stones:
        if i in s:
            counter += 1
    return counter



# Q26: keys and rooms
# input: 2-D array where each bucket is the room and each bucket has room keys
# output: return boolean if you come across each key from previous rooms/buckets visited
# description: you automatically get the room key 0.
def keys_and_rooms(rooms):
    s = set()
    stack = []
    stack.append(0)
    
    while stack:
        cur = stack.pop()
        s.add(cur)
        
        for i in rooms[cur]:
            if not i in s:
                stack.append(i)
                
    return len(s) == len(rooms)


# Q27: squares of sorted array
# input: a sorted array of neg. and pos. integers 
# output: return a 1-D array of sorted integers that are the squares of the input array
def squares_sorted_array(nums):
    left = 0
    right = len(nums) - 1
    res_index = right
    res = [0]*len(nums)
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[res_index] = nums[left]*nums[left]
        else:
            res[res_index] = nums[right]*nums[right]
        res_index -= 1
    return res
    


# Q28: find numbers with even number integers
# input: 1-D array of integers
# output: return how many integers have even amount of integers ex.) 23, 4125, 689030
def find_numbers_with_even_integers(nums):
    counter = 0
    for i in nums:
        temp = 0
        while i:
            i = i//10
            temp+= 1
            
        if temp % 2 == 0:
            counter += 1
            
    return counter




# Q29: check if double int exists
# input: array of integers
# output: return boolean to see if there's an integer that is double than another integer in nums
def check_if_double_exists(nums):
    s = set()
    
    for i in nums:
        if i*2 in s or (i%2==0 and i//2 in s):
            return True
        s.add(i)
    return False


##########################################################################

# Q31: get right side of BST
# input: root of BST
# output: integer values at each level that would appear first if facing BST from the right side
def right_side(root):
    queue = []
    res = []
    queue.append(root)
    
    while stack:
        row_len = len(queue)
        right_side = None
        for i in range(row_len):
            cur = queue.pop(0)
            if cur:
                right_side = cur
                queue.append(cur.left)
                queue.append(cur.right)
            if right_side:
                res.append(right_side.val)
    return res


# Q30: rotate array
# input: 1-d int array of numbers and k the amount to be rotated
# output: nothing, edit in-place array rotating to the right by 'k' times
def rotate_array(nums, k):
    k = k%len(nums)
    if len(num)*k== 0:
        return
    
    reverse(nums, 0, len(nums)-1)
    reverse(nums,0, k-1)
    reverse(nums, k, len(nums)-1)

def reverse(nums, l, r):
    while l < r:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
        r -= 1


# Q29: rotate image
# input: 2-d int array
# output: in-place, rotate the 2-d matrix 90 deg to the right
def rotate_array(nums):
    l = len(nums)
    m = (len(nums) // 2) 
    
    if len(nums[0]) % 2 == 0:
        n = len(nums[0])
    else:
        n = (len(nums[0]) // 2) + 1
    
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            temp = nums[i][j]
            nums[i][j] = nums[l-1-j][i]
            nums[l-1-j][i] = nums[l-1-i][l-1-j]
            nums[l-1-i][l-1-j] = nums[j][l-1-i]
            nums[j][l-1-i] = temp
    
    
# Q28: longest increasing subsequence
# input: 1-d array of integers called nums
# output: return integer of the max numbers of an increasing subsequence inside nums
def longest_increasing_subsequence(nums):
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
    
    
# Q27: unique num of path
# input: integer represent rows 'm', and integer representing num of columns 'n'
# output: integer of the possible ways to reach the bottom right of game board (m x n) only moving 1 right or down
def unique_path(m, n):
    dp = np.zeros((m,n), dtype=int)+1
    
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
            
    return dp[m-1][n-1]
    

# Q26: find peak of mountain
# input: 1-d int array called nums of heights of mounain that go in a straight line
# output: integer index of the peak of the mountain found in nums array
def peak_mounain(nums):
    left = 0
    right = len(nums)
    
    while left < right:
        mid = (right+left) // 2
        
        if nums[mid] > nums[mid+1]:
            right = mid
        else:
            left = mid+1
            
    return left



# Q25: top k frequent items
# input: 1-d array 'nums' of integers that may contain duplicates and integer k 
# output: return a list of integers of len k, that apear the most frequent in 'nums'
def top_k_freq_items(nums, k):
    h1 = []
    res = []
    d = dict()
    
    for i in nums:
        if i in d:
            d[i] -= 1
        else:
            d[i] = -1
        
    for k,v in d.items():
        heapq.heappush(h1, (v,k))
    
    for i in range(k):
        res.append(heapq.heappop() )
        
    return res
        

# Q24: find kth largest element
# input: 1-d array of integers called nums and integer k, representing the kth largest item
# output: integer from nums array that is the kth largest item in nums
def kth_largest_element(nums, k):
    h1 = []
    for i in num:
        heapq.heappush(h1, -1*i)
    
    res = 0
    for i in range(k):
        res = heapq.heappop(h1)
    return res


# Q23: t9 text letter possibility combinations
# input: a string representing a number
# output: a list of string combinations made from the input representing a number
def t9_combo(string1):
    
    t9 = {
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
    stack.append(("0", ""))
    res = []
    while stack:
        cur_len, combo = stack.pop()
        
        if cur_len == len(string1):
            res.apend(combo)
        else:
            next_digit = t9[cur_len]
            children = t9[next_digit]
            for child in children:
                stack.append(cur_len+1, combo+child)
    return res


# Q22: count words with 1 iterator
# input: string of char's and space's
# output: return integer of how many words found in string1
def count_words(words):
    counter = 0
    in_word = False
    for c in words:
        if c != ' ' and in_word == False:
            counter+=1
            in_word = True
        elif c == ' ' and in_word == True:
            in_word = False
    return counter


# Q21: word search
# input: 2-d array of char's called board and a string called 'word'
# output: return boolean if word was found in board moving up,down,left,right 
def word_search(board, word):
    path = set()
    
    def dfs_board(i, j, cur_len):
        if cur_len == len(word):
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j>= len(board[0]) or word[cur_len] != board[i][j] or (i,j) in path:
            return False
        path.add((i,j))
        res = ( dfs_board(i-1,j, cur_len+1) or 
               dfs_board(i+1,j, cur_len+1) or 
               dfs_board(i,j+1, cur_len+1) or 
               dfs_board(i,j-1, cur_len+1) )
        path.remove( (i,j))
        return res
        
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs_board(i,j,0):
                return True
    return False


# Q20: median integer of data stream
# input: 1-D array of integers called 'nums'
# output: return the median integer of the data stream
def median_data_stream(nums):
    hmin = hmax = []
    
    for i in nums:
        heapq.heappush(hmax, -1*i)
        
        if len(hmin) > 0 and len(hmax) > 0 and -1*hmax[0] > hmin[0]:
            val = -1 * heapq.heappop(hmax)
            heapq.heappush(hmin, val)
            
        
        if len(hmax) > len(hmin)+1:
            val = -1*heapq.heappop(hmax)
            heapq.heappush(hmin, val)
        
        if len(hmax)+1 < len(hmin):
            val = heap.heappop(hmin)
            heapq.heappush(hmax, -1*val)
        
        if len(hmin) == len(hmax):
            v1 = heapq.heappop(hmin)
            v2 = heapq.heappop(hmax)
            return (v1+v2) // 2
        else:
            if len(hmin) > len(hmax):
                return heapq.heappop(hmin)
            else:
                return -1*heapq.heappop(hmax)
            
# Q19: longest palindrome
# input: string 's' made of char's
# output: string palindrome that is the longest palindrome found in 's'
def longest_palindrome(s):
    longest = 0
    res = ''
    for i in range(len(s)):
        #ODD
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > longest:
                longest = right - left + 1
                res = s[left:right+1]
            left -= 1
            right += 1
        
        #EVEN
        left = i
        right = i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right-left+1 > longest:
                longest = right-left+1
                res = s[left:right+1]
            left -= 1
            right += 1
        
    return res
            


# Q18: set matrix zeros across col's and row's
# input: 2-d 'matrix' array of 1's and 0's
# output: None, edit 'matrix' in-place replacing the whole row and col where '0' are found
def set_matrix_zeros(matrix):
    rowz = len(matrix) * [0]
    colz = len(matrix) * [0]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rowz[i] = 1
                colz[j] = 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if rowz[i] or colz[j]:
                matrix[i][j] = 0


# Q17: container with most water
# input: 1-d array of int's that represent the height of each mountain at that index
# output: integer of the maximum water being able to be held without spilling
def container_most_water(nums):
    largest = 0
    left = 0
    right = len(nums) - 1
    
    while left < right:
        temp_water = 0
        if nums[left] > nums[right]:
            temp_water = (right-left)*nums[right]
            right -= 1
        else:
            temp_water = (right-left)*nums[left]
            left += 1
        
        largest = max(largest, temp_water)
    return largest
            
            
# Q16: find missing number
# input: 1-d array of int
# output: integer of the missing number in the array 0..n
def find_missing_num(nums):
    tsum = sum(nums)
    n = len(nums)
    
    return ((n*(n+1))//2) - tsum


# Q15: pascal's triangle
# input: integer of the number of rows down you want to travel pascals triangle
# output: a 2-d array of integers that represent pascals triangle
def pascal_triangle(rows):
    res = [ [1] ]
    
    for i in range(1, rows):
        row_len = len(res[-1])
        prev_row = [0] + res[-1] + [0]
        row = []
        
        for j in range(prev_row + 1):
            row.append(prev_row[j] + prev_row[j + 1])
            
        res.append(row)
    return res
    


# Q14: integer to roman numerals
# input: integer called nums
# output: string of the corresponding integer in roman numeral form
def integer_to_roman(nums):
    int_val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]  
    res = ''
    i = 0
    while nums:
        res += (nums//int_val[i]) * roman[i]
        nums = nums % int_val[i]
        i += 1
    return res
    

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
    for i in range(len(string1) ):
        if i+1 < len(string1) and d[string1[i+1]] > d[string1[i]]:
            res -= d[string1[i]]
        else:
            res += d[string1[i]]
    return res
        

# Q12: house robber
# input: 1-d array of integers that represent how much money each house has acording to its position
# output: integer, the maximum money that can be stolen not robing house directly next to each other
def house_robber(nums):
    res = [0]*len(nums)
    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        res[i] = max(res[i-2]+nums[i], res[i-1])
        
    return max(res)


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


# Q10: fibonacci sequence (dp)
# input: integer 'n'
# output: the fibo number of 'n'
def fibo(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
        
    return dp[n]


# Q9: climbing stairs
# input: integer of how many stairs there are
# output: integer of how many ways to reach the top by either taking 1 or 2 steps at a time
def climbing_stairs(n):
    dp = [1] * n
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n):
        dp[i] = dp[i-2]+dp[i-1]
        
    return dp[n-1]
    

# Q8: is palindrome
# input: string called 's' with spaces, nums, special chars
# output: return boolean if string is palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True


# Q7: is anagram
# input: 2 strings that represent words
# output: boolean checking if word 's' is anagram of word 't'
def is_anagram(s, t):
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
    

# Q6: reverse integer
# input: given integer + or -
# output: return the integer reversed unless bigger than SYS.MAXINT
def reverse_integer(n):
    if n < 0:
        symbol = -1
        n = -1*n
    else:
        symbol = 1
    
    rev = 0
    while n:
        rev = rev*10 + (n%10)
        n = n//10
    
    if rev > math.pow(2,31):
        return None
    
    return rev*symbol



# Q5: best time to sell stock 2
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in all transactions
def best_time_to_sell_stock_2(nums):
    maxp = 0
    
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            maxp += nums[i+1] - nums[i]
            
    return maxp


# Q4: best time to sell stock 1
# input: daily prices of stocks in a 1-d array of int's
# output: an integer of the max profit that could be made in 1 transaction
def best_time_to_sell_stock_1(nums):
    min1 = math.inf
    maxp = -math.inf
    
    for i in nums:
        if i < min1:
            min1 = i
            
        tprofit = i-min1
        maxp = max(maxp, tprofit)
        
    return maxp


# Q3: 3 sum
# input: an unsorted integer array w/ or w/o duplicates
# output: a list of 3 number tuplet int's that sum to target (zero), no repeats
def three_sum(nums):
    res = []
    nums.sort()
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums) - 1
        
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                res.append((nums[i] , nums[left], nums[right] ))
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
    return res


# Q2: max sum of subarray
# input: 1-d array of integers both + and -
# output: return the maximum subarray sum found
def max_subarray(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
        
    return max(dp)


# Q1: max product of 3 integers
# input: int array of numbers that are + and -
# output: return an int, being the largest product produced by 3 int's
def max_product(nums):
    max1 = max2 = max2 = -math.inf
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



#####################################################################################

# Q3: subarray sum equals k
# input: 1-d array of int's and 'k' the integer sum goal
# output: return integer of the total amount of continious subarrays that equal to k
def subarray_equals_k(nums, k):
    prefix = 0
    d = dict()
    d[0] = 1
    count = 0
    
    for i in nums:
        prefix += i
        
        if prefix - k in d:
            count += d[prefix-k]
        
        if prefix in d:
            d[prefix] += 1
        else:
            d[prefix] = 1
            
    return count
            


# Q2: Longest Substring with At Most K Distinct Characters
# input: string 's' of letters and integer k determing how many distinct letters we can have at a time
# output: integer of the max length substring possible with k distict letters
def longest_substring_at_most_k_chars(s, k):
    if len(s) * k == 0:
        return 0
    
    d = dict()
    longest = 0
    left = 0
    
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
            
        longest = max(longest, right-left+1)
    return longest
            

# Q1: Maximum Size Subarray Sum Equals k
# input: 1-d array of int's called 'nums' and integer k
# output: integer, the longest subarray that equals to k in nums 
def maximum_size_subarray_equals_k(nums, k):
    longest = 0
    prefix = 0
    
    for i in range(len(nums)):
        prefix += nums[i]
        
        if prefix == k:
            longest = i + 1
        
        if prefix-k in d:
            longest = max(longest, i - d[prefix-k])
        
        if not prefix in d:
            d[prefix] = i
            
    return longest
                


# Q6: is palidrome (integer)
# input: integer above zero
# output: boolean determining if integer is palidrome or not
def is_palindrome_int(n):
    if n < 0:
        return False
    
    if n != 0 and n%10 == 0:
        return False
    
    rev = 0
    while n > rev:
        rev = rev*10 + (x%10)
        n = n//10
    
    return n == rev or n == rev//10
        
    
        
            
    
    
    
    

        