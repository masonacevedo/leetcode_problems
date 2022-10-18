class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Problem:
            Given a list of numbers,
            find and return the
            indices of two numbers
            that sum to a specified
            target.

        Solution:
            Iterate through the list
            and use a hashmap.
            Specifically, for every 
            number you encounter,
            store that number as a 
            key, and store the index
            as it's associated value.

            Then, as we iterate,
            we can use the hashmap to 
            quickly find pairs. Specifically,
            suppose we're looking at some
            number x. Then, we can check
            the hashmap in O(1) time to 
            see if we've seen target-X 
            before. If we have, then
            we return the current index
            and whatever index we stored
            with target-X. 

        """
        hashMap = {}
        
        for index in range(0, len(nums)):
            num = nums[index]
            if (target - num) in hashMap:
                return [index, hashMap[target - num]]
            else:
                hashMap[num] = index