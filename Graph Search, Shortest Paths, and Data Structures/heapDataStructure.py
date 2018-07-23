def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def bubbleUpComparison(currentNode, parentNode, heapType):
    if heapType == "M" and currentNode > parentNode:
        return True
    elif heapType == "m" and currentNode < parentNode:
        return True
    else:
        return False


def bubbleDownComparison(currentNode, l_child, r_child, heapType):
    if heapType == "M":
        if currentNode < l_child and l_child >= r_child:
            return "L"
        elif currentNode < r_child and r_child > l_child:
            return "R"

    elif heapType == "m":
        if currentNode > l_child and l_child <= r_child:
            return "L"
        elif currentNode > r_child and r_child < l_child:
            return "R"


class Heap:
    def __init__(self, input_data, heapType):
        if heapType == "M":
            self.Heap = [float("inf")]
        elif heapType == "m":
            self.Heap = [float("-inf")]
        self.heapType = heapType
        self.buildHeap(input_data)

    def bubbleUp(self, currentIndex):
        parentIndex = currentIndex // 2
        # if current node is greater than it's parent node, then swap them

        if bubbleUpComparison(
                self.Heap[currentIndex],
                self.Heap[parentIndex],
                self.heapType):
            swap(self.Heap, currentIndex, parentIndex)
            self.bubbleUp(parentIndex)

    def buildHeap(self, input_data):
        for element in input_data:
            self.addNode(element)

    def heapSort(self):
        temp = []
        while len(self.Heap) > 1:
            temp.append(self.extract())
        return temp

    def extract(self):
        assert len(self.Heap) > 1
        return_value = self.Heap[1]
        last_node = self.Heap.pop()

        if len(self.Heap) <= 1:
            return last_node

        self.Heap[1] = last_node
        currentIndex = 1

        while currentIndex <= len(self.Heap) - 1:
            try:
                currentNode = self.Heap[currentIndex]
                l_child = self.Heap[currentIndex * 2]
                r_child = self.Heap[currentIndex * 2 + 1]
                bubbledown = bubbleDownComparison(
                    currentNode, l_child, r_child, self.heapType)

                if bubbledown == "L":
                    swap(self.Heap, currentIndex, currentIndex * 2)
                    currentIndex = currentIndex * 2

                elif bubbledown == "R":
                    swap(self.Heap, currentIndex, currentIndex * 2 + 1)
                    currentIndex = currentIndex * 2 + 1

                else:
                    return return_value

            except BaseException:
                return return_value

    def addNode(self, node):
        self.Heap.append(node)
        currentIndex = len(self.Heap) - 1
        self.bubbleUp(currentIndex)

def test():
    testdata = [[1,2,3,4],[4,3,2,1],[2,5,3,4,1],[1],[1,2],[2,1]]
    for data in testdata:
        print("Test dataset: {}".format(data))
        test = Heap(data, "M")
        print("Heapsort with Max Heap: {}".format(test.heapSort()))
        test = Heap(data, "m")
        print("Heapsort with Min Heap: {}".format(test.heapSort()))
        print("\n\n")
        

if __name__ == "__main__":
    test()
