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
        """
        nodeList = []
        current = head
        while current != None:
            nodeList.append(current)
            current = current.next
        print("nodeList:", nodeList)

        n = len(nodeList)
        for index in range(0, n):
            nextIndex = self.nextIndex(index,n)
            if nextIndex is None:
                nodeList[index].next = None
            else:
                nodeList[index].next = nodeList[nextIndex]
        print("nodeList:", nodeList)
        
        return head

    def nextIndex(self, x,n):
        if (x < n//2):
            return n-x-1
        elif (x > n//2):
            return (n-x)
        else:
            return None