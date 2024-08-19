def min_flips(target):
    length = len(target)
    current = [0] * length  # 초기 상태는 모두 0
    flips = 0

    for i in range(length):
        # 현재 상태와 목표 상태가 다르면 뒤집기
        if target[i] != current[i]:
            flips += 1
            # i+1의 배수 위치에 있는 모든 값 뒤집기
            for j in range(i, length, i + 1):
                current[j] = 1 - current[j]  # 0을 1로, 1을 0으로

    return flips

# 입력 받기
target = list(map(int, input().split()))

# 최소 뒤집기 횟수 계산
result = min_flips(target)
print(result)
