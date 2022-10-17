# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Problem:
            Given the head of a linked list
            return the node in the middle of 
            that linked list.
        Solution:
            Iterate through the linkedlist 
            to count how many elements there are.
            Save that number, then iterate 
            up until length/2.
        """
        length = 0

        currentNode = head
        while currentNode != None:
            currentNode = currentNode.next
            length += 1
        
        middleIndex = length//2
        count = 0
        currentNode = head
        while count < middleIndex:
            currentNode = currentNode.next
            count += 1
        
        return currentNode
