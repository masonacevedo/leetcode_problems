class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
            Problem:
                Given an array, of nums,
                and an integer k, 
                return the number of 
                contiguous subarrays that 
                sum to k. 
            Solution:
                Compute the "prefix sums" for the list of numbers.
                Then, once you have the prefix sums, store them
                in a hashmap so that it's easy to find a pair of prefix
                sums that adds up to k. (Inspired by twosum solution)
                For example, consider: 
                [3,5,4,1,6], k = 10
                Then, the prefix sums are:
                [3,8,12,13,16]
                Then, if we loop through the prefix sums,
                once we get to 13, we can check if there's a 13-10=3
                in the hashmap, and if there is, we increment the count.
                If there are multiple 3's in the hashmap, we increase the
                count that many times. 
        """
        # Compute prefix sums
        sum = 0
        prefixSums = []
        for num in nums:
            sum += num
            prefixSums.append(sum)
        
        hashMap = {}
        # There might be some prefix sums that
        # already sum to k, so start the count
        # with however many of those there are. 
        count = prefixSums.count(k)
        for num in prefixSums:
            if (num-k) in hashMap:
                count += hashMap[num-k]
            
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        return count