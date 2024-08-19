N = int(input())
clap = ['3', '6', '9']
arr = []
for i in range(1, N + 1):
    cnt = 0
    for claps in str(i):
        if claps in clap:
            cnt += 1
    if cnt > 0:
        i = 'X' * cnt
    print(i, end=' ')
