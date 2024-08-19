N = int(input())
arr = list(map(int, input().split()))

result = [0] * 23
for i in range(N):
    result[arr[i]-1] += 1
print(*result)