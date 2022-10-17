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
            Problem:
                Given the head of a linked list, determine if it has a cycle.
                If it does, return the head of the cycle.
                If it doesn't, return None.
            Solution:
                Iterate through the linked list, and maintain a 
                hash set of nodes we've already seen before.
                At each step, check to see if we've seen this particular
                node before.
                If we have, return this node.
                If this never happens, return None.
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