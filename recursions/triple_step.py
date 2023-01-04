# time:  O(n)
# space: O(n)
def triple_step(n):
    return hop(n, {})

def hop(n, memo):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2

    if n in memo: return memo[n]
    count = 0
    # hop 1-step
    count += hop(n - 1, memo)
    # hop 2-step
    count += hop(n - 2, memo)
    # hop 3-step
    count += hop(n - 3, memo)
    memo[n] = count
    return count

# time:  O(n)
# space: O(n) 
def triple_step2(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

for step in [0,1,2,3,4,5,6,900]:
    print(step, triple_step2(step), triple_step(step))
