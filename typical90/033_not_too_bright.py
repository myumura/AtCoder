# -*- coding: utf-8 -*-
# python3

h, w = map(int, input().split())

h_light = h // 2 if h % 2 == 0 else (h - 1) // 2 + 1
w_light = w // 2 if w % 2 == 0 else (w - 1) // 2 + 1

if h == 1 or w == 1:
    answer = h * w
else:
    answer = h_light * w_light

print(answer)
