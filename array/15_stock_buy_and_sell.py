# Q1. Given an array having the price of a stock on different days, find the maximum profit
# Constraint: Can only sell after buying (must buy before sell, not same day)
# Approach: Find the pair (buy_day, sell_day) where sell_day > buy_day and arr[sell] - arr[buy] is maximum

prices = [7, 2, 1, 5, 6, 4, 8]

# Method 1: Brute Force
# Check all possible pairs of buy and sell days
def brute_max_profit(arr):
    n = len(arr)
    max_profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                profit = arr[j] - arr[i]
                max_profit = max(profit, max_profit)

    # Return 0 if no profitable transaction possible
    if max_profit < 0:
        return 0
    else:
        return max_profit

print(brute_max_profit(prices))

# TC - O(N(N+1)/2) ~ O(N2)
# SC - O(1)
 
print("************** METHOD 2 **************")

# Method 2: Find min price first, then max profit after min
# Note: This has a flaw - if the minimum comes near the end, max_price will be 0
def max_profit(arr):
    n = len(arr)
    min_price = min(arr)
    min_idx = prices.index(min_price)
    # Look for maximum price only after the minimum price day
    max_price = 0
    for i in range(min_idx + 1, n):
        max_price = max(max_price, arr[i])

    result = max_price - min_price
    return max(result, 0)  # Return 0 if no profit possible

print(max_profit(prices))

# TC - O(N)
# SC - O(1)

print("************** METHOD 3 **************")

# Method 3: Optimal Single Pass (Recommended)
# Track the minimum price seen so far and calculate potential profit at each day
def max_profit_2(arr):
    min_price = float("inf")  # Initialize to infinity to track the lowest price
    max_profit = 0
    n = len(arr)
    for i in range(n):
        # Update minimum price if current price is lower
        min_price = min(min_price, arr[i])
        # Update max profit if selling at current price gives better profit
        max_profit = max(max_profit, arr[i] - min_price)
    return max_profit

print(max_profit_2(prices))

# TC - O(N)
# SC - O(1)