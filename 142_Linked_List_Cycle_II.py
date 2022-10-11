# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currentNode = head
        seenBefore = set()
        while currentNode != None:
            if currentNode in seenBefore:
                return currentNode
            seenBefore.add(currentNode)
            currentNode = currentNode.next
        
        # if the code makes it here,
        # then we never found a cycle.
        # so, we should return None
        return None