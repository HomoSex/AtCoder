import math
import collections as cl
from collections import deque

S = input()

ans = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        ans += 1

print(ans)
