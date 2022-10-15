import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Works by first building a hashmap 
        of all the elements in the list with
        their frequencies. Then, uses a hashmap
        to get the top K frequent of them.
        Runs in O(n + klogn) time. 
        """
        # First, we build a table
        # that gives the frequency of 
        # each element (the table is 
        # just a hashmap). 
        # Runs in O(n) time
        frequencyTable = {}
        for num in nums:
            if (num in frequencyTable):
                frequencyTable[num] += 1
            else:
                frequencyTable[num] = 1
        
        # Once we have the have the frequency table,
        # We add all the elements to a priority queue,
        # where the top element is always the most frequent 
        # element in the list. Runs in O(n) time.
        keys = frequencyTable.keys()
        heap = []
        for key in keys:
            heap.append((-1*frequencyTable[key], key))
        
        # The previous step just added all the values we 
        # need to add; this command actually makes them into
        # a heap that satisfies the structure and order 
        # properties. Runs in O(n) time.
        heapq.heapify(heap)
        
        # finally, we pop k elements off the heap,
        # which are the k most frequent elements.
        # Runs in O(klogn) time. 
        ans = []
        for index in range(0,k):
            ans.append(heapq.heappop(heap)[1])

        return ans