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

mySol = Solution()

l6 = ListNode(-30, next = None)
l5 = ListNode(-20, next = l6)
l4 = ListNode(-10, next = l5)
l3 = ListNode(0, next = l4)
l2 = ListNode(10, next = l3)
l1 = ListNode(20, next = l2)

mySol.middleNode(l1)
