# -*- coding: utf-8 -*-
# pypy

n = int(input())
a_list = list(map(int, input().split()))
num_list = [i for i in range(1, n + 1)]

a_sort_list = sorted(a_list)
print("Yes" if a_sort_list == num_list else "No")
