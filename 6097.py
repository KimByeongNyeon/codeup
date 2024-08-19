h, w = map(int, input().split())
arr = [[0] * w for _ in range(h)]
N = int(input())
for _ in range(N):
    l, d, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if d == 0:
        for i in range(l):
            arr[x][y + i] = 1
    elif d == 1:
        for i in range(l):
            arr[x + i][y] = 1
for row in arr:
    print(*row)
