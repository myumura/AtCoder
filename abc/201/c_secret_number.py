# -*- coding: utf-8 -*-
# python3
s = input()
ans = 0

for i in range(10000):
    pad_i = str(i).zfill(4)
    frag = [False] * 10
    for j in pad_i:
        frag[int(j)] = True
    ans_frag = True
    for j in range(10):
        if s[j] == 'o' and not frag[j]:
            ans_frag = False
        if s[j] == 'x' and frag[j]:
            ans_frag = False
    ans += ans_frag

print(ans)
