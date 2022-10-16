class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
        
        n = len(nums)
        expectedSum = n*(n+1)//2
        difference = expectedSum - sum
        return difference

nums = [3,0,1]

mySol = Solution()
ans = mySol.missingNumber(nums)
print("ans:", ans)