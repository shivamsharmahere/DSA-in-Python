# Remove duplicates from sorted array inplace
# Notes:
# - The problem assumes the input array is SORTED. This is critical because it allows
#   the optimal two-pointer solution (Method 2) which runs in O(N) time.
# - Method 1 (freq_map): Has a BUG - freq_map is a global variable that persists state
#   across calls. If you call remove_duplicates() twice, the second call will find all
#   elements already in the map. Also, dict iteration doesn't guarantee sorted order
#   (in Python 3.7+ it preserves insertion order, but elements are inserted in first-occurrence
#   order which happens to be sorted here only because input is sorted). SC is actually O(N)
#   because the map stores up to N unique elements.
# - Method 2 (two-pointer): Optimal for sorted arrays. i tracks the position of the last
#   unique element. j scans ahead. When arr[j] != arr[i], we found a new unique element.
#   The array is modified in-place from index 0 to i+1.

nums = [0,0,1,2,3,3,4,4,4,5,6,7,8,8,9,9,9,15]

#Method 1 : TC - O(N), SC- O(N) (freq_map stores all unique elements)
# WARNING: Global freq_map is a bug - it retains state between function calls.
freq_map = {}
def remove_duplicates(arr):
    for i in range(0,len(arr)):
        if arr[i] not in freq_map:
            freq_map[arr[i]] = 1
    j=0
    for k in freq_map:
        nums[j] = k
        j += 1
    return j

print(remove_duplicates(nums))


# Method 2 OPTIMAL : 

nums2 = [0,0,1,2,3,3,4,4,4,5,6,7,8,8,9,9,9,15]

def duplicates(arr):
    if len(arr) <= 1:
        return len(arr)

    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

print(duplicates(nums2))
