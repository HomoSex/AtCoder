N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

for s in S:
    if s in T:
        print("Yes")
    else:
        print("No")
