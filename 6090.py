a, m, d, n = map(int, input().split())

arr = []

for _ in range(n - 1):
    a = a * m + d
    arr.append(a)

print(a)
