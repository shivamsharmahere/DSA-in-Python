# Check whether an array is sorted or not
# Notes:
# - Only need to check adjacent pairs (arr[i] vs arr[i+1]) because if all adjacent
#   pairs are in order, the entire sequence is in order.
# - For ascending: each element must be <= next element.
# - For descending: each element must be >= next element.
# - Empty array or single element array is trivially sorted (no adjacent pairs to violate).
# - If you want strictly sorted (no equal adjacent elements), use < or > instead of <= or >=.

nums = [1,6,65,1,6,-98,5,12,12,65,59,89,5,4]
nums2 = [1,2,3,4,5,6,7,8,9]
nums3 = [9,8,7,6,5,4,3,2,1]

def is_sorted_ascending(arr):
    n = len(arr)
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def is_sorted_des(arr):
    n = len(arr)
    for i in range(0,n-1):
        if arr[i] < arr[i+1]:
            return False
    return True
        
print(is_sorted_ascending(nums))        
print(is_sorted_ascending(nums2))
print(is_sorted_des(nums3))

# TC - O(N)
# SC - O(1)