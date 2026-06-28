# Merge two sorted arrays into one sorted array without duplicates
# Notes:
# - Both input arrays must be sorted individually for this two-pointer merge to work.
# - The result is also sorted and contains no duplicates from either array.
# - Using `<=` in comparison (arr1[i] <= arr2[j]) prioritizes arr1 elements when equal,
#   which maintains stability for elements that appear in both arrays.
# - Checking `result[-1] != arr` ensures we don't add duplicates from the same array
#   (since inputs are sorted, duplicates would be adjacent) AND from the other array.
# - Time complexity: O(m + n) - each element from both arrays is visited exactly once.
# - Space complexity: O(m + n) for the result array (required since we return a new merged array).
#   If duplicates didn't need to be removed and we could modify inputs, we could do it in O(1) extra.

nums1 = [1,2,3,4,5,6]
nums2 = [3,4,5,6,7,8]

def merge(arr1, arr2):
    result = []
    m = len(arr1)
    n = len(arr2)
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] <=  arr2[j]:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        else :
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
    
    while i < m :
        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    
    while j < n:
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result

print(merge(nums1,nums2))
        
# In this we are actually prioritising the arr1 that we will only insert the arr1 elements after the comparison and then finally will insert the values of arr2 with 2nd priority and that is why we dont need to check the whole RESULT array and can just validate by using last element.
# TC - O(n+m)
# SC - If result is included in calcluation then O(n+m) or else O(1)