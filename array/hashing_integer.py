"""
hashing_integer.py

Demonstrate counting frequencies of integers with different memory/time
trade-offs. The examples below assume `m` is the list to be counted and `n`
is the list of query values whose frequencies we want to report.

Use cases and constraints:
- If values in `m` lie in a small fixed range (e.g. 1..10), a fixed-size
  array of counters is the most space-efficient.
- If `n` may contain arbitrary values outside that range, store results in a
  dictionary when necessary.
"""

m = [5, 5, 8, 7, 5, 4, 4, 5, 5, 9, 1, 2, 2, 8]
n = [16, 554, 23, 0, 0, 5, 5, 8, 7, 9, 8, 23, 0, 0]

# --- Method 1: Brute force (simple, but slow) ---------------------------------
# For each query in `n` scan the whole `m` list and count matches.
# Time: O(len(m) * len(n)). Space: O(u) where u is number of unique queries
# (we store one dict entry per query).
brute_counts = {}
for q in n:
    count = 0
    for x in m:
        if q == x:
            count += 1
    brute_counts[q] = count

print("Brute force counts:", brute_counts)

# --- Method 2: Hash map (general, fast lookups) -------------------------------
# Build a frequency map for elements in m (dictionary). Then answer queries
# by looking up the map (O(1) per query).
# Time: O(len(m) + len(n)). Space: O(k) where k is number of unique elements in m.
freq_map = {}
for x in m:
    freq_map[x] = freq_map.get(x, 0) + 1

print("Frequency map of m:", freq_map)

query_results = {}
for q in n:
    # freq_map.get(q, 0) returns 0 for values not present in m
    query_results[q] = freq_map.get(q, 0)

print("Query results using hash map:", query_results)

# --- Method 3: Fixed-size array (best when value range is small) ------------
# If we know in advance that values in `m` lie in a small integer range,
# e.g. 1..10 inclusive, we can use an array of length (max_value+1) for O(1)
# counters. This uses constant extra space independent of len(m).
# Time: O(len(m) + len(n)). Space: O(1) (fixed-size array counters).

MIN_VAL = 1
MAX_VAL = 10
RANGE_SIZE = MAX_VAL - MIN_VAL + 1

fixed_counts = [0] * (RANGE_SIZE)
for x in m:
    if MIN_VAL <= x <= MAX_VAL:
        fixed_counts[x - MIN_VAL] += 1

print("Fixed-range counts (indices 1..10):", fixed_counts)

fixed_query_results = {}
for q in n:
    if MIN_VAL <= q <= MAX_VAL:
        fixed_query_results[q] = fixed_counts[q - MIN_VAL]
    else:
        # queries outside the known range must be reported separately
        fixed_query_results[q] = 0

print("Query results using fixed-range array:", fixed_query_results)

# Summary of trade-offs:
# - Hash map: time O(m+n), space O(k) (k = unique values in m). Works for
#   arbitrary integer values.
# - Fixed array: time O(m+n), space O(1) if range is constant and small.
# - Brute force: easy to write, but time O(m*n) and not suitable for large inputs.
