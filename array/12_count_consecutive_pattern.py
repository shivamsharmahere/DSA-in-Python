# Q1. In an array count the no of consecutive 1 repeated
# Notes:
# - This is a "maximum consecutive occurrences" problem. Common variations include:
#   max consecutive 1s, max consecutive 0s, max consecutive same elements, etc.
# - Key insight: Use a running count that resets when the pattern breaks (0 encountered).
#   Track the maximum count seen so far.
# - The final `max(max_count, count)` after the loop is crucial because the array might
#   end with the maximum streak (e.g., [1,1,1,0,1,1] - if we only update max_count on 0,
#   the last streak of 2 would be missed without the final max check).
# - Edge cases: All 1s (max = n), all 0s (max = 0), empty array (max = 0), single element.
# - Can be generalized by replacing `arr[i] == 1` with any target value.
# - If you also need the position/start index of the max streak, track that alongside count.

nums = [1,1,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1]

def pattern(arr):
    n = len(arr)
    i = 0
    count= 0
    max_count = 0   
    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            max_count = max(max_count,count)
            count = 0
    return max(max_count,count)
            
print(pattern(nums))

# TC - O(n)
# SC - O(1)

