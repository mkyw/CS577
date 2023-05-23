import math

n = int(input())
m = int(input())

a = [-1] * n

for i in range(m):
    x, y, z = map(int, input().split())
    if x > 0 and a[abs(x) - 1] == -1:
        a[abs(x) - 1] = 1
    if y > 0 and a[abs(y) - 1] == -1:
        a[abs(y) - 1] = 1
    if z > 0 and a[abs(z) - 1] == -1:
        a[abs(z) - 1] = 1

countSat = sum([1 for i in a if i == 1])
threshold = math.floor(7 * m / 8)

i = n - 1
while countSat < threshold:
    if a[i] == -1:
        countSat += 1
        a[i] = 1
    i -= 1

for i in range(n):
    print(a[i], end=' ')
