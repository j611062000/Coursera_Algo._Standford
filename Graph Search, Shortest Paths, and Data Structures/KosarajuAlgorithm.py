from DFS import Graph, constructGraph
from collections import defaultdict


def reverseGraph(dataset):
    temp_dic = defaultdict(list)
    for key in dataset:
        for element in dataset[key]:
            if key not in temp_dic[element]:
                temp_dic[element].append(key)
    return constructGraph(temp_dic)


def numberOfNode(dataset):
    keys = list(dataset.keys())
    values = []
    for data in dataset:
        for element in dataset[data]:
            values.append(element)
    return len(list(set(keys + values)))

def printProgress(i, total):
    print("{:3.2f} %".format(100*i/total))

def k_algo(dataset):
    starting_vertex = 1
    reverse_graph = reverseGraph(dataset)
    graph = constructGraph(dataset)
    DFS_order_for_reverseGraph = graph.DFS(starting_vertex)
    total = len(DFS_order_for_reverseGraph)

    temp_SCC = []
    for count, node in enumerate(DFS_order_for_reverseGraph):
        printProgress(count, total)
        if node not in reverse_graph.explored_nodes:
            temp_SCC.append(reverse_graph.DFS(node, True))
    return temp_SCC


if __name__ == "__main__":
    dataset = defaultdict(list)
    with open("SCC.txt", "r") as file:
        for element in file.readlines():
            data_pair = [int(num) for num in element.split(" ")[:-1]]
            dataset[data_pair[0]].append(data_pair[1])
    print(k_algo(dataset))


# 434821,968,459,313,211
