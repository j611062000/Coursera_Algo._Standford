from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.explored_nodes = []
        self.DFS_path = []
        self.stack = []
        self.topo = []

    def addedge(self, nodeU, nodeV):
        # the directed edge is from U to V (U --> V)
        self.graph[nodeU].append(nodeV)
    
    def flushDFS(self):
        self.DFS_path = []
        self.topo = []

    def DFS(self, startingVertex, flush = False):
        
        if flush:
            self.flushDFS()

        self.DFS_path.append(startingVertex)
        self.explored_nodes.append(startingVertex)
        self.stack.append(startingVertex)

        for adjnode in self.graph[startingVertex]:
            if adjnode not in self.explored_nodes:
                self.DFS(adjnode)

        # record the topological sort
        self.topo.append(self.stack.pop())
        return self.DFS_path



def testDFS():
    dataset = {1: [2, 3], 2: [4], 3: [4, 5], 4: [5]}
    testGraph = constructGraph(dataset)
    print("topological_sorting(testGraph)=%s" %
          (topological_sorting(testGraph)))


def constructGraph(dataset):
    g = Graph()
    for key in dataset:
        for node in dataset[key]:
            g.addedge(key, node)
    return g


if __name__ == "__main__":
    testDFS()
