N = int(input())
s = 0
for i in range(N + 1):
    if i % 2 == 0:
        s += i
print(s)