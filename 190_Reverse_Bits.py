class Solution:
    """
    Problem:
        Given an integer, compute it's binary representation,
        reverse that representation, and return the associated integer.
    Solution:
        Use python built-in functions.
    """
    def reverseBits(self, n):
        numAsString = bin(n)
        backwardsString = numAsString[:1:-1]
        backwardsWithZeros = backwardsString + (32-len(backwardsString))*"0"
        return int(backwardsWithZeros,2)