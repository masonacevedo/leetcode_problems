class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Problem: 
            Given a list of n nums all in the range
            [1,n], find the duplicate number in O(n) 
            time and O(1) space.
        Solution:
            This solution is bizarre!
            It recognizes that the array of nums 
            can be thought of as a linked list.
            Specifically, because each entry is between
            [1,n], we can think of each entry as containing 
            the index of some other entry. Then, we follow the 
            trail and voila! Linked list behavior. 
            Then, we use Floyd cycle-finding algorithm to 
            find the beginning of the cycle, which is the repeated element.
        """
        slow = nums[0]
        fast = nums[0]

        count = 0
        # this could technically be a while(True), 
        # but just in case we receive a bad input... 
        while (count < 3 * (len(nums))): 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if (fast == slow):
                break
            count += 1
    
        slow2 = nums[0]
        while (slow != slow2):
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow