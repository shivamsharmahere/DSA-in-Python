# PALINDROME CHECK USING RECURSION
# ===============================
# Compare characters from both ends moving toward center

s = "Nitin"

def is_palindrome(s, l=0, r=None):
    s = s.strip().lower()  # Clean up: remove spaces, make lowercase
    
    if r is None:          # First call: set r to last index
        r = len(s) - 1
    
    if l >= r:           # Base case 1: pointers crossed/middle reached
        return True        # All pairs matched → palindrome!
    
    if s[l] != s[r]:     # Base case 2: mismatch found
        return False       # Characters don't match → not palindrome
    
    return is_palindrome(s, l+1, r-1)  # Check next pair inward

print(is_palindrome(s))
# For "Nitin": 'n'=='n' ✓, 'i'=='i' ✓, then l>=r → True

# HOW IT WORKS:
# s="nitin", l=0, r=5 → s[0]='n' == s[5]='n' ✓ → recurse
# s="nitin", l=1, r=4 → s[1]='i' == s[4]='i' ✓ → recurse  
# s="nitin", l=2, r=3 → s[2]='t' == s[3]='t' ✓ → recurse
# s="nitin", l=3, r=2 → l>=r → return True

# COMPLEXITY ANALYSIS
# Time: O(n/2) ~ O(n) - We check n/2 character pairs
# Space: O(n/2) ~ O(n) - Stack depth is n/2 (pointers meet at middle)
#   - Much better than O(n) when comparing to single-pointer recursion

# PATTERN: When you see two pointers meeting, stack depth halves!
# Classic use case: palindrome, two-sum variations, reverse operations



