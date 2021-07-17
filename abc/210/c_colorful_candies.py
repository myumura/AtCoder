# python3

import collections

n, k = map(int, input().split())
c_list = list(map(int, input().split()))
color = collections.Counter(c_list[:k])
max_c = [len(color)]

for i in range(0, n - k):
    before = c_list[i]
    after = c_list[i + k]
    color[before] -= 1
    if color[before] == 0:
        del color[before]
    if after in color:
        color[after] += 1
    else:
        color[after] = 1
    max_c.append(len(color))

print(max(max_c))
