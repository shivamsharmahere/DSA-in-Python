# Find the largest element in an array
# Notes:
# - Initializing with nums[0] instead of float("-inf") is safer because it correctly handles
#   cases where the array might be empty (though accessing nums[0] would still fail, it makes
#   the intent clearer). However, float("-inf") is useful when the array could potentially
#   be empty and you want a default value, or when iterating through multiple arrays.
# - Method 1 (while loop) and Method 2 (for loop) are functionally identical - both O(n).
# - Method 3 with -inf is robust for negative-only arrays and when the initial value should
#   be lower than any possible array element.

nums = [1,6,65,1,6,-98,5,12,12,65,59,89,5,4]

# Method 1: TC - O(n), SC - O(1)
i = 0
largest_element = nums[0]
while i < len(nums):
    if nums[i] > largest_element:
        largest_element = nums[i]
    i += 1

print(largest_element)


# Method 2: TC - O(n), SC - O(1)
largest = nums[0]
for i in range(0,len(nums)):
    largest = max(largest, nums[i])

print(largest)

#Method 3 : Use -inf

largest_no = float("-inf")
for i in range(0,len(nums)):
    largest_no = max(largest_no, nums[i])

print(largest_no)

