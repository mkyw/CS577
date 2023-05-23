import sys


class BipartiteMaxMatching:
    def __init__(self, numNodesA, numNodesB, numEdges):
        self.numNodesA = numNodesA
        self.numNodesB = numNodesB
        self.adjMatrix = [[0] * numNodesB for _ in range(numNodesA)]

    @staticmethod
    def parse_input():
        instances = []
        numInstances = int(input())

        for _ in range(numInstances):
            numNodesA, numNodesB, numEdges = map(int, input().split())
            instance = BipartiteMaxMatching(numNodesA, numNodesB, numEdges)

            for _ in range(numEdges):
                nodeA, nodeB = map(int, input().split())
                instance.addEdge(nodeA, nodeB)

            instances.append(instance)

        return instances

    def addEdge(self, nodeA, nodeB):
        self.adjMatrix[nodeA - 1][nodeB - 1] = 1

    def maxMatching(self):
        matches = [0] * self.numNodesB
        count = 0

        for i in range(self.numNodesA):
            visited = [0] * self.numNodesB

            if self.isMatch(visited, matches, i):
                count += 1

        return count

    def isMatch(self, visited, matches, i):
        for j in range(self.numNodesB):
            if self.adjMatrix[i][j] == 1 and visited[j] == 0:
                visited[j] = 1

                if matches[j] == 0 or self.isMatch(visited, matches, matches[j]):
                    matches[j] = i
                    return True

        return False

    def isPerfectMatch(self):
        for i in range(self.numNodesA):
            for j in range(self.numNodesB):
                if self.adjMatrix[i][j] == 0:
                    return 'N'

        return 'Y'


if __name__ == '__main__':
    try:
        instances = BipartiteMaxMatching.parse_input()
        for m in instances:
            print(m.maxMatching(), m.isPerfectMatch())
    except:
        print(sys.exc_info()[0])
