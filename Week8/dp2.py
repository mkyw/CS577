import sys

instances = int(sys.stdin.readline())
for i in range(instances):
    l1 = sys.stdin.readline().split()
    numItems = int(l1[0])
    cap = int(l1[1])
    items = list()
    for j in range(numItems):
        items.append(sys.stdin.readline().split())

    M = [[0 for i in range(cap + 1)] for j in range(numItems + 1)]

    for i in range(numItems + 1):
        for j in range(cap + 1):
            if i == 0 or j == 0:
                M[i][j] = 0
            elif int(items[i-1][0]) <= j:
                M[i][j] = max(M[i-1][j-int(items[i-1][0])] +
                              int(items[i-1][1]), M[i-1][j])
            else:
                M[i][j] = M[i-1][j]

    print(M[numItems][cap])
