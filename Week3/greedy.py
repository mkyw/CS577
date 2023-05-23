# Shortest finish first algorithm
from queue import Empty
import sys
import math

instances = int(sys.stdin.readline())
for i in range(instances):
    jobs = int(sys.stdin.readline())
    pairs = list()
    for j in range(jobs):
        x = sys.stdin.readline().split()
        x[0] = int(x[0])
        x[1] = int(x[1])
        pairs.append(x)

    pairs = sorted(pairs, key=lambda l: l[1])

    num_jobs = 0
    time = 0
    for i in range(len(pairs)):
        if (time <= int(pairs[i][0])):
            time = int(pairs[i][1])
            num_jobs += 1

    print(num_jobs)
