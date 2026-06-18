# BUBBLE SORT (Adjacent Sort)
# ============================
# Strategy: Compare adjacent elements, swap if out of order - larger elements "bubble up"

nums = [6,4,9,4,6,1,2,6,8,7,1,2,0]

def bubble_sort(nums, j=None):
    j = len(nums)-1 if j is None else j
    
    # j = rightmost boundary of unsorted portion (shrinks each pass)
    for i in range(0, j):
        # Compare each adjacent pair
        if nums[i+1] < nums[i]:
            nums[i], nums[i+1] = nums[i+1], nums[i]  # Swap if wrong order
    
    # After one pass, largest element is at position j
    # Recurse on remaining elements, or return if done
    return bubble_sort(nums, j-1) if j > 1 else nums

print(bubble_sort(nums))
# Output: [0, 1, 1, 2, 2, 4, 4, 6, 6, 6, 7, 8, 9]

# STEP BY STEP:
# Pass 1 (j=12): Bubbles 9 to end → [..., 9]
# Pass 2 (j=11): Bubbles 8 to position 11 → [..., 8, 9]
# Each pass places one more element in correct position

# COMPLEXITY ANALYSIS:
# Time: O(n²) worst case - nested structure with n passes
#   - Best case: O(n) when already sorted (still does n passes but no swaps)
# Space: O(1) - In-place sorting, only constant extra variables

# OPTIMIZED BUBBLE SORT
# =====================
# Add a flag to detect if array becomes sorted early

def optimized_bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False  # Track if any swap happened
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:  # No swaps = already sorted!
            break
    return nums

print(optimized_bubble_sort(nums))

# KEY INSIGHT: The recursive version here is unusual - typically bubble sort is iterative
# Optimization saves time on nearly-sorted arrays (common in real-world scenarios)
