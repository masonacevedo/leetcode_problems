class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Problem: 
            Given two strings, s and t,
            return True if they are isomorphic
            and False otherwise.
            Two strings are isomorphic if 
            there exists a function F, which maps
            characters to other characters, such that
            applying F to every character in string s
            results in string t. 
        Solution:
            We iterate through one of the strings and 
            build an isomorphism as we go. For example, 
            consider:
            s = "egg"
            t = "add"
            We iterate through the characters of s. At 
            each step, we find one more mapping that must
            be in our isomorphism. i.e. if there is an 
            isomorphism, it must be the case that 
            e -> a
            g -> d
            g -> d
            This is totally fine, so we return True. 
            To see a situation where we'd return False,
            consider:

            s = "foo"
            b = "bar"
            We iterate through tha characters of s, and we 
            find:
            f -> b
            o -> a
            o -> r. 
            We see "o" must map to both "a" and "r". 
            This is not a valid function, so we return False.
            This idea is implemented easily with a hashmap. 

            This is the gist of the solution, but there is an important
            edge case. Namely, this checks if there is a valid
            function from s to t, but not the other way around.
            To illustrate, consider another example:
            s = "badc"
            t = "baba"
            Our code would see that we must have:
            b -> b
            a -> a
            d -> b
            c -> a
    
            The code would not find a situation where one letter
            needs to get mapped to two different letters, and would
            therefore return True.
            
            However, we wan't to return False, because
            both "b" and "d" map to "b". Can't have two letters
            mapping to the same letter.
            
            Luckily, this problem is easily solved if we just run
            the same code with the the arguments s and t swapped.
            Then, we get:

            b -> b
            a -> a
            b -> d
            a -> c

            Then, our code would pick up on the fact that "b" is 
            mapped to both "b" and "d", and return False.

            So, our function needs to check if there is a valid
            function from s to t, and from t to s. So just call it twice
            and take the "AND" of them. 
        """
        return self.validFunctionExists(s,t) and self.validFunctionExists(t,s)
    
    def validFunctionExists(self, s,t):
        isomorphism = {}
    
        for index in range(0, len(s)):
            if s[index] in isomorphism:
                if isomorphism[s[index]] != t[index]:
                    return False
            else:
                isomorphism[s[index]] = t[index]
    
        return True