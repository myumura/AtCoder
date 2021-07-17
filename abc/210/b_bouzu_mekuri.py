# python3

n = int(input())
s = str(input())
count = 0

for i in s:
    count += 1
    if i == '1':
        if count % 2 == 0:
            print('Aoki')
            break
        else:
            print('Takahashi')
            break
