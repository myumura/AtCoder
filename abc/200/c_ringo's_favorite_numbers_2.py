# -*- coding: utf-8 -*-
# python3

n = int(input())
a = list(map(int, input().split()))
bucket = [0] * 200
ans = 0

for i in a:
    bucket[i % 200] += 1

for i in bucket:
    ans += i * (i - 1) // 2

print(ans)
