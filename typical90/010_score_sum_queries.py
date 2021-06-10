# -*- coding: utf-8 -*-
# python3

n = int(input())
score_list = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
q_list = [list(map(int, input().split())) for _ in range(q)]

a_score_sum = 0
b_score_sum = 0
a_score_list = [0] * (n + 1)
b_score_list = [0] * (n + 1)
answer = ''

for i in range(n):
    if score_list[i][0] == 1:
        a_score_sum += score_list[i][1]
        a_score_list[i + 1] = a_score_sum
        b_score_list[i + 1] = b_score_sum
    else:
        b_score_sum += score_list[i][1]
        b_score_list[i + 1] = b_score_sum
        a_score_list[i + 1] = a_score_sum

for i in q_list:
    start = i[0]
    goal = i[1]
    a_ans = a_score_list[goal] - a_score_list[start - 1]
    b_ans = b_score_list[goal] - b_score_list[start - 1]
    answer += str(a_ans) + ' ' + str(b_ans) + '\n'

print(answer)
