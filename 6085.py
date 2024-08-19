w, h, b = map(int, input().split())
temp = (w * h * b) / 8
result = temp/1024
mb = result/1024
print(format(mb, '0.2f'), 'MB')
