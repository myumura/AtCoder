# -*- coding: utf-8 -*-
# python3
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
road = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    road[A].append(B)


def dfs(s):
    if goal[s]:
        return
    goal[s] = True
    for r in road[s]:
        dfs(r)


ans = 0
for i in range(1, N + 1):
    goal = [False] * (N + 1)
    dfs(i)
    ans += sum(goal)

print(ans)
