from heapDataStructure import Heap


def printHeap(HeapFormedian):
    print("maxHeap.Heap=%s" % (HeapFormedian.maxHeap.Heap), end="  |  ")
    print("minHeap.Heap=%s" % (HeapFormedian.minHeap.Heap))


def printTop(HeapFormedian):
    print(
        "L Top:{}  ||  R Top:{}".format(
            HeapFormedian.leftTop,
            HeapFormedian.rightTop))


class HeapFormedian:

    """
                   median

    [max heap]                     [min heap]
    smaller than median            greater than median
    """

    def __init__(self, dataset):
        self.maxHeap = Heap([], "M")
        self.minHeap = Heap([], "m")
        self.leftTop = None
        self.rightTop = None
        self.median = None
        for element in dataset:
            self.addNode(element)
            print("\n\n")

    def addNode(self, node):
        print("new node:", node)
        if self.median is None:
            self.median = node
            self.minHeap.addNode(node)
        elif node <= self.median:
            self.maxHeap.addNode(node)
            print("new node to left, because of <={}".format(self.median))
        elif node > self.median:
            self.minHeap.addNode(node)
            print("new node to right, because of >{}".format(self.median))

        print("before balanceing:", end=" ")
        printHeap(self)

        if not self.isBalance():
            self.balanceing()

        print("after balanceing :", end=" ")
        printHeap(self)

        # revising the top value of heaps respectively
        self.reviseHeapTop()
        printTop(self)

        self.median = self.getMedian()

    def isBalance(self):
        rightnodes = len(self.minHeap.Heap)
        leftnodes = len(self.maxHeap.Heap)
        if (rightnodes - leftnodes) == 1 or (rightnodes - leftnodes) == 0:
            return True
        else:
            return False

    def reviseHeapTop(self):
        lenOfLeftHeap = len(self.maxHeap.Heap)
        lenOfRightHeap = len(self.minHeap.Heap)

        if lenOfLeftHeap >= 2:
            self.leftTop = self.maxHeap.Heap[1]
        elif lenOfLeftHeap < 2:
            self.leftTop = None

        if lenOfRightHeap >= 2:
            self.rightTop = self.minHeap.Heap[1]
        elif lenOfLeftHeap < 2:
            self.rightTop = None

    def balanceing(self):
        while not self.isBalance():
            left_nodes = len(self.maxHeap.Heap)
            right_nodes = len(self.minHeap.Heap)

            if left_nodes > right_nodes:
                self.minHeap.addNode(self.maxHeap.extract())
            elif right_nodes > left_nodes:
                self.maxHeap.addNode(self.minHeap.extract())

    def getMedian(self):
        assert self.isBalance

        if self.rightTop is not None and self.leftTop is not None:
            if len(self.maxHeap.Heap) == len(self.minHeap.Heap):
                return (self.leftTop + self.rightTop) / 2
            else:
                return self.rightTop

        else:
            return self.rightTop


def test():
    testData = [[10, 99, 100, 1, 2, 2, 4, 1, 0, 100, 88]]
    for test in testData:
        testcase = HeapFormedian(test)


if __name__ == "__main__":
    test()
