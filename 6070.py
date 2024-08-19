word = int(input())
if word == 1 or word == 2 or word == 12:
    print('winter')
elif word//3 == 1:
    print('spring')
elif word//3 == 2:
    print('summer')
elif word//3 == 3:
    print('fall')
    