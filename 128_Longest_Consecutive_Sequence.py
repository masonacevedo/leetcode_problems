class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsAsSet = set(nums)
        seqLength = 0
        bestSoFar = 0
        alreadyComputed = set()
        for num in nums:
            # if num-1 is not in the list of nums,
            # then num is the beginning of some consecutive sequence
            # (perhaps of length 1.) So, see how long
            # this sequence is, and compare it to the longest
            # sequence so far.
            if not((num-1) in numsAsSet) and not(num in alreadyComputed):
                seqLength = self.findLongestSequenceGivenBeginning(num, numsAsSet)
                bestSoFar = max(seqLength, bestSoFar)
                alreadyComputed.add(num)
        
        return bestSoFar

    def findLongestSequenceGivenBeginning(self, beginning, numsAsSet):
        count = 1
        while (beginning + 1 in numsAsSet):
            count += 1
            beginning += 1
        return count