# -*- coding: utf-8 -*-
# python3

a, b, c = map(int, input().split())

ans = a + b
if b + c > ans:
    ans = b + c
if c + a > ans:
    ans = c + a

print(ans)
