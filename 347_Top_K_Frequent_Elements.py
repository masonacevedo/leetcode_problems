import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Problem: 
            Given a list of nums, and 
            an integer k, return the k
            nums in the list that
            repeat the most often.
            (i.e. have the highest frequncy)
        Solution:
            Iterate through the list,
            and build a hashmap that stores 
            all the elements in the list with
            their frequencies. 

            Then, store the numbers in a priority
            queue, where priorities are 
            assigned according to how frequent
            the elements are. i.e. most 
            frequent thing on top.

            Finally, call heappop() k times.

            Runs in O(n + klogn) time. 
        """
        frequencyTable = {}
        for num in nums:
            if (num in frequencyTable):
                frequencyTable[num] += 1
            else:
                frequencyTable[num] = 1
        

        keys = frequencyTable.keys()
        heap = []
        for key in keys:
            heap.append((-1*frequencyTable[key], key))
        
        # The previous step just added all the values we 
        # need to add; this command actually makes them into
        # a heap that satisfies the structure and order 
        # properties. Runs in O(n) time.
        heapq.heapify(heap)
        
        ans = []
        for index in range(0,k):
            ans.append(heapq.heappop(heap)[1])

        return ans