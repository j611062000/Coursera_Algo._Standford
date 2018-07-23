def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


def bubbleUpComparison(currentNode, parentNode, heapType):
    if heapType == "M" and currentNode > parentNode:
        return True
    elif heapType == "m" and currentNode < parentNode:
        return True
    else:
        return False

def isBubbleDown_R(currentNode, l_child, r_child, heapType):
    if l_child is None:
        if heapType == "M":
            if currentNode < r_child:
                return True
        elif heapType == "m":
            if currentNode > r_child:
                return True

    elif l_child is not None:
        if heapType == "M":
            if l_child < r_child and currentNode < r_child:
                return True
        elif heapType == "m":
            if l_child > r_child and currentNode > r_child:
                return True
def isBubbleDown_L(currentNode, l_child, r_child, heapType):
    if r_child is None:
        if heapType == "M":
            if currentNode < l_child:
                return True
        elif heapType == "m":
            if currentNode > l_child:
                return True

    elif r_child is not None:
        if heapType == "M":
            if l_child >= r_child and currentNode < l_child:
                return True
        elif heapType == "m":
            if l_child <= r_child and currentNode > l_child:
                return True

def bubbleDownComparison(currentNode, l_child, r_child, heapType):
    if l_child is not None and r_child is not None:
        if isBubbleDown_R(currentNode, l_child, r_child, heapType):
            return "R"
        elif isBubbleDown_L(currentNode, l_child, r_child, heapType):
            return "L"

    elif l_child is None and r_child is None:
        return None

    elif l_child is None:
        if isBubbleDown_R(currentNode, l_child, r_child, heapType):
            return "R"

    elif r_child is None:
        if isBubbleDown_L(currentNode, l_child, r_child, heapType):
            return "L"


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
        print("Heap:",self.Heap)
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
            return return_value

        self.Heap[1] = last_node
        currentIndex = 1
        treeLen = len(self.Heap) - 1

        while currentIndex <= treeLen:
            currentNode = self.Heap[currentIndex]

            # make sure the path of bubble is within the legal path
            if currentIndex * 2 <= treeLen:
                l_child = self.Heap[currentIndex * 2]
            else:
                l_child = None

            if currentIndex * 2 + 1 <= treeLen:
                r_child = self.Heap[currentIndex * 2 + 1]
            else:
                r_child = None

            bubbledown = bubbleDownComparison(
                currentNode, l_child, r_child, self.heapType)
            print("bubbledown=%s" % (bubbledown))
            print("currentNode=%s, l_child=%s, r_child=%s" % (currentNode, l_child, r_child))
            if bubbledown == "L":
                swap(self.Heap, currentIndex, currentIndex * 2)
                currentIndex = currentIndex * 2

            elif bubbledown == "R":
                swap(self.Heap, currentIndex, currentIndex * 2 + 1)
                currentIndex = currentIndex * 2 + 1

            elif bubbledown is None:
                return return_value

    def addNode(self, node):
        self.Heap.append(node)
        currentIndex = len(self.Heap) - 1
        self.bubbleUp(currentIndex)


def generalTest():
    testdata = [[1,2,2,1]]
    for data in testdata:
        print("Test dataset: {}".format(data))
        test = Heap(data, "M")
        print("MaxHeap:", test.Heap)
        print("Heapsort with Max Heap: {}".format(test.heapSort()))
        test = Heap(data, "m")
        print("Heapsort with Min Heap: {}".format(test.heapSort()))
        print("\n\n")


def extractTest():
    testdata = [[4, 2,2,1]]
    for data in testdata:
        print("Test dataset: {}".format(data))
        test = Heap(data, "M")
        print("heapified dataset: {}".format(test.Heap))
        for i in range(len(data) - 1):
            test.extract()
            print("test.Heap=%s" % (test.Heap))
        print("\n\n")


if __name__ == "__main__":
    test=2
    if test ==1:
        generalTest()
    else:
        extractTest()
