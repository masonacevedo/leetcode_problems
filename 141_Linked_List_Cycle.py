# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
            Problem:
                Given the head of a linked list, 
                return true if the linked list 
                has a cycle and return false otherwise.
            Solution:
                Maintain a hash set of nodes that we've seen before. 
                At each step, check to see if we've seen this node before.
                    If we have, return the node.
                    If we haven't, add the node to the hash set and continue.
        """
        seenBefore = set()
        currentNode = head
        while currentNode != None:
            if currentNode in seenBefore:
                return True
            else:
                seenBefore.add(currentNode)
            currentNode = currentNode.next
        
        return False