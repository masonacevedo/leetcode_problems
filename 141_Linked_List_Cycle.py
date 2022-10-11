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
        seenBefore = set()
        currentNode = head
        while currentNode != None:
            if currentNode in seenBefore:
                return True
            else:
                seenBefore.add(currentNode)
            currentNode = currentNode.next
        
        return False

mySol = Solution()
h = ListNode(x = 1)
h.next = None

ans = mySol.hasCycle(h)
print("ans:", ans)