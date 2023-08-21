N = int(input())
S = [input() for _ in range(N)]

dp = [[0 for _ in range(2)] for _ in range(N + 1)]

dp[0] = [1, 1]

for i, s in enumerate(S):
    if s == "OR":
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][0] + 2 * dp[i][1]
    else:
        dp[i + 1][0] = 2 * dp[i][0] + dp[i][1]
        dp[i + 1][1] = dp[i][1]

print(dp[N][1])

