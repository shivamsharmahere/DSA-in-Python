# RECURSION WITH PARAMETERS PATTERN
# ================================
# Using parameters to track state: 'i' (current) and 'N' (limit/target)

# Q1: Print x, N times (Tail Recursion style)
# Logic: Print first, then reduce N by 1
def func(x,N):
    if N == 0:      # Base case: stop when N reaches 0
        return
    print(x)        # Do work first
    func(x, N-1)    # Then recurse with reduced N

func("Shivam", 5)
# Output: "Shivam" printed 5 times (5,4,3,2,1)

# Q2: Print 1 to N (Tail Recursion)
# Logic: Print increasing i, recurse until i exceeds N
def func(i,N):
    if i > N:       # Base case: stop when i crosses N
        return
    print(i)        # Do work first (prints current i)
    func(i+1, N)    # Then increment i

func(1, 5)
# Output: 1,2,3,4,5 (natural order)

# Q3: Print N to 1 (Head Recursion - also called Backtracking)
# Logic: Recurse ALL the way first, then print on the way back
def func(i,N):
    if i > N:
        return
    func(i+1, N)    # 1. FIRST: Go all the way to the end
    print(i)        # 2. THEN: Print while unwinding (reverse order)

func(1,4)
# Output: 4,3,2,1 (reverse order)
# Call stack: func(1,4) -> func(2,4) -> func(3,4) -> func(4,4) -> func(5,4) [returns]
# Unwinding: print(4) -> print(3) -> print(2) -> print(1)

# Q4: Print N to 1 using Head Recursion (simpler version)
# Logic: Just use N as parameter, no need for i
def func(N):
    if N == 0:      # Base case
        return
    print(N)        # Print before recursing
    func(N-1)       # Then go to N-1

func(3)
# Output: 3,2,1 (same as Q3 but simpler)

# Q5: Print 1 to N using Head Recursion (Backtracking)
# Logic: Recurse to the bottom first, then print on the way UP
print("======== Q5 ========")
def func(N):
    if N == 0:
        return
    func(N-1)       # 1. FIRST: Recurse all the way to 1
    print(N)        # 2. THEN: Print while coming back up

func(3)
# Output: 1,2,3 (reverse of what you might expect!)
# Call stack goes: func(3) -> func(2) -> func(1) -> func(0) [returns]
# Unwinding prints: 1, then 2, then 3

# KEY INSIGHT: In Head Recursion, operations happen AFTER the recursive call returns
# - Call goes deep first, then work happens on the way back
# - Great for problems where you need to process after reaching the end