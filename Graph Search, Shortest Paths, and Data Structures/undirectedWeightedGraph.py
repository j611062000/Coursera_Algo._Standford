from collections import defaultdict


class weightedGraph:
    def __init__(self):
        self.distance = {}
        self.graph = defaultdict(list)

    def addEdge(self, Node1, Node2, weighted):
        self.graph[Node1].append(Node2)
        self.distance[(Node1, Node2)] = weighted



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



