class Solution(object):
    def __init__(self):
        self.openingBrackets = set(["{", "[", "("])
        self.closingBrackets = set(["}", "]", ")"])
        self.bracketPairs = {
                        "{":"}", "}":"{",
                        "[":"]", "]":"[",
                        "(":")", ")":"("}
        
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Idea: Use a stack to keep track of all the parenthesis.
        Specifically: 
            Whenever we see an open parenthesis,
            we push it to the stack.
            Whenever we see a closing parenthesis, 
            we make sure that it matches with whatever is on the stack
            at the moment (if it doesn't return False.) Then pop
            the stack.
        """
        
        # if the string has an odd number of brackets
        # then it must be invalid. 
        if len(s) % 2 == 1:
            return False

        stack = []
        for index in range(0, len(s)):
            char = s[index]
            if len(stack) == 0 and char in self.closingBrackets:
                return False
            elif char in self.openingBrackets:
                stack.append(char)
            elif char in self.closingBrackets and self.bracketPairs[char] != stack[-1]:
                return False
            elif char in self.closingBrackets:
                stack.pop()
            else:
                raise Exception("Character is not a valid bracket.")
        
        if len(stack) > 0:
            return False
        else:
            return True