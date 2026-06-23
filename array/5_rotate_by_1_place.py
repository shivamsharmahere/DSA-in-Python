# Rotate an array to Right by 1 place
# Notes:
# - Right rotation by 1: last element moves to index 0, all others shift right.
# - Left rotation by 1 would be: first element moves to last index, all others shift left.
# - Method 1 (slicing): Creates a new list even with nums[:] assignment. The [:] ensures
#   we modify the same list object in-place, but the concatenation [nums[-1]] + nums[0:n-1]
#   creates a temporary list of size N. So time is O(N), space is O(N).
# - Method 2 (shifting): Truly in-place with O(1) extra space. We store the last element
#   in temp, shift all elements right by one, then place temp at index 0.
# - Edge case: If array is empty or has 1 element, rotation has no effect.

nums = [5,-2,3,9,0,6,10,7]

# Method 1 : Slicing - TC - O(N), SC - O(N)
n = len(nums)
nums[:] = [nums[-1]] + nums[0:n-1]

print(nums)

print("*******************************************")

# Method 2: In-place shifting - TC - O(N), SC - O(1)

nums = [5,-2,3,9,0,6,10,7]

n = len(nums)
temp = nums[n-1]

for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)
