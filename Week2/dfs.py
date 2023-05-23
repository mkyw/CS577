import sys

# Basic node class


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

# Modified graph class, basic structure cited to https://www.programiz.com/dsa/graph-adjacency-list

# Graph is unfinished, unable to account for lettered nodes


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    # DFS function

    # incomplete, still needs testing
    def DFS(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)

        print(v)

        for next in graph[v] - visited:
            DFS(graph, next, visited)
        return visited


if __name__ == "__main__":
    numGraphs = int(sys.stdin.readline())

    # does this for # of instances provided
    for i in range(numGraphs):
        numNodes = int(sys.stdin.readline())

        # Create graph and edges
        graph = Graph(numNodes)
        for j in range(numNodes):
            nodes = sys.stdin.readline().split()
            for k in range(1, len(nodes)):
                graph.add_edge(nodes[0], nodes[k])

        graph.print_agraph()

        # DFS on root node
        DFS(graph, 1)
