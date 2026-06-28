# Q. You are given an array and you need to find the missing number from that array
# Assumption: Array contains numbers from 0 to n (or 1 to n) with exactly one missing.
# Notes:
# - Method 1 (brute force): Checks each number from 0 to n if it exists in array.
#   `in` operator on list is O(N), so nested loop gives O(N^2). Horrible for large arrays.
# - Method 2 (hash map): Marks presence of each number in O(N), then scans map in O(N).
#   Bug in current code: freq is a global variable that persists state across calls.
#   Also, initializing freq with keys 0 to n-1 is wrong - should be 0 to n since
#   missing number could be n (when array has 0 to n-1). Should use set() instead.
# - Method 3 (math formula): Most elegant. Sum of 0..n is n*(n+1)/2. Subtract sum of
#   array elements to get the missing number. O(N) time, O(1) space.
# - Alternative: XOR approach. XOR of 0..n XOR XOR of all array elements = missing number.
#   Works because x ^ x = 0 and x ^ 0 = x. Also O(N) time, O(1) space.
#   Advantage: No overflow issues for very large n (unlike the sum formula in languages
#   with fixed integer sizes, though Python handles big ints fine).

# Method 1: Brute Force

nums = [9,8,7,5,6,2,3,1,0]

n = len(nums)
 
for i in range(n+1):
    if i not in nums:
        print(i)

# TC - O(N^2)
# SC - O(1) 

# Method 2: Optimal

freq = {}   
def find_missing(arr):
    for i in range(n):
        freq[i] = 0
    
    for num in nums:
        freq[num] = 1
        
    for k,v in freq.items():
        if v == 0:
            return k

print(find_missing(nums))

# TC - O(N) + O(n) + O(n) = o(3n) ~ O(N)
# SC - O(N)

# Method 3 Optimal :

def missing_no(arr) :
    n = len(arr)
    result = int(n*(n+1)/2) - sum(nums)
    return result

print(missing_no(nums))