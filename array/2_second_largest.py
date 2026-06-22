# Find the second largest element
# Notes:
# - If array has fewer than 2 elements, second largest doesn't exist.
# - If all elements are same, there is no second largest distinct element.
# - Must handle duplicates correctly (second largest should be distinct from largest).

nums = [1,6,65,1,6,-98,5,12,12,65,59,89,5,4,651]

# Method 1: Sort and pick second last
# WARNING: nums.sort() sorts IN-PLACE and returns None. So nums_sorted = nums.sort()
# assigns None to nums_sorted. Use nums.sort() alone, or sorted(nums) for a new list.
# Not optimal because sorting is O(nlogn) when we can do it in O(n).

nums.sort()
largest_no = nums[-2]
print("Second Largest:", largest_no)

# TC - O(nlogn), SC - O(1) or O(n) depending on sort implementation

#Method 2: Better - two passes

largest = float("-inf")
for i in range(0,len(nums)):
    largest = max(largest, nums[i])

largest2 = float("-inf")
for i in range(0,len(nums)):
    if nums[i] > largest2 and nums[i] < largest:
        largest2 = nums[i]

print("Largest:" ,largest)
print("Second Largest:",largest2)

# TC - O(2n) = O(n), SC = O(1)
# Still not optimal - we traverse the array twice.


# OPTIMAL SOLUTION - Single pass
# Key insight: Track largest (l) and second largest (sl) simultaneously.
# - When current element > l: old l becomes sl, current becomes new l
# - When current element is between sl and l: update sl
# - The condition `nums[i] < l` ensures we handle duplicates correctly.
#   Example: [12, 12, 65, 65, 59] -> largest=65, second_largest=59
# Edge case: If array has all same elements, sl remains -inf.
# Edge case: If array length < 2, no second largest exists.

l = float("-inf")
sl = float("-inf")

for i in range(0,len(nums)):
    if nums[i] > l :
        sl = l
        l = nums[i]
    elif nums[i] > sl and nums[i] < l:
        sl = nums[i]

print("Largest:", l)
print("Second Largest:", sl)

# TC - O(N), SC - O(1)