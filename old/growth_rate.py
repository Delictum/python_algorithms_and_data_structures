n = int(input())

points = []

mas = [[int(x) for x in input().split()] for i in range(n)]    
mas.sort(key=lambda x: x[1])

j = 0
points.append(mas[0][1])
for i in range(1, n):
    if mas[i][0] > points[j]:
        points.append(mas[i][1])
        j += 1

for point in points:
    print(point, end=' ')
