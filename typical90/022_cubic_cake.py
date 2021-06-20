# -*- coding: utf-8 -*-
# python3

A, B, C = map(int, input().split())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


d = gcd(A, B)
quotient = gcd(C, d)
answer = (A // quotient - 1) + (B // quotient - 1) + (C // quotient - 1)
print(answer)
