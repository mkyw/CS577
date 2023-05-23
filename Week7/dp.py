import sys


def binarySearch(job, start_index):
    low = 0
    high = start_index - 1

    while low <= high:
        mid = (low + high) // 2
        if int(job[mid][1]) <= int(job[start_index][0]):
            if int(job[mid + 1][1]) <= int(job[start_index][0]):
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def schedule(job):
    M = [0] * numjobs
    M[0] = int(job[0][2])
    for x in range(1, numjobs):
        w = int(job[x][2])
        y = binarySearch(job, x)
        if y != -1:
            w += int(job[y][2])

        M[x] = max(w, M[y-1])

    return M[numjobs-1]


instances = int(sys.stdin.readline())
for i in range(instances):
    numjobs = int(sys.stdin.readline())

    jobs = list()
    for i in range(numjobs):
        jobs.append(sys.stdin.readline().split())

    jobs.sort(key=lambda x: x[1])
    print(schedule(jobs))
