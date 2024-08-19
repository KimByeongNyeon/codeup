N = int(input())
cnt = 0
result = 0
while result < N:
    result += cnt
    cnt += 1
    if result >= N:
        print(cnt - 1)
        break

