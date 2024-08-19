arr = [list(map(int, input().split())) for _ in range(19)]
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1  # 인덱스 조정
    b -= 1  # 인덱스 조정

    # 해당 열(a)을 뒤집기
    for i in range(19):
        arr[a][i] = 1 - arr[a][i]  # 0은 1로, 1은 0으로

    # 해당 행(b)을 뒤집기
    for i in range(19):
        arr[i][b] = 1 - arr[i][b]  # 0은 1로, 1은 0으로

# 결과 출력
for row in arr:
    print(*row)
