"""
frequency_storing.py

Demonstrate simple ways to count frequencies of items in a list.

Concepts covered:
- Counting with a dictionary (hash map) — O(n) time, O(k) extra space where k
  is number of unique items.
- Using `dict.get()` to write concise counting logic.

Examples show counting integers; the same approach applies to characters or
other hashable Python objects.
"""

num = [1, 2, 3, 4, 5, 6, 8, 4, 1, 2, 5, 7, 8, 8, 4, 1, 5, 8, 7, 4, 5, 5]

print("Input list:", num)

# Method 1: explicit membership check
counts = {}
for x in num:
    if x not in counts:
        counts[x] = 1
    else:
        counts[x] += 1

print("Frequencies (method 1):", counts)

# Complexity: Time O(n), Space O(k) where k is number of unique elements

# Method 2: idiomatic Python using dict.get for brevity
counts2 = {}
for x in num:
    counts2[x] = counts2.get(x, 0) + 1

print("Frequencies (method 2):", counts2)

# Note: For convenience and readability, Python's `collections.Counter` is
# recommended in production code:
# from collections import Counter
# counts3 = Counter(num)
# print(counts3)


