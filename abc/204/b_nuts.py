# -*- coding: utf-8 -*-
# python3

n_sum = 0
n = int(input())
tree_list = list(map(int, input().split()))

for i in tree_list:
    if i > 10:
        n_sum += i - 10

print(n_sum)
