# -*- coding: utf-8 -*-
# python3

n = int(input())
request = [input() for _ in range(n)]
user_list = set()
answer = []

for i, j in enumerate(request):
    if j not in user_list:
        user_list.add(j)
        answer.append(i + 1)

for i in answer:
    print(i)
