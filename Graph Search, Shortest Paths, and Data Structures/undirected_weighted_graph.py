from collections import defaultdict


class weightedGraph:
    def __init__(self):
        self.distance = {}
        self.graph = defaultdict(list)

    def addEdge(self, Node1, Node2, weighted):
        self.graph[Node1].append(Node2)
        self.distance[(Node1, Node2)] = weighted


def dijkstra(source, weightedGraph,destinations=None):
    visited, unvisited, distanceFromSource = dijkstraInit(source, weightedGraph)
    
    while unvisited != []:
        (currentNode, mindist) = minDist(distanceFromSource,visited)
        for adjnode in weightedGraph.graph[currentNode]:
            distanceFromSource[adjnode] = min(distanceFromSource[adjnode], distanceFromSource[currentNode] + weightedGraph.distance[(currentNode, adjnode)])
        visited.append(currentNode)
        unvisited.remove(currentNode)
    return distanceFromSource[destinations]

    
def minDist(distanceFromSource, visited):
    """
    extract the min value/node from the given distance list
    """
    mindist = 1000001
    currentNode = None
    for node in distanceFromSource:
        if node not in visited:
            if distanceFromSource[node] < mindist:
                mindist = distanceFromSource[node]
                currentNode = node
    if mindist<1000000:
        return currentNode, mindist

def dijkstraInit(source, weightedGraph):
    visited = []
    unvisited = []
    distanceFromSource = defaultdict(list)
    distanceFromSource[source] = 0
    for node in weightedGraph.graph:
        unvisited.append(node)
        if node != source:
            distanceFromSource[node] = 1000000

    return visited, unvisited, distanceFromSource

def constructGraph(dataset, graph):
    for pair in dataset:
        graph.addEdge(pair[0], pair[1], pair[2])


def readingFile(file):
    with open(file, "r") as file:
        tempList = []
        for line in file.readlines():
            raw = line.split("\t")[:-1]
            head = int(raw[0])
            body = [raw[i].split(",") for i in range(1, len(raw))]
            for node in body:
                tempList.append([head, int(node[0]), int(node[1])])

    return tempList


if __name__ == "__main__":
    dataset = [["a", "b", 1], ["a", "c", 2], [
        "b", "c", 3], ["b", "d", 4], ["c", "d", 5]]
    graph1 = weightedGraph()
    constructGraph(dataset, graph1)
    print(graph1.graph)
    print(graph1.distance)
