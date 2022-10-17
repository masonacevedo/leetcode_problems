import math

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        Problem:
            Given an integer n, return
            the number of "1"s in the 
            binary representation of that number. 
        Solution:
            Perform the computations that you
            would in order to convert the number
            into a binary string. Every time
            you'd put in a 1, increment a counter.
            Return counter at the end. 
            Note that the binary string's length
            as a function of n is log(n), so
            this solution runs in log(n) time. 
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