class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        leftSums = [0]
        for index in range(1, len(nums)):
            sum += nums[index-1]
            leftSums.append(sum)

        sum = 0
        rightSums = [0]
        for index in reversed(range(0, len(nums)-1)):
            sum += nums[index+1]
            rightSums.append(sum)
        rightSums.reverse()
    
        for index in range(0, len(leftSums)):
            if (leftSums[index] == rightSums[index]):
                return index
        
        return -1
        


mySol = Solution()
nums = [2,1,-1]
ans = mySol.pivotIndex(nums)
print("ans:", ans)