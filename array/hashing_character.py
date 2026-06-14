"""
hashing_character.py

Count occurrences of lowercase letters using a fixed-size array of 26 counters.

Why this works:
- Lowercase ASCII letters 'a'..'z' map to code points 97..122.
- Subtracting `ord('a')` (97) yields indices 0..25 which fit into a 26-element
  list. This gives O(1) space for the counters and O(len(m) + len(n)) time.

This file also demonstrates safe handling of characters outside 'a'..'z'.
"""

m = "wsredtfdfsgngjhnbzugyiuhjohjgcfxd"
n = ["a", "j", "d", "g", "Z"]  # sample queries (includes an uppercase to show handling)

# Prepare counters for 'a'..'z' (indices 0..25)
BASE = ord('a')
ALPHABET_SIZE = 26
char_counts = [0] * ALPHABET_SIZE

for ch in m:
    # normalize and make sure we only count lowercase letters
    if 'a' <= ch <= 'z':
        idx = ord(ch) - BASE
        char_counts[idx] += 1

print("Character counts (a..z):", char_counts)

# Answer queries from `n` safely
result = {}
for ch in n:
    if isinstance(ch, str) and len(ch) == 1 and 'a' <= ch <= 'z':
        result[ch] = char_counts[ord(ch) - BASE]
    else:
        # Out-of-range characters (uppercase, digits, symbols) are treated as 0
        result[ch] = 0

print("Count of characters in query list:", result)

# Complexity: O(len(m) + len(n)) time, O(1) extra space (26 counters)

