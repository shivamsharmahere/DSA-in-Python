# FIBONACCI USING RECURSION
# ========================
# Classic example: each number = sum of two preceding numbers

def fibonnaci(N):
    # Base cases: F(0)=0, F(1)=1
    if N == 0 or N == 1:
        return N
    return fibonnaci(N-1) + fibonnaci(N-2)  # Sum of previous two

print(fibonnaci(0))
# For N=5: f(5) = f(4) + f(3) = (f(3)+f(2)) + (f(2)+f(1)) = ...

# VISUAL CALL TREE for f(5):
#                    f(5)
#                   /    \
#                 f(4)   f(3)
#                /  \    /  \
#              f(3) f(2) f(2) f(1)
#             / \   / \   / \
#           f(2)f(1)f(1)f(0)...
#          / \
#        f(1)f(0)
#
# Notice: f(3), f(2), f(1) are calculated MULTIPLE times! This is inefficient.

# COMPLEXITY ANALYSIS
# Time: O(2^n) - EXPONENTIAL! Each call branches into 2 calls
#   - Number of nodes in binary tree = 2^0 + 2^1 + ... + 2^(n-1) ≈ 2^n
#   - Tree depth = n, but total nodes = exponential
# Space: O(2^n) - Call stack can go to depth n at most
#   - Actually O(n) for stack depth, but O(2^n) for total function calls

# WARNING: This is INEFFICIENT for large N! 
# Use Memoization or Iterative approach for better performance:
# - Memoized: O(n) time, O(n) space
# - Iterative: O(n) time, O(1) space

# The recursive version is mainly for understanding the mathematical definition,
# NOT for practical use with large inputs.