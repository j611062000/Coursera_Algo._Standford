from BFS import Graph, constructGraph

# 3 connected components in graph, dataset
dataset = {0: [1, 3], 1: [2, 0], 2: [3, 1], 3: [0, 2], 
           4: [5, 6], 5: [4, 6], 6: [4, 5], 
           7:[8], 8:[7]}

def findConnectedComponents(graph):
    """
    Arguments:
    The argument is the object of Graph defined in BFS.py

    Returns:
    A list composed of connected components
    """
    temp_connectedComponent = []
    traversed_nodes = []
    for node in graph.graph:
        if node not in traversed_nodes:
            traversed_nodes += graph.BFS(node)[1]
            temp_connectedComponent.append(graph.layer)
    return temp_connectedComponent


graph1 = constructGraph(dataset)
for component in findConnectedComponents(graph1):
    print(component)
