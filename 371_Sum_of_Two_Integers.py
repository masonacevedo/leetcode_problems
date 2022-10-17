class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        Problem: 
            Given two integers, return their sum
            without using the "+" or "-" operators.
        Solution:
            Convert the integers into binary strings,
            add them as binary strings, then convert 
            them back. 
        
        NOTE: This solution works when a and b are 
        both non-negative. It doesn't work otherwise.
        """
        aString = bin(a)[2:]
        bString = bin(b)[2:]

        sumString = self.addBinaryNums(aString, bString, carry=False)
        return int(sumString,2)
    
    def addBinaryNums(self, s1,s2, carry):
        if (len(s1) == 0):
            return self.addBinaryNums("0", s2, carry)
        if (len(s2) == 0):
            return self.addBinaryNums("0", s1, carry)
        
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