from heapDataStructure import Heap


class HeapFormedian:

    """
                   median

    [max heap]                     [min heap]
    smaller than median            greater than median
    """

    def __init__(self, dataset):
        self.minHeap = Heap([], "m")
        self.maxHeap = Heap([], "M")
        self.leftTop = None
        self.rightTop = None
        for element in dataset:
            self.addNode(element)

    def addNode(self, node):
        self.maxHeap.addNode(node)
        if not self.isBalance():
            self.balanceing()
        try:
            self.leftTop = self.maxHeap.Heap[1]
            self.rightTop = self.minHeap.Heap[1]
        except:
            pass

    def isBalance(self):
        rightnodes = len(self.minHeap.Heap)
        leftnodes = len(self.maxHeap.Heap)
        if rightnodes - leftnodes <= 1 and rightnodes >= leftnodes:
            return True
        else:
            return False

    def balanceing(self):
        while not self.isBalance():
            left_nodes = len(self.maxHeap.Heap)
            right_nodes = len(self.minHeap.Heap)
            if left_nodes > right_nodes:
                self.minHeap.addNode(self.maxHeap.extract())

    def getMedian(self):
        assert self.isBalance
        try:
            print("self.leftTop=%s, self.rightTop=%s" % (self.leftTop, self.rightTop))
            if len(self.maxHeap.Heap) == len(self.minHeap.Heap):
                return (self.leftTop + self.rightTop) / 2
            else:
                return self.rightTop
        except:
            pass



if __name__ == "__main__":
    testData = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(2, len(testData)):
        print(testData[:i])
        test = HeapFormedian(testData[:i + 1])
        print(test.getMedian())
        print("self.minHeap.Heap=%s" % (test.minHeap.Heap))
        print("self.maxHeap.Heap=%s" % (test.maxHeap.Heap))
        print("\n\n")
