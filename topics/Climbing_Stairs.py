# You can climb 1 or 2 steps at a time. How many ways to reach step n?
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]   # same recurrence as fibonacci!
    return dp[n]

print(climb_stairs(5))   # 8
