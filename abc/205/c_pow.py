# -*- coding: utf-8 -*-
# pypy

a, b, c = map(int, input().split())
abs_a = abs(a)
abs_b = abs(b)

if c % 2 == 0:
    if abs_a > abs_b:
        print(">")
    elif abs_a < abs_b:
        print("<")
    else:
        print("=")
else:
    if a * b > 0:
        if abs_a > abs_b:
            print(">")
        elif abs_a < abs_b:
            print("<")
        else:
            print("=")
    elif a * b <= 0:
        if a > b:
            print(">")
        elif a < b:
            print("<")
        else:
            print("=")
