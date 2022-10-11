class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        This solution is bizarre!
        It recognizes that the array of nums 
        can be thought of as a linked list.
        Specifically, bc each entry is between
        [1,n], we can think of each entry as containing 
        the index of some other entry. Then, we follow the 
        trail to create a linked list.
        Then, we use Floyd's algorithm to 
        find the beginning of the cycle, which is the repeated element.
        """
        slow = nums[0]
        fast = nums[0]

        # this is loop condition 
        # is technically unnecessary,
        # since we're guaranteed that a loop
        # exists in our linked list,
        # so we are guaranteed to get to
        # the "break" statement
        # However, just in case we get
        # some input we're not supposed to,
        # we just arbitrarily cut off the loop at 
        # 3n (the loop should always terminate before this)
        count = 0
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
        
        

nums = [1,3,4,2,2]
mySol = Solution()
ans = mySol.findDuplicate(nums)
print("ans:", ans)