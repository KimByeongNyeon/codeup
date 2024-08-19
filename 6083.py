r, g, b = map(int, input().split())

colors = []

for red in range(r):
    for green in range(g):
        for blue in range(b):
            colors.append((red, green, blue))

colors.sort()

for color in colors:
    print(color[0], color[1], color[2])

print(len(colors))
