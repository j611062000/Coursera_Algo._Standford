from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.queue = []
        self.layer = defaultdict(list)

    def addedge(self, nodeU, nodeV):
        # the directed edge is from U to V (U --> V)
        self.graph[nodeU].append(nodeV)

    def shortestPath(self, source, destination, printLayer=False):
        shortestPath = self.BFS(source, destination)[0]
        if printLayer:
            for layer in self.layer:
                print("Layer: {}".format(layer))
                for node in self.layer[layer]:
                    print("{:^3}, ".format(node), end="")
                print()

        # return the shortest path of (source, destination)
        return shortestPath

    def BFS(self, startingVertex, destination=None):
        """
        Args:
        startingVertex: the starting point for BFS
        destination: only user call shortestPath(), this argument should be specified

        Returns:
        BFS() returns two results, distance of shortest path and the explored nodes
        """
        self.enqueue(self.queue, startingVertex, 0)
        traversed_nodes = [startingVertex]
        # flush the contents in self.layer in order to find connected components
        self.layer = defaultdict(list)
        self.layer[0].append(startingVertex)
        temp_dist = None

        def isIn(x, y): return True if x in y else False

        while self.queue != []:
            temp_value = self.queue[0][0]
            temp_layer = self.queue[0][1]
            self.dequeue(self.queue)

            if temp_value in self.graph:
                for adjNode in self.graph[temp_value]:
                    if (not isIn(adjNode, traversed_nodes) and
                        not isIn(adjNode, self.layer[temp_layer + 1])):
                        self.enqueue(self.queue, adjNode, temp_layer + 1)
                        self.layer[temp_layer + 1].append(adjNode)
                        traversed_nodes.append(adjNode)
                        if adjNode == destination:
                            temp_dist = temp_layer + 1
        return temp_dist, traversed_nodes

    def enqueue(self, queue_list, value, layer):
        queue_list.append((value, layer))

    def dequeue(self, queue_list):
        del queue_list[0]


def constructGraph(dataset):
    g = Graph()
    for key in dataset:
        for node in dataset[key]:
            g.addedge(key, node)
    return g


def testBFS():
    dataset = {4: [5, 6], 5: [4, 6], 6: [4, 5]}
    testGraph = constructGraph(dataset)
    testGraph.BFS(4)
    print("testGraph.layer=%s" % (testGraph.layer))


if __name__ == "__main__":
    testBFS()
