# time:  O(n*m), or O(2^(n+m)) without memoization,  where n is amount and m is number of coins
# space: O(n*m)
def coin_change(amount, coins):
    return change(amount, coins, 0, {})

def change(amount, coins, index, memo):
    if amount == 0: return 1
    if amount < 0 or index == len(coins): return 0
    if (amount, index) in memo:
        return memo[(amount, index)]

    count = change(amount - coins[index], coins, index, memo)
    count += change(amount, coins, index + 1, memo)
    memo[(amount, index)] = count
    return count

# def coin_change1(amount, coins):
#     return change1(amount, coins, 0, {})

# def change1(amount, coins, index, memo):
#     if amount == 0: return 1
#     if (amount, index) in memo:
#         return memo[(amount, index)]
#     count = 0
#     for i in range(index, len(coins)):
#         if amount - coins[i] >= 0:
#             count += change1(amount - coins[i], coins, i, memo)
#     memo[(amount, index)] = count
#     return count


# time:  O(n*m)
# space: O(n*m)
def coin_change2(amount, coins):
    dp = [[0] * len(coins) for _ in range(amount + 1)]
    for j in range(len(coins)):
        dp[0][j] = 1
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                dp[i][j] += dp[i - coins[j]][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[amount][len(coins) - 1]

def coin_change3(amount, coins):
    dp = [[0] * (amount + 1) for _ in range(len(coins))]
    for i in range(len(coins)):
        dp[i][0] = 1
    for i in range(len(coins)):
        for j in range(1, amount + 1):
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - coins[i] >= 0:
                dp[i][j] += dp[i][j - coins[i]]
    return dp[len(coins) - 1][amount]

# time:  O(n*m)
# space: O(n)
def coin_change4(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(1, amount + 1):
            if j - coins[i] >= 0:
                dp[j] += dp[j - coins[i]]
    return dp[amount]


cases = [
    (5, [1, 2, 5]),
    (15, [1, 5, 10, 15]),
]
for amount, coins in cases:
    print(amount, coins, coin_change(amount, coins), 
        # coin_change1(amount, coins),
        coin_change2(amount, coins), 
        coin_change3(amount, coins),
        coin_change4(amount, coins))