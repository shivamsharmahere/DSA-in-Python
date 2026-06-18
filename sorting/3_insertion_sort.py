# INSERTION SORT
# ==============
# Strategy: Build sorted array one element at a time, like arranging playing cards

nums = [6,9,8,4,55,9,4,6,1,2,6,8,7,1,2,0]

def insertion_sort(nums):
    n = len(nums)
    # Start from index 1 (index 0 is trivially sorted)
    for i in range(1, n):
        key = nums[i]   # Element to insert into sorted portion
        j = i-1         # Start comparing with element before
        
        # Shift elements right until we find correct position for key
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]  # Move larger element one position right
            j -= 1
        
        nums[j+1] = key  # Insert key in its correct position

    return nums

print(insertion_sort(nums))
# Output: [0, 1, 1, 2, 2, 4, 4, 6, 6, 6, 7, 8, 8, 9, 9, 55]

# STEP BY STEP:
# i=1: key=9, compare with 6, 9 goes after 6 → [6,9,...]
# i=2: key=8, shift 9 right, insert 8 → [6,8,9,...]
# i=3: key=4, shift 9,8,6 right, insert 4 → [...,4,6,8,9]

# COMPLEXITY ANALYSIS:
# Time: O(n²) worst case - When array is reverse sorted, inner loop runs i times for each i
#   - Best case: O(n) when already sorted (inner loop never executes)
#   - Average: O(n²) for random data
# Space: O(1) - In-place sorting, only uses temp variables

# BEST FOR: Small arrays, nearly sorted data, or online sorting (can insert new elements easily)
# WHY: Very little overhead, adaptive - faster when data is partially sorted

