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
        Problem:
            Given a linkedlist of length n, we 
            define the *twin* of the ith node 
            to be the (n-i)th node.

            Then, we define the twinsum as the 
            sum of a node and it's twin.

            Return the maximum twinsum. 
            Note: we are guaranteed a linkedlist
            with an even number of nodes, so all
            nodes will have a twin.
        Solution:
            Iterate through the linkedlist 
            and add all the numbers to a list.
            Once that list is made, 
            use it to compute all the twinsums,
            and return the maximum twinsum.

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