import heapq

class MedianFinder(object):
    """
    This data structure works by keeping two heaps.
    Specifically, a minHeap is used to keep track of the 
    larger half of the elements so far, and a maxHeap is used
    to keep track of the smaller half of the elements so far.

    Then, when a user asks for the median, we have access to
    the smallest of the larger half and the largest of the smaller half.
    The median will either be one of these values OR their average,
    depending on whether there's an even or odd number of elements added so far.
    
    In order to add an element, we simply have to determine which 
    heap it belongs in by comparing it to the min of the right half
    and the max of the left half. If we end up in a situation where
    we want to add a number to the heap that's already bigger, we simply
    do a little rebalancing to make sure that the heap sizes are within 1
    of each other.

    NOTE: The maxHeap is implemented using a minHeap data structure, 
    but every element is multiplied by -1 before pushing and after popping.
    So, instead of just calling heapq's heappush() and heappop() methods
    for the max heap, we have our own versions of the functions.
    """
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    
    def __repr__(self):
        outputString = "minHeap:"
        outputString += str(self.minHeap)
        outputString += "\n"

        # all this is needed because maxheap
        # stores negative numbers
        outputString += "maxHeap:"
        outputString += "["
        for index in range(0, len(self.maxHeap)):
            outputString += str(-1*self.maxHeap[index])
            if (index != len(self.maxHeap)-1):
                outputString += ", "

        outputString += "]\n"
        return outputString

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        Adds an element to either the min or max heap based on the following criteria:
            If an element is in the larger half of elements we've seen so far, 
            it gets added to the min Heap
            If an element is in the smaller half of elements we've seen so far,
            it gets added to the max heap. 
            
            if, after adding, one heap would be larger than the other by a margin 
            of 2 elements, (i.e. max has 10 elements and min has 8),
            then we pop an element off the larger heap and push it onto the smaller
            heap in order to rebalance. 

        Runs in O(logn) time, where n is the number of elements added to
        the medianFinger object so far. 
        """
        if (len(self.minHeap) == 0) and (len(self.maxHeap) == 0):
            heapq.heappush(self.minHeap, num)
        elif len(self.minHeap) == len(self.maxHeap):
            if num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                self.maxHeapPush(num)
        elif len(self.minHeap) > len(self.maxHeap):
            if (num >= self.minHeap[0]):
                heapq.heappush(self.minHeap, num)
                elementToMove = heapq.heappop(self.minHeap)
                self.maxHeapPush(elementToMove)
            else:
                self.maxHeapPush(num)
        else:
            if (num <= self.peekMaxHeap()):
                self.maxHeapPush(num)
                elementToMove = self.maxHeapPop()
                heapq.heappush(self.minHeap, elementToMove)
            else:
                heapq.heappush(self.minHeap, num)

    def findMedian(self):
        """
        :rtype: float
        If the number of elements in the data structure is even, this means
        that half of them are stored in the minheap, and half are stored in the 
        maxheap. In that case, return the average of the minHeap element and maxHeap element.
        Otherwise, return whatever element is atop the larger heap, because that's the one that
        would be in the 'middle' of the sorted array.

        Runs in O(1) time.
        """
        if len(self.minHeap) == len(self.maxHeap):
            return (float(self.minHeap[0]) + float(self.peekMaxHeap()))/2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.peekMaxHeap()
        
    def peekMaxHeap(self):
        return (-1 * self.maxHeap[0])

    def maxHeapPush(self, num):
        heapq.heappush(self.maxHeap, -1*num)
    
    def maxHeapPop(self):
        return -1 * heapq.heappop(self.maxHeap)