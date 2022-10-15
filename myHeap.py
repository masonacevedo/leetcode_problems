from turtle import right
from xml.dom.minidom import Element


class myMinHeap:

    def __init__(self):
        self.heap = []
        self.heapSize = 0
    def __repr__(self):
        return str(self.heap[0:self.heapSize])

    def pop(self):
        if len(self.heap) == 0:
            pass
        else:
            element = self.heap[0]
            lastElement = self.heap[self.heapSize-1]
            self.heap[0] = lastElement
            self.percolateDown()
            self.heapSize -= 1
            return element

    def percolateDown(self):
        """
        To percolate the top element down, we 
        compare the element to it's two children,
        and replace it with the smaller of it's two children,
        until the element is smaller than both it's children.
        """
        currentIndex = 0
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


test = myMinHeap()

test.push(10)
test.push(50)
test.push(70)
test.push(60)

test.push(0)
test.push(40)
test.push(20)
test.push(30)
print("test:", test)
test.pop()
print("test:", test)
test.pop()
print("test:", test)
test.pop()
print("test:", test)
test.pop()
print("test:", test)
test.pop()
print("test:", test)
test.pop()
print("test:", test)
test.pop()
print("test:", test)
# test.percolateUp(6)