N = input().strip().upper()
value = int(N, base=16)
for i in range(1, 16):
    result = value * i
    hex_value = format(i, 'X')
    hex_result = format(result, 'X')
    print(f'{N}*{hex_value}={hex_result}')
