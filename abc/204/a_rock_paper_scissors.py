# -*- coding: utf-8 -*-
# pypy

n_list = []
x, y = map(int, input().split())
n_list.append(x)
n_list.append(y)

if x == y:
    answer = x
else:
    if 0 not in n_list:
        answer = 0
    elif 1 not in n_list:
        answer = 1
    else:
        answer = 2
    
print(answer)
