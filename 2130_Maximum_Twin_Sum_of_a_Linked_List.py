# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        nums = []
        currentNode = head
        while (currentNode):
            nums.append(currentNode.val)
            currentNode = currentNode.next
        
        currentSum = float("-inf")
        bestSoFar = currentSum

        for index in range(0, len(nums)//2):
            currentSum = nums[index] + nums[-1*(index+1)]
            bestSoFar = max(bestSoFar, currentSum)
        return bestSoFar

# l6 = ListNode(-30, next = None)
# l5 = ListNode(-20, next = l6)
# l4 = ListNode(-10, next = l5)
# l3 = ListNode(0, next = l4)
# l2 = ListNode(10, next = l3)
# l1 = ListNode(20, next = l2)

# mySol = Solution()
# mySol.pairSum(l1)