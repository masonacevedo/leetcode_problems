class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        Problem: 
            Compute x to the nth power.
        Solution:
            The straightforward thing
            to do is to multiply x
            by itself n times, and then 
            return that. However,
            that's an O(n) solution and 
            we can do better. 
            Notice that, if n is even,
            then we have the identity:
            x^n = (x^(n//2))^2
            If n is odd, we instead have:
            x^n = x * (x^(n//2))^2
            This enables us to cut 
            n in half at each step, until
            we end up at x^0 or x^1.
            So, we have a log(n) solution.

            Finally, note that if n is negative,
            we just use the fact that
            x^(-n) = 1/(x^n). 
        """
        if n < 0:
            return 1/float(self.myPow(x, -1*n))
        elif n == 0:
            return 1
        elif n == 1:
            return x
        elif (n % 2 == 0):
            numToSquare = self.myPow(x,n//2)
            return numToSquare * numToSquare
        else:
            numToSquare = self.myPow(x,n//2)
            return numToSquare * numToSquare * x