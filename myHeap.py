class myMinHeap:

    def __init__(self, L = None):
        if L is None:
            self.heap = []
            self.heapSize = 0
        else:
            self.heap = L
            self.heapSize = len(L)
            self.heapify()

    def __repr__(self):
        return str(self.heap[0:self.heapSize])

    def pop(self):
        if len(self.heap) == 0:
            pass
        else:
            element = self.heap[0]
            lastElement = self.heap[self.heapSize-1]
            self.heap[0] = lastElement
            self.percolateDown(indexToPerc = 0)
            self.heapSize -= 1
            return element

    def percolateDown(self, indexToPerc):
        """
        To percolate the top element down, we 
        compare the element to it's two children,
        and replace it with the smaller of it's two children,
        until the element is smaller than both it's children.
        """
        currentIndex = indexToPerc

        leftChildIndex = (2*currentIndex) +  1
        rightChildIndex = (2*currentIndex) + 2
        while (currentIndex <= self.heapSize-1) and \
              (leftChildIndex <= self.heapSize-1) and \
              (rightChildIndex <= self.heapSize-1) and \
              ((self.heap[currentIndex] > self.heap[rightChildIndex]) or \
               (self.heap[currentIndex] > self.heap[leftChildIndex])):
            # swap current node and parent node
            if (self.heap[leftChildIndex] < self.heap[rightChildIndex]):
                swapIndex = leftChildIndex
            else:
                swapIndex = rightChildIndex
            
            temp = self.heap[currentIndex] 
            self.heap[currentIndex] = self.heap[swapIndex]
            self.heap[swapIndex] = temp 
            currentIndex = swapIndex
            leftChildIndex =  (2*currentIndex) + 1
            rightChildIndex = (2*currentIndex) + 2

    def push(self, element):
        # pseudocode:
        # add element to bottom-right-most heap element
        # to preserve structure property, then percolate
        # it up until order property is restored.
        if len(self.heap) == 0:
            self.heap.append(element)
        else:
            if len(self.heap) == self.heapSize:
                self.heap.append(element)
                self.percolateUp(self.heapSize)
            else:
                self.heap[self.heapSize] = element
                self.percolateUp(self.heapSize)
                # then percolate this element up
        self.heapSize += 1
    
    def percolateUp(self, index):
        """
        In order to percolate an element up, 
        we look at the element and it's parent.
        Then, if the element is smaller than it's parent,
        we swap those to, and begin again. Otherwise, we stop
        self.heap = [10,20,15,30,40,60,0]
        """
        
        currentIndex = index
        parentIndex = (currentIndex-1)//2
        while (currentIndex >= 0) and (parentIndex >= 0) and (self.heap[currentIndex] < self.heap[parentIndex]):
            
            # swap current node and parent node
            temp = self.heap[currentIndex] 
            self.heap[currentIndex] = self.heap[parentIndex]
            self.heap[parentIndex] = temp

            # this works bc of the heap property! 
            currentIndex = parentIndex
            parentIndex = (currentIndex-1)//2
    
    def heapify(self):
        """
        To heapify a tree that doesn't satisfy the 
        order property, we iterate backwards
        through the tree and percolate every element 
        with children down.
        """
        
        firstIndexWithChildren = (self.heapSize//2)-1
        index = firstIndexWithChildren
        while (index >= 0):
            self.percolateDown(index)
            index -= 1