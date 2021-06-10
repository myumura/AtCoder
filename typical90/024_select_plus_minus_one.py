# -*- coding: utf-8 -*-
# python3

n, k = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

diff_list = [abs(a_list[i] - b_list[i]) for i in range(n)]
diff_sum = sum(diff_list)
rest = k - diff_sum

if rest % 2 != 0 or k < diff_sum:
    print("No")
else:
    print("Yes")
