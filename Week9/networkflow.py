import sys


def BFS(self, s, t, parent):

    visited = [False]*(self.ROW)

    queue = []

    queue.append(s)
    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(self.graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True

    return False


def ford_fulkerson(self, source, sink):
    parent = [-1] * (self.ROW)
    max_flow = 0

    while self.searching_algo_BFS(source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, self.graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while (v != source):
            u = parent[v]
            self.graph[u][v] -= path_flow
            self.graph[v][u] += path_flow
            v = parent[v]

    return max_flow


instances = int(sys.stdin.readline())

for i in range(instances):
    VE = sys.stdin.readline().split()
    nodes = VE[0]
    numEdges = VE[1]
    edges = list()
    for i in range(int(numEdges)):
        edges.append(sys.stdin.readline().split())
    print(edges)

    flow = 0
