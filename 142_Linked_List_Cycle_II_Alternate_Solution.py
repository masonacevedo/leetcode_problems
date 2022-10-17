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
                Floyd's Cycle-Finding Algorithm. (google it!)
                (Uses Slow-Pointer/Fast-Pointer)
        """

        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                break
        if (fast == None) or (fast.next == None):
            return None
        
        slow2 = head
        while slow != slow2:
            slow = slow.next
            slow2 = slow2.next
        
        return slow