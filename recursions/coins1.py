"""Return the fewest number of coins that you need to make up an amount"""

# time:  O(n*m), or O(2^(n+m)) without memoization,  where n is amount and m is number of coins
# space: O(n*m)
def coin_change(amount, coins):
    count = change(amount, coins, 0, {})
    return count if count < float('inf') else -1

def change(amount, coins, index, memo):
    if amount == 0: return 0
    if amount < 0 or index == len(coins): return float('inf')
    if (amount, index) in memo:
        return memo[(amount, index)]

    count1 = 1 + change(amount - coins[index], coins, index, memo)
    count2 = change(amount, coins, index + 1, memo)
    count = min(count1, count2)
    memo[(amount, index)] = count
    return count

# time:  O(n*m)
# space: O(n*m)
def coin_change2(amount, coins):
    dp = [[float('inf')] * len(coins) for _ in range(amount + 1)]
    for j in range(len(coins)):
        dp[0][j] = 0
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                dp[i][j] = 1 + dp[i - coins[j]][j]
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1])
    count = dp[amount][len(coins) - 1]
    return count if count < float('inf') else -1

def coin_change3(amount, coins):
    dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]
    for i in range(len(coins)):
        dp[i][0] = 0
    for i in range(len(coins)):
        for j in range(amount + 1):
            if j - coins[i] >= 0:
                dp[i][j] = 1 + dp[i][j - coins[i]]
            if i - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
    count = dp[len(coins) - 1][amount]
    return count if count < float('inf') else -1

# time:  O(n*m)
# space: O(n)
def coin_change4(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(len(coins)):
        for j in range(amount + 1):
            if j - coins[i] >= 0:
                dp[j] = min(dp[j], 1 + dp[j - coins[i]])
    return dp[amount] if dp[amount] < float('inf') else -1

cases = [
    (5, [1, 2, 5]),
    (15, [1, 5, 10]),
]
for amount, coins in cases:
    print(amount, coins, coin_change(amount, coins), 
        coin_change2(amount, coins),
        coin_change3(amount, coins),
        coin_change4(amount, coins))