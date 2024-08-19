h, b, c, s = map(int, input().split())
temp = (h * b * c * s)/8
result = temp/1024
mb = result/1024
print(format(mb, '0.1f'), 'MB')