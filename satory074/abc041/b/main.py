A, B, C = map(int, input().split())
MOD = 10 ** 9 + 7

print((A * B % MOD) * C % MOD)
