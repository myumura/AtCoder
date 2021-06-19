# -*- coding: utf-8 -*-
# python3
import collections

n = int(input())
A = list(map(int, input().split()))
ans = n * (n - 1) / 2

new_A = sorted(A)
c = collections.Counter(new_A)

for i in c.values():
    ans -= i * (i - 1) / 2

print(int(ans))
