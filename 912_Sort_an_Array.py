import heapq

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        implements quicksort
        """
        heapq.heapify(nums)
        ans = []
        while len(nums) > 0:
            ans.append(heapq.heappop(nums))
        
        return ans