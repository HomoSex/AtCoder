import collections as cl
import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

a, b = map(int, input().split())

if 0 <= b - (a * 2) <= 1:
    print("Yes")
else:
    print("No")
