# python3

n = int(input())
a = list(map(int, input().split()))
score_list = sorted(a, reverse=True)
print(a.index(score_list[1]) + 1)
