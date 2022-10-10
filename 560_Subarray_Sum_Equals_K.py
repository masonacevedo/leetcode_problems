class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Idea: Compute the "prefix sums" for the list of numbers.
        Then, once you have the prefix sums, store them
        in a hashmap so that it's easy to find a pair of prefix
        sums that adds up to k
        For example, consider: 
        [3,5,4,1,6], k = 10
        Then, the prefix sums are:
        [3,8,12,13,16]
        Then, if we loop through the prefix sums,
        once we get to 13, we can check if there's a 13-10=3
        in a hashmap, and if there is, we increment the count.
        If there are multiple 3's in the hashmap, we increase the
        count that many times! 
        """
        sum = 0
        prefixSums = []
        for num in nums:
            sum += num
            prefixSums.append(sum)
        
        hashMap = {}

        count = prefixSums.count(k)
        for index in range(0, len(prefixSums)):
            if (prefixSums[index]-k) in hashMap:
                count += hashMap[prefixSums[index]-k]
            if not(prefixSums[index] in hashMap):
                hashMap[prefixSums[index]] = 1
            else:
                hashMap[prefixSums[index]] += 1
        return count