a, m, d = map(int, input().split())

arr = []

for _ in range(d - 1):
    a = a + m
    arr.append(a)

print(a)
