from undirected_weighted_graph import weightedGraph
from undirected_weighted_graph import constructGraph
from undirected_weighted_graph import readingFile
from undirected_weighted_graph import dijkstra

dataset = readingFile("dijkstraData.txt")
destinations = [7,37,59,82,99,115,133,165,188,197]
ans = []

for element in destinations:
	graph = weightedGraph()
	constructGraph(dataset, graph)
	ans.append(dijkstra(1, graph, element))

print(ans)
# [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]