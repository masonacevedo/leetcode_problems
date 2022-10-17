class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Problem:
            Given an array of integers,
            (which may be positive, negative, 
            zero, and non-distinct)
            Find the contiguous subarray 
            with the maximum sum.
        Solution:
            Kadane's algorithm. (Google it!)
        """
        # special case for when the entire
        # list is negative
        if max(nums) < 0:
            return max(nums)
        currentSum = 0
        bestSoFar = 0

        for num in nums:
            if num > 0:
                currentSum += num
            else:
                if (currentSum + num) > 0:
                    currentSum += num
                else:
                    currentSum = 0
            bestSoFar = max(bestSoFar, currentSum)
        
        return bestSoFar