class linked_list_node:
    def __init__(self, data, isRoot=False):
        self.data = data
        self.next_node = None
        self.isRoot = isRoot
        if isRoot:
            self.rear = None

    def add_node_to_root(self, newNode):
        if self.next_node is None:
            self.next_node = newNode
            self.rear = self.next_node
        else:
            self.rear.next_node = newNode
            self.rear = newNode

    def traversing_from_root_and_print(self):
        temp = self

        while True:
            if temp.next_node is not None:
                print("[{:^3}] -->".format(temp.data), end="")
                temp = temp.next_node
            else:
                print("[{:^3}] --> None".format(temp.data))
                break

# class graph_by_adjacnecy_list(linked_list_node):

def createLinkedList(dataset):
    root = linked_list_node(dataset[0], True)
    for i in range(1, len(dataset)):
        root.add_node_to_root(linked_list_node(dataset[i]))
    return root


def test_linked_list():
    dataset = [1, 2, 3, 4, 5, 2, "a", "Sid"]
    linkedList1 = createLinkedList(dataset)
    linkedList1.traversing_from_root_and_print()
    print("Root_data: {}, Rear_data: {}".format(
        linkedList1.data, linkedList1.rear.data))


def createAdjacencyList(undirected_graph_dic):
    table = []
    for key in undirected_graph_dic:
        table.append(createLinkedList([key] + undirected_graph_dic[key]))
    return table


if __name__ == "__main__":
    undirected_graph_dic = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [1]}
    undirected_graph_2DList = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0]
    ]

    graph1 = createAdjacencyList(undirected_graph_dic)
    for element in graph1:
        element.traversing_from_root_and_print()
