arr = [list(map(int, input().split())) for _ in range(10)]
i, j = 1, 1  # 시작 위치 (2, 2) → 인덱스 (1, 1)로 변환
arr[i][j] = 9  # 시작 위치를 9로 설정

while True:
    if arr[i][j] == 2:
        arr[i][j] = 9
        break

    # 오른쪽으로 이동 가능하면 이동
    if j + 1 < 10 and arr[i][j + 1] != 1:
        j += 1
    # 아래쪽으로 이동 가능하면 이동
    elif i + 1 < 10 and arr[i + 1][j] != 1:
        i += 1
    else:
        break  # 더 이상 이동할 수 없는 경우 종료

    if arr[i][j] == 2:
        arr[i][j] = 9
        break

    arr[i][j] = 9  # 이동한 위치를 9로 설정

# 결과 출력
for row in arr:
    print(*row)
