# Linear search : search for an element in an array and if not found return -1
# Notes:
# - Simplest search algorithm - checks each element sequentially until found or end reached.
# - Works on both sorted and unsorted arrays (unlike binary search which requires sorted data).
# - Time complexity is always O(N) because in worst case we check every element.
# - arr.index(e) inside the loop is inefficient because it searches from the beginning again.
#   Better to use enumerate and return the index directly.
# - If you need the first occurrence, linear search is correct. If you need all occurrences,
#   collect them in a list instead of returning immediately.
# - Best for small arrays or when array is unsorted. For large sorted arrays, use binary search (O(log N)).

nums = [1,321,65,165,1,651,32,1,31,5,5,9,8,9,2,3,5,8]

def linear_search(arr):
    search = int(input("Enter the element to search: "))
    for e in arr:
        if search == e:
            return arr.index(e)
    return -1   
        
print(linear_search(nums))