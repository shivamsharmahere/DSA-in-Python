nums = [4,6,3,5,9,8,7,1,3,0,2,5,9]

# Quick Sort - Divide and Conquer, In-place sorting algorithm
# Notes:
# - This implementation uses HOARE'S PARTITION SCHEME (pivot = first element)
# - Partition returns the correct position of the pivot after placing it
# - Pivot selection strategies:
#   1. First element (this implementation) - worst for sorted/reverse-sorted arrays
#   2. Last element (Lomuto partition) - also bad for sorted arrays
#   3. Random pivot - avoids worst case in practice
#   4. Median-of-three - chooses median of first, middle, last
# - Quick Sort is NOT a stable sort (equal elements may not preserve original order)
# - Worst case: O(n^2) when array is already sorted and pivot is always first/last
# - Best/Average case: O(n log n)
# - Space: O(log n) average for recursion stack, O(n) worst case

def partition(nums, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(nums)-1

    pivot = nums[low]
    i = low 
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low +1:
            j -= 1
        
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[j], nums[low] = nums[low], nums[j]
    return j

print(partition(nums))

def quick_sort(nums, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(nums)-1

    if low < high:
        p_index = partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)

    return nums

print(quick_sort(nums))

# TC: O(n log n) average, O(n^2) worst case
#     (when pivot is consistently smallest/largest element or array has all same elements)
# SC: O(log n) average, O(n) worst case (due to recursion stack depth)

