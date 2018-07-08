from DFS import Graph, constructGraph


def topological_sorting(graph, nodes):
    """
    Args:
    the Graph object provided by DFS
    """
    temp_topo = []
    for node in nodes:
        if node not in graph.explored_nodes:
            graph.flushDFS()
            graph.DFS(node)
            temp_topo = graph.topo[::-1] + temp_topo

    return temp_topo


def numberOfNode(dataset):
    keys = list(dataset.keys())
    values = []
    for data in dataset:
        for element in dataset[data]:
            values.append(element)
    return list(set(keys + values))


if __name__ == "__main__":
    dataset = {1: [2, 3], 2: [4], 3: [4, 5], 4: [5]}
    testGraph = constructGraph(dataset)
    print("topological_sorting(testGraph)=%s" %
          (topological_sorting(testGraph, numberOfNode(dataset))))
