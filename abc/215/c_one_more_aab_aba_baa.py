# python3

import collections
import itertools
import math

s, k = map(str, input().split())
b = 1

A = list(itertools.permutations(s))
sort_a = sorted(A)

c = dict(collections.Counter(s))
for v in c.values():
    b *= math.factorial(v)

print("".join(sort_a[b * int(k) - 1]))
