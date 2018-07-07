from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.queue = []

    def addedge(self, nodeU, nodeV):
        # the directed edge is from U to V (U --> V)
        self.graph[nodeU].append(nodeV)

    def BFS(self, startingVertex):
        self.enqueue(self.queue, startingVertex)
        traversed_nodes = []

        while self.queue != []:
            temp = self.queue[0]
            print(temp, end = " / ")
            self.dequeue(self.queue)
            traversed_nodes.append(temp)
            
            if temp in self.graph:
                for adjacentNode in self.graph[temp]:
                    if adjacentNode not in traversed_nodes:
                        self.enqueue(self.queue, adjacentNode)

            
    def enqueue(self,queue_list, value):
        queue_list.append(value)

    def dequeue(self,queue_list):
        del queue_list[0]
    

g = Graph()
g.addedge(2, 0)
g.addedge(0, 2)
g.addedge(0, 1)
g.addedge(1, 2)
g.addedge(2, 3)
g.addedge(3, 3)
print(g.graph)
g.BFS(2)
