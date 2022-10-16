class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        numAsString = bin(n)
        backwardsString = numAsString[:1:-1]
        backwardsWithZeros = backwardsString + (32-len(backwardsString))*"0"
        return int(backwardsWithZeros,2)

mySol = Solution()
print(mySol.reverseBits(n=10))