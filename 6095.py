arr = [[0] * 19 for _ in range(19)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    for i in range(19):
        for j in range(19):
            arr[x][y] = 1
for row in arr:
    print(*row)