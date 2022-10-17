class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if (len(nums) == 1):
            return nums[0]

        # The optimal robbing of just 1 house 
        # is to rob that house.
        # The optimal robbing of two houses is just
        # to rob the one with more money. Thus,
        # We have the following base cases
        DPTable = [nums[0], max(nums[0], nums[1])]
        for index in range(2, len(nums)):
            robThisHouse = DPTable[index-2] + nums[index]
            dontRobThisHouse = DPTable[index-1]
            DPTable.append(max(robThisHouse, dontRobThisHouse))
        
        return DPTable[-1]
    
    def robRecursive(self, nums):
        """
        This is the slow recursive solution.
        The optimized DP solution is above.
        """
        if (len(nums) == 1):
            return nums[0]
        elif (len(nums) == 2):
            return (max(nums))
        else:
            robLastHouse = nums[-1] + self.robRecursive(nums[0:len(nums)-2])
            dontRobLastHouse = self.robRecursive(nums[0:len(nums)-1])
            return max(robLastHouse, dontRobLastHouse)