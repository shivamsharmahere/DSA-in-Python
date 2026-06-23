# Rotate Right an array with K place
# Notes:
# - Right rotation by k: last k elements move to the front, remaining shift right.
# - k % n is essential because rotating by n (or multiples of n) brings array back to original.
#   Example: [1,2,3,4,5] rotated by 5 = [1,2,3,4,5] (same), rotated by 7 = rotated by 2.
# - Method 1 (brute force): Each pop() from end is O(1), but insert(0, e) is O(N) because
#   all elements shift. Doing this r times gives O(N * r) time.
# - Method 2 (slicing): Concatenation creates a new list of size N, so SC is O(N).
# - Method 3 (reverse trick): Optimal. Reverse entire array, then reverse first r elements,
#   then reverse remaining n-r elements. Both time and space are O(N) and O(1) respectively.
#   Example: [1,2,3,4,5], k=2
#     Reverse all: [5,4,3,2,1]
#     Reverse first 2: [4,5,3,2,1]
#     Reverse last 3: [4,5,1,2,3] -> Correct right rotation by 2.

# Method 1 : Brute Force

nums = [5,8,5,6,9]

# As we can have k = 28,150 etc. also we we should first get the reminder by % it so that we can get min rotations needed as array will repeat itself at its multiple.

k = 28
n = len(nums)
rotations = k % n
print("Rotations Needed : ",rotations)

for _ in range(0,rotations):
    e = nums.pop()
    nums.insert(0,e)

print("Rotated Array:",nums)

# TC- o(n*r), SC -O(1)


# Method 2: Slicing

nums = [5,8,5,6,9]

nums[:] = nums[n-rotations:] + nums[:n-rotations]
print("Rotated Array via SLICING:", nums)

# TC - O(N), SC - O(N) (creates a new combined list)


# Method 3 : 

nums = [5,8,5,6,9]

def reverse(arr,left,right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

reverse(nums,n-rotations,n-1)
reverse(nums,0,n-rotations-1)
print("Array after Rotation:")
print(reverse(nums,0,n-1))