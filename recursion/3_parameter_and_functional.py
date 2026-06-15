# PARAMETER vs FUNCTIONAL RECURSION
# ==============================
# Two styles to accumulate results: pass result as parameter OR return and add up

# Q1: Sum using PARAMETER recursion (also called "state passing")
# Logic: Pass the running sum as a parameter, build it up
def result_sum(sum, i, N):
    # Parameters: sum (running total), i (current number), N (target limit)
    if i > N:       # Base case: when current exceeds target
        print(sum)  # Print final result
        return
    result_sum(sum+i, i+1, N)  # Add current to sum, move to next number

result_sum(0, 1, 5)
# Output: 15 (1+2+3+4+5)
# Call flow: sum=0,i=1 -> sum=1,i=2 -> sum=3,i=3 -> ... -> sum=10,i=5 -> sum=15,i=6 [prints and returns]

# Q2: Sum using FUNCTIONAL recursion (return values accumulate)
# Logic: Each call returns its part, combine on the way back
def result_sum(N):
    if N == 0:    # Base case: nothing to add
        return 0
    return N + result_sum(N-1)  # Add current N to sum of remaining numbers

print(result_sum(5))
# Output: 15
# Think: 5 + (4 + (3 + (2 + (1 + (0)))) = 5+4+3+2+1+0 = 15

# COMPLEXITY: Both are O(n) time, O(n) space
# - Time: n calls, each does O(1) work
# - Space: Stack depth grows to n frames

# Q3: Factorial using functional recursion
# Logic: N! = N × (N-1) × (N-2) × ... × 1
def func(N):
    if N == 0:    # Base case: 0! = 1
        return 1
    return N * func(N-1)  # Multiply N with factorial of N-1

print(func(5))
# Output: 120 (5! = 5×4×3×2×1)
# Call flow: 5 * (4 * (3 * (2 * (1 * (1))))) = 5*4*3*2*1*1 = 120

# KEY DIFFERENCE:
# Parameter style: Uses extra parameters to carry state through calls
# Functional style: Each call returns a value, building result on unwind
# Both achieve same goal - choose based on problem needs