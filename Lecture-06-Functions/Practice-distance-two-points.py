dist = lambda x1, y1, x2, y2 : ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
print(dist(x1, y1, x2, y2))