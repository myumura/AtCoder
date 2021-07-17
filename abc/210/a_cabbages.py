# python3

n, a, x, y = map(int, input().split())

if n <= a:
    ans = x * n
else:
    ans = x * a + y * (n - a)

print(ans)
