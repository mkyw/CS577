import sys

instances = int(sys.stdin.readline())
for i in range(instances):
    cache_size = int(sys.stdin.readline())
    numReq = int(sys.stdin.readline())

    cache = []
    csz = 0
    seq = sys.stdin.readline().split()

    pagefaults = 0

    for j in range(numReq):
        if csz < cache_size:
            cache.insert(csz, seq[j])
            csz += 1
            pagefaults += 1
        elif seq[j] in cache:
            continue
        else:
            pagefaults += 1

            fitf = None

            pages = set()
            for k in range(j, len(seq)):
                pages.add(seq[k])

            for m in cache:
                if m not in pages:
                    fitf = m

            if fitf == None:
                for l in range(j, len(seq)):
                    if fitf != seq[l] and seq[l] in pages:
                        fitf = seq[l]
                        pages.remove(seq[l])

            for m in range(len(cache)):
                if cache[m] == fitf:
                    cache[m] = seq[j]
                    exit

    print(pagefaults)
