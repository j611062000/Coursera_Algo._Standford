import random
import copy
import os

def kargerAlgo(graph_dic):
    graph_after_contract = copy.deepcopy(graph_dic)
    while True:
        node1, node2 = chooseEdge(graph_after_contract)
        contract(graph_after_contract, node1, node2)
        if len(graph_after_contract) <= 2:
            break
    return find_cut_edges(graph_after_contract, graph_dic)


def find_cut_edges(graph_after_contract, graph_dic):
    temp = list(graph_after_contract.keys())
    if isinstance(temp[0], int):
        left_set = [temp[0]]
        right_set = [int(element) for element in temp[1].split("/")]
    elif isinstance(temp[1], int):
        right_set = [temp[1]]
        left_set = [int(element) for element in temp[0].split("/")]
    else:
        left_set = [int(element) for element in temp[0].split("/")]
        right_set = [int(element) for element in temp[1].split("/")]

    count = 0

    for element1 in left_set:
        for element2 in right_set:
            if element1 in graph_dic[element2]:
                count += 1
    return count


def reviseExistingNodes(graph_dic, node1, node2, newnode):
    for key in graph_dic:
        for node in [node1, node2]:
            if node in graph_dic[key]:
                graph_dic[key].remove(node)

    for node in graph_dic[newnode]:
        graph_dic[node].append(newnode)


def contract(graph_dic, node1, node2):
    # create new node
    adjacent_nodes_to_newNode = [ element for element in set(
            graph_dic[node1] +
            graph_dic[node2])]
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
    return [u, v]

def showProgress(i, total_iteration):
    print("Progress:{:^3.1f}%".format(100*(i/total_iteration)))


def test_kargerAlgo(dataset, num):
    min_cut = 10000
    for i in range(num):
        if i%10 == 0:
            showProgress(i,num)
            print("Mincut_so_far:{}".format(min_cut))
        cut_edges = kargerAlgo(dataset)
        if cut_edges < min_cut:
            min_cut = cut_edges
    return min_cut


def test_contract():

    dataset = {1: [2, 3, 4],
               2: [1, 3, 4],
               3: [4, 1, 2, 5],
               4: [1, 2, 3, 5],
               5: [3, 4]}
    print(chooseEdge(dataset))
    contract(dataset, 1, 2)
    print("dataset=%s" % (dataset))
    print(chooseEdge(dataset))
    contract(dataset, "1/2", 4)
    print("dataset=%s" % (dataset))


def test_find_cut_edges():
    before_dataset = {1: [2, 3, 4], 2: [1, 3, 4],
                      3: [4, 1, 2, 5], 4: [1, 2, 3, 5], 5: [3, 4]}
    after_dataset = [{"1/2/3": ["4/5"], "4/5":["1/2/3"]},
                     {"1": ["2/3/4/5"], "2/3/4/5":["1"]}]
    for data in after_dataset:
        print(find_cut_edges(data, before_dataset))


if __name__ == "__main__":
    
    graph_dic = {}
    with open("data_for_kargerMinCut.txt", "r") as file:
        lines = file.readlines()
        for node in lines:
            x = [int(element) for element in node.split("\t")[:-1]]
            graph_dic[x[0]] = x[1:]
    
    print(test_kargerAlgo(graph_dic, 7000))
