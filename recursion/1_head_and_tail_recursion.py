# HEAD vs TAIL RECURSION
# =======================
# Two ways to structure recursion based on WHEN you do the work (print/processing).

# HEAD RECURSION: "Work after the call"
# - First: recurse to the base case (go deep)
# - Then: do the work on the way back up (pop from stack)
# - Think: "Call first, work later"

def head_recursion(n):
    if n == 0:          # Base case: stop when we reach 0
        return
    head_recursion(n-1) # 1. FIRST: Go deep (print happens AFTER this returns)
    print("Shivam")     # 2. THEN: Print on the way back up

print("Head Recursion:")
head_recursion(5)
# Output: Prints 5 times "Shivam" but in REVERSE order of calls
# Call stack builds: head(5) -> head(4) -> ... -> head(0) -> returns
# Then unwinding: print happens -> head(4) -> print -> ... -> head(5) -> print

# TAIL RECURSION: "Work before the call"
# - First: do the work immediately
# - Then: make the recursive call at the END
# - Think: "Work first, call next"

def tail_recursion(n):
    if n == 0:
        return
    print("Shivam")     # 1. FIRST: Print immediately
    tail_recursion(n-1) # 2. THEN: Make the recursive call at the END

print("Tail Recursion:")
tail_recursion(5)
# Output: Prints 5 times "Shivam" in SAME order as calls

# COMPLEXITY ANALYSIS
# Time Complexity: O(n) - We make n recursive calls (n, n-1, ..., 1, 0)
# Space Complexity: O(n) - Call stack grows to depth n before returning
#   - Each call waits in stack until its children return
#   - Memory used: n function call frames