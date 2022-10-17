import heapq

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Problem:
            Sort an array of numbers.
        Solution:
            Add all the numbers to a minHeap,
            then just keep calling pop.
            They will pop off the heap
            in ascending order! 
        """
        heapq.heapify(nums)
        ans = []
        while len(nums) > 0:
            ans.append(heapq.heappop(nums))
        
        return ans