class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # special case for when the entire
        # list is negative
        if max(nums) < 0:
            return max(nums)
        currentSum = 0
        bestSoFar = 0
        for index in range(0, len(nums)):
            if nums[index] > 0:
                currentSum += nums[index]
            else:
                if (currentSum + nums[index]) > 0:
                    currentSum += nums[index]
                else:
                    currentSum = 0
            bestSoFar = max(bestSoFar, currentSum)
        return bestSoFar