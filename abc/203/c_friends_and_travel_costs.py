# -*- coding: utf-8 -*-

N, K = map(int, input().split())
vil = 0
rest = K
answer = ''

money = [list(map(int, input().split())) for _ in range(N)]
money.sort()

for i in range(len(money)):
    now = money[i][0]
    rest -= now - vil
    vil = now
    if rest >= 0:
        rest += money[i][1]
        answer = vil + rest
    else:
        answer = vil + rest
        break

print(answer)
