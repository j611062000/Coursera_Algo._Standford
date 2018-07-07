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
        shortestPath = self.BFS(source, destination)
        if printLayer:
            for layer in self.layer:
                print("Layer: {}".format(layer))
                for node in self.layer[layer]:
                    print("{:^3}, ".format(node), end="")
                print()

        # return the shortest path of (source, destination)
        return shortestPath

    def BFS(self, startingVertex, destination=None):

        self.enqueue(self.queue, startingVertex, 0)
        traversed_nodes = []
        self.layer[0].append(startingVertex)
        temp_dist = None

        while self.queue != []:
            temp_value = self.queue[0][0]
            temp_layer = self.queue[0][1]
            self.dequeue(self.queue)
            # mark temp as explored node
            traversed_nodes.append(temp_value)

            if temp_value in self.graph:
                for adjacentNode in self.graph[temp_value]:
                    if adjacentNode not in traversed_nodes:
                        self.enqueue(self.queue, adjacentNode, temp_layer + 1)
                        self.layer[temp_layer + 1].append(adjacentNode)
                        if adjacentNode == destination:
                            temp_dist = temp_layer + 1
        return temp_dist

    def enqueue(self, queue_list, value, layer):
        queue_list.append((value, layer))

    def dequeue(self, queue_list):
        del queue_list[0]


if __name__ == "__main__":

    g = Graph()
    g.addedge(2, 0)
    g.addedge(0, 2)
    g.addedge(0, 1)
    g.addedge(1, 2)
    g.addedge(2, 3)
    g.addedge(3, 3)
    print(g.graph)
    print(g.BFS(2, 1))
    print(g.layer)
