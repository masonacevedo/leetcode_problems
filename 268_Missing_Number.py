class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Problem:
            Given a list of distinct, numbers,
            all in the range [0,n], 
            return the only number that is missing.
        Solution:
            When all the numbers
            From 0 to n are present,
            their sum should be 1 + 2 + .. + n,
            which simplfies to n(n+1)/2.
            So, compute quantity, then compare
            it to the actual sum of the numbers
            in the array, and that will tell you
            what's missing.
        """
        sum = 0
        for num in nums:
            sum += num
        
        n = len(nums)
        expectedSum = n*(n+1)//2
        difference = expectedSum - sum
        return difference