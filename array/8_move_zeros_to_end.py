# Move all the zeros in an array to the end while maintaining the relative order of the non-zero elements inplace.
# Notes:
# - The key constraint is "maintain relative order of non-zero elements" - this rules out
#   a simple swap-based approach that might reorder non-zeros.
# - Method 1 (temp array): Straightforward but uses O(N) extra space. Not truly in-place.
# - Method 2 (two-pointer overwrite): Optimal in-place. i tracks where to write next non-zero.
#   After all non-zeros are written, fill remaining positions with 0.
# - Method 3 (two-pointer swap): Also in-place O(1) space. i tracks first zero, j scans for
#   non-zeros and swaps. This preserves relative order because j always moves ahead of i,
#   and we only swap when we find a non-zero after a zero.
# - Method 4 (partition-style): Similar to Method 3 but more concise. Works like the partition
#   step in quick sort where we treat zeros as "smaller" elements.
# - All methods preserve the relative order of non-zero elements.

nums = [1,0,2,6,4,9,-5,0,3,5,0,0,6,4,0,54,2,4,6]

#Method 1 : Brute Force

n = len(nums)
temp = []

for e in nums:
    if e != 0:
        temp.append(e)

n2 = len(temp)
for i in range(0,n2):
    nums[i] = temp[i]
for i in range(n2,n):
    nums[i] = 0

print(nums)

# TC - 1st loop: o(N) , 2nd + 3rd loop: O(N)
# SC - O(N) as in the worst case the temp can be full if their is no 0 in the original array


print("************************Method 2***********************************")

nums = [1,0,2,6,4,9,-5,0,3,5,0,0,6,4,0,54,2,4,6]

def move(nums):
    i = 0
    for e in nums:
        if e != 0:
            nums[i] = e
            i += 1

    while i < len(nums):
        nums[i] = 0
        i += 1

    return nums

print(move(nums))

# TC - O(N)
# SC - O(1)

print("**************** Method 3 ******************")

nums = [1,0,2,6,4,9,-5,0,3,5,0,0,6,4,0,54,2,4,6]

def move_zero(arr):
    i = 0
    n = len(arr)
    if len(arr) == 1:
        return
    while i < len(arr):
        if arr[i] == 0:
            break
        i += 1
    
    if i == len(arr):
        return 
    j = i +1

    while j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    
    return arr

print(move_zero(nums))

# TC - partial iteration + partail iteration = O(N)
# SC - O(1)

print("****************** METHOD 4 ******************")

nums = [1,6,5,0,0,1,5,1,2,0]

def move_zeroes(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums

print(move_zeroes(nums))