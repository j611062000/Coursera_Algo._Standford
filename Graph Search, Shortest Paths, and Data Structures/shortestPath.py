from BFS import Graph

dataset = {0: [1, 2], 1: [3, 4], 2: [5, 6], 5: [7, 8]}

def constructGraph(dataset):
    g = Graph()
    for key in dataset:
        for node in dataset[key]:
            g.addedge(key, node)
    return g

graph1 = constructGraph(dataset)
print("Shortest Path of ({},{}) is {}".format(0,8,graph1.shortestPath(0,8, True)))
