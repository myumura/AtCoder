# -*- coding: utf-8 -*-
# python
import collections

N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
bc_list = []

for i in c_list:
    bc_list.append(b_list[i - 1])

bc_c = collections.Counter(bc_list)
a_c = collections.Counter(a_list)
dup = list(set(a_list) & set(bc_list))

ans = 0
if len(dup) != 0:
    for i in dup:
        ans += bc_c[i] * a_c[i]

print(ans)
