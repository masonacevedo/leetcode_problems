import math

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0):
            return 0
        power = math.floor(math.log(n,2))
        num = n
        count = 0
        while (power >= 0):
            if (math.pow(2,power) <= num):
                num -= math.pow(2,power)
                count += 1
            power -= 1
        return count

mySol = Solution()

mySol.hammingWeight(4294967293)