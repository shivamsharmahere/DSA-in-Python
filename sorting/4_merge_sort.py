# MERGE SORT
# ==========
# Strategy: Divide-and-conquer - split, sort each half, then merge back together

def merge_array(left, right):
    # Merge two already-sorted arrays into one sorted array
    result = []
    n, m = len(left), len(right)
    i, j = 0, 0  # Pointers for each array
    
    # Compare and take smaller element from either array
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements (only one of these loops will execute)
    while i < n:
        result.append(left[i])
        i += 1
    
    while j < m:
        result.append(right[j])
        j += 1
    
    return result

def merge_sort(arr):
    # Base case: array of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2           # Split point
    left_half = arr[:mid]          # Left portion
    right_half = arr[mid:]         # Right portion
    
    # Recursively sort each half (divide step)
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge sorted halves back together (conquer step)
    return merge_array(left_half, right_half)

nums = [1,2,3,5,5,1,5,9,2,0,5,1,56]
print(merge_sort(nums))
# Output: [0, 1, 1, 2, 2, 3, 5, 5, 5, 9, 56]

# VISUAL DIVIDE TREE for [3,1,2]:
#        [3,1,2]
#       /        \
#     [3]       [1,2]
#              /      \
#            [1]      [2]
#             \       /
#            [1,2]
#           /     \
#        [1,2,3]   [3,1,2] → merged and sorted

# COMPLEXITY ANALYSIS:
# Time: O(n log n) - Always! 
#   - Why log n: We divide array in half each time (tree height)
#   - Why n: Each level does O(n) work merging (all elements processed)
#   - Total: n * log n (n levels, log n depth)
# Space: O(n) - Uses extra arrays for merging
#   - Not in-place: needs temporary storage for merge step
#   - Can be optimized to O(log n) with careful implementation

# WHY IT'S GREAT:
# - Predictable O(n log n) time (unlike quicksort's worst case)
# - Stable sort (preserves order of equal elements)
# - Great for large datasets, external sorting