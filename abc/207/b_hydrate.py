# -*- coding: utf-8 -*-

a, b, c, d = map(int, input().split())
blue = a
red = 0
ans = 0

if b >= c * d:
    ans = -1
else:
    while red * d < blue:
        ans += 1
        blue += b
        red += c

print(ans)
