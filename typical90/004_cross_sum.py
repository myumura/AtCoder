# -*- coding: utf-8 -*-
# pypy

line_list = []
sum_list = []
h, w = map(int, input().split())
line_sum = [0] * h
column_sum = [0] * w

for i in range(h):
    line = list(map(int, input().split()))
    line_list.append(line)

for i in range(h):
    for j in range(w):
        line_sum[i] += line_list[i][j]
        column_sum[j] += line_list[i][j]

for i in range(h):
    for j in range(w):
        a_sum = line_sum[i] + column_sum[j] - line_list[i][j]
        sum_list.append(a_sum)

print(' '.join(map(str, sum_list[:w])))
for i in range(1, h):
    print(' '.join(map(str, sum_list[(i * w):(i * w + w)])))
