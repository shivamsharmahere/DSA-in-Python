# SELECTION SORT
# ==============
# Strategy: Find the minimum element and place it at the beginning repeatedly

nums = [1,5,4,8,5,9,7,1,5,9,0]

def selection_sort(arr, l=0, r=None):
    if r is None:
        r = len(arr)
    
    # The algorithm maintains two subarrays:
    # 1) Sorted part (left side, indices 0 to i-1)
    # 2) Unsorted part (right side, indices i to r-1)
    
    for i in range(l, r):
        min_idx = i              # Assume current position has minimum
        # Find the actual minimum in unsorted portion
        for j in range(i+1, r):
            if arr[j] < arr[min_idx]:
                min_idx = j    # Update minimum index
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap to place min at position i
    
    return arr

print(selection_sort(nums))
# Output: [0, 1, 1, 4, 5, 5, 7, 8, 9, 9]

# STEP BY STEP:
# Pass 1: Find min=0 at index 10, swap with arr[0] → [0,...]
# Pass 2: Find min=1 at index 6, swap with arr[1] → [0,1,...]
# Continue until sorted...

# COMPLEXITY ANALYSIS:
# Time: O(n²) - Two nested loops: (n-1) + (n-2) + ... + 1 = n(n-1)/2 comparisons
#   - Always the same: O(n²) regardless of input order
# Space: O(1) - Only uses a few temporary variables for swapping
#   - In-place sorting (no extra arrays)

# BEST FOR: Small arrays, or when you need minimum swaps (at most n-1 swaps)

