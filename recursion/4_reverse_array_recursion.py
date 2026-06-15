# REVERSE ARRAY USING RECURSION
# ============================
# Two-pointer technique: swap elements from left and right moving toward center

m = [8,4,5,6,2,1,7,8,9,5,1,3,6]

def reverse_elements(array, l, r):
    # l = left index pointer, r = right index pointer
    if l >= r:      # Base case: pointers crossed or met (middle reached)
        print(array)
        return
    array[l], array[r] = array[r], array[l]  # Swap elements at l and r
    reverse_elements(array, l+1, r-1)          # Move pointers inward

reverse_elements(m, 1, 3)
# Only reverses elements from index 1 to 3: swaps m[1]↔m[3]
# To reverse whole array: call reverse_elements(m, 0, len(m)-1)

# How it works:
# Initial: l=1, r=3 → swap m[1] and m[3] → [8,6,5,4,2,...]
# Next: l=2, r=2 → condition l>=r met → stop
# Result: subarray [1:3] reversed

# COMPLEXITY ANALYSIS
# Time: O(n/2) ~ O(n) - We process ~n/2 pairs of elements
#   - Each swap takes O(1) time
#   - Total swaps = (r-l+1)/2 ≈ n/2
# Space: O(n/2) ~ O(n) - Stack depth goes to n/2 (not full n!)
#   - Because l and r meet in the middle, not at the end
#   - Maximum depth = number of swaps = (r-l+1)/2

# KEY: Two pointers meet at center, so we only go half the depth
# This is more space-efficient than single-pointer recursion