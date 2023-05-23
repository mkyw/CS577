import sys


def main():
    instances = int(sys.stdin.readline())
    numpairs = int(sys.stdin.readline())
    x = list()
    y = list()

    for i in range(instances):
        for j in range(numpairs):
            x.append(int(sys.stdin.readline()))
        for k in range(numpairs):
            y.append(int(sys.stdin.readline()))

        print(algo(x, y))


def algo(x, y):
    intersections = 0
    if len(x) == 2 and len(y) == 2:
        if (x[0] < x[1] and y[1] > y[0]) or (x[1] < x[0] and y[0] > y[1]):
            intersections += 1
    else:
        intersections += algo(x[0:len(x)//2], y[0:len(y)//2])
        intersections += algo(x[len(x)//2:len(x)], y[len(y)//2:len(y)])

    return intersections


if __name__ == "__main__":
    main()
