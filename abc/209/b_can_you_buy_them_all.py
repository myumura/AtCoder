n, x = map(int, input().split())
a_list = list(map(int, input().split()))

a_sum = sum(a_list) - n // 2

ans = 'Yes' if a_sum <= x else 'No'
print(ans)
