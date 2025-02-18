def coins_combinations(target, coins):
    # Create a dp array of size target + 1, where dp[i] will be the number of ways to make amount i
    dp = [0] * (target + 1)
    
    # There's one way to make amount 0: using no coins
    dp[0] = 1
    
    # Loop through each coin
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]
    
    return dp[target]

# Test cases
print(coins_combinations(4, [1, 2]))  # 3
print(coins_combinations(10, [5, 2, 3]))  # 4
print(coins_combinations(11, [5, 7]))  # 0
