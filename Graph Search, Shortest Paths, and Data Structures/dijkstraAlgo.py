from undirectedWeightedGraph import weightedGraph
from undirectedWeightedGraph import constructGraph
from undirectedWeightedGraph import readingFile
from collections import defaultdict

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



if __name__ == "__main__":

	dataset = readingFile("dijkstraData.txt")
	source = 1
	destinations = [7,37,59,82,99,115,133,165,188,197]
	ans = []

	for element in destinations:
		graph = weightedGraph()
		constructGraph(dataset, graph)
		ans.append(dijkstra(source, graph, element))

	print(ans)
	# [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]