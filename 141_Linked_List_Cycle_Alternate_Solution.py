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
        """
        slow = head
        fast = head
        while (fast != None) and (fast.next != None):
            
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        
        return False



mySol = Solution()
h = ListNode(x = 1)
h.next = None

ans = mySol.hasCycle(h)
print("ans:", ans)