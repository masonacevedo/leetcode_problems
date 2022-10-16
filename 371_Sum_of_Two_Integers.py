class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        aString = bin(a)[2:]
        bString = bin(b)[2:]

        sumString = self.addBinaryNums(aString, bString, carry=False)
        return int(sumString,2)
    
    def addBinaryNums(self, s1,s2, carry):
        # print("s1:", s1)
        # print("s2:", s2)
        # print()
        if (len(s1) == 0):
            return self.addBinaryNums("0", s2, carry)
        if (len(s2) == 0):
            return self.addBinaryNums("0", s1, carry)
        # if both last digits are 1
        numOnes = [s1[-1],s2[-1]].count("1")
        if carry:
            numOnes += 1
        
        if len(s1) == 1 and len(s2) == 1:
            if numOnes == 0:
                return ""
            elif numOnes == 1:
                return "1"
            elif numOnes == 2:
                return "10"
            else:
                return "11"
        

        restOfS1 = s1[0:len(s1)-1]
        restOfS2 = s2[0:len(s2)-1]

        if (numOnes == 0):
            return self.addBinaryNums(restOfS1, restOfS2, carry = False) + "0"
        elif (numOnes == 1):
            return self.addBinaryNums(restOfS1, restOfS2, carry = False) + "1"
        elif (numOnes == 2):
            return self.addBinaryNums(restOfS1, restOfS2, carry = True) + "0"
        elif (numOnes == 3):
            return self.addBinaryNums(restOfS1, restOfS2, carry = True) + "1"

mySol = Solution()
ans = mySol.getSum(10,30)
print("ans:", ans)