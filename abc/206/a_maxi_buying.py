# -*- coding: utf-8 -*-
# python3

n = int(input())
tax = 1.08
val = int(n * tax)

if val < 206:
    print('Yay!')
elif val == 206:
    print('so-so')
else:
    print(':(')
