# Q1. Find the maximum subarray sum in an array
# A subarray is a contiguous part of the array
# Maximum subarray sum = the largest sum of any contiguous subarray

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Method 1 : Brute Force
# Try all possible subarrays and find the maximum sum
def brute_max_subarray(arr):
    # Initialize max sum to negative infinity to handle all negative arrays
    i, j = 0, 0
    maxi = float("-inf")
    n = len(arr)
    # For each starting index, calculate sum of all subarrays from that index
    for i in range(n):
        total = 0
        for j in range(i, n):
            total = total + arr[j]
            maxi = max(maxi, total)

    return maxi

print(brute_max_subarray(nums))

# TC - O(N(N+1)/2) ~ O(N2)
# SC - O(1)

print("********** METHOD 2 **************")

# Method 2: Optimal (Kadane's Algorithm)
# Idea: Keep track of running sum, reset to 0 when it becomes negative
# This works because a negative prefix can never contribute to maximum subarray sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def optimal_max_subarray(arr):
    maxi = float("-inf")
    total = 0
    n = len(arr)
    for i in range(n):
        total += arr[i]
        # Update maximum if current running sum is larger
        if total > maxi:
            maxi = total
        # Reset running sum if it becomes negative (start fresh from next element)
        elif total < 0:
            total = 0
    return maxi

print(optimal_max_subarray(nums))

# TC - O(N)
# SC - O(1)