a = input()
for i in range(len(a)):
    if a[i] == ':':
        b = i
c = a.find(':')
print(a[c+1:b])
