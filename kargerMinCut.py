import random

def kargerAlgo(graph_dic):
    while True:
        node1, node2 = chooseEdge(graph_dic)
        contract(graph_dic, node1, node2)
        if len(graph_dic)<=2:
            break


def reviseExistingNodes(graph_dic, node1, node2, newnode):
    for key in graph_dic:
        for node in [node1, node2]:
            if node in graph_dic[key]:
                graph_dic[key].remove(node)
    
    for node in graph_dic[newnode]:
        graph_dic[node].append(newnode)

def contract(graph_dic, node1, node2):
    # create new node
    adjacent_nodes_to_newNode = [element for element in set(graph_dic[node1] + graph_dic[node2])]
    adjacent_nodes_to_newNode.remove(node1)
    adjacent_nodes_to_newNode.remove(node2)
    newnode = "{}/{}".format(str(node1), str(node2))
    graph_dic[newnode] = adjacent_nodes_to_newNode
    graph_dic.pop(node1)
    graph_dic.pop(node2)

    # revise existing nodes
    reviseExistingNodes(graph_dic, node1, node2, newnode)

def chooseEdge(graph_dic):
    u = random.choice(list(graph_dic.keys()))
    v = random.choice(graph_dic[u])
    return [u,v]

def test_kargerAlgo():
    for i in range(2):
        dataset = {1: [2, 3,1], 2: [1, 3, 4], 3: [4, 1,2,5], 4: [1, 2, 3,5], 5: [3, 4]}
        kargerAlgo(dataset)
        print(dataset)

def test_contract():

    dataset = {1: [2, 3,1], 2: [1, 3, 4], 3: [4, 1,2,5], 4: [1, 2, 3,5], 5: [3, 4]}
    print(chooseEdge(dataset))
    contract(dataset, 1, 2)
    print("dataset=%s" % (dataset))
    print(chooseEdge(dataset))
    contract(dataset, "1/2", 4)
    print("dataset=%s" % (dataset))


if __name__ == "__main__":
    test_kargerAlgo()
