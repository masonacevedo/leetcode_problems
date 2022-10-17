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
                Use a slow and a fast pointer. If there's 
                a cycle, the fast pointer will eventually catch
                up to the slow pointer. If this never happens, 
                there is no cycle. 
        """
        slow = head
        fast = head
        while (fast != None) and (fast.next != None):
            
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        
        return False