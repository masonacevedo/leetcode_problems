# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return self.reprHelper(1)
    
    def reprHelper(self, depth):
        if depth == 1:
            if self.next is None:
                return "(" + str(self.val) + ", None)" 
            else:
                return "(" + str(self.val) + ", " + self.next.reprHelper(0) + ")"
        else:
            return str(self.val)
    
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
            Problem:
                Given the head of a linked list, modify-it-in place
                so that the nodes have a different ordering. Best
                illustrated by example.
                Given:
                0 -> 1 -> 2 -> ... -> n-1 -> n
                Change it to:
                0 -> n -> 1 -> n-1 -> 2 -> n-2 -> .... 
            Solution:
                Iterate through the linked list and store 
                all the nodes in an array. 
                Then, once we have O(1) access to all the nodes,
                we can just look at them all and replace whatever 
                their "next" node is with whatever it "should" be.
                This is easy to figure out using a mathematical 
                formula. 
        """
        nodeList = []
        current = head
        while current != None:
            nodeList.append(current)
            current = current.next

        n = len(nodeList)
        for index in range(0, n):
            nextIndex = self.nextIndex(index,n)
            if nextIndex is None:
                nodeList[index].next = None
            else:
                nodeList[index].next = nodeList[nextIndex]
        
        return head

    def nextIndex(self, x,n):
        if (x < n//2):
            return n-x-1
        elif (x > n//2):
            return (n-x)
        else:
            return None