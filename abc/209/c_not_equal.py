import sys
input = sys.stdin.readline
 
n = int(input())
c_list = list(map(int, input().split()))
 
c_list.sort()
 
ans = 1
count = 0
 
for i in c_list:
    ans *= (i - count)
    ans %= 10 ** 9 + 7
    if ans == 0:
        break
    count += 1
 
print(ans)
