# Q1. Given an array see if there are any two numbers in the array that add up to a specific target number.
# Notes:
# - Method 1 (brute force): Check all pairs with nested loop. Simple but O(N^2).
#   Prints all pairs that sum to target. Handles duplicates naturally (e.g., [10,10] with target 20).
# - Method 2 (complement search with nested loop): Still O(N^2) - finds complement b = target-a
#   for each a, then searches the rest of array. Slightly more structured than Method 1 but
#   same complexity. Collects results in a list instead of printing.
# - Method 3 (hash map): Optimal - O(N) time, O(N) space. Stores each number's index in a hash
#   map. For each number, check if its complement (target - num) exists in the map.
#   - Returns first pair found as [index1, index2].
#   - To return ALL pairs, you'd need a different approach (e.g., sort + two-pointer for O(N log N),
#     or handle duplicates carefully in the hash map approach).
# - Important: The hash map stores "seen" elements, so when we find a complement, it's from an
#   earlier index. This means returned indices are in ascending order (i < j).
# - If array is sorted, use two-pointer technique: one at start, one at end, move based on sum.
#   This gives O(N) time and O(1) space without a hash map.

nums = [5,9,1,2,4,15,6,3,10,10,13,8]


# Method 1: Brute Force

n = len(nums)
i= 0
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i] + nums[j] == 13:
            print(nums[i],nums[j])

# TC - O(N2)
# SC - O(1)


# Method 2

result = []
def two_sum(arr, target):
    n = len(arr)
    i=0
    j= i+1
    for i in range(n):
        a = nums[i]
        b = target - a
        for j in range(i+1,n):
            if nums[j] == b:
                result.append((a,b))
            else:
                continue
    return result


print(two_sum(nums,13))

# TC - O(n2)
# SC - O(N)

# Method 3 : Optimal

def two_sum_optimal(arr, target):
    n = len(arr)
    i = 0
    hash_map = {}
    for i in range(n):
        remaining = target - nums[i]
        if  remaining in hash_map:
            return [hash_map[remaining],i]
        else:
            hash_map[nums[i]] = i

print(two_sum_optimal(nums,13))

# SC - O(N)
# TC - O(N)