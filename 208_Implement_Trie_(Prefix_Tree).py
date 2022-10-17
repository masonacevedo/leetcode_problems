class Node():
    """
    Node objects are very simple. 
    children is a dictionary where 
    the keys are letters and the 
    values are Node objects associated
    with those letters.

    isEndOfWord is a boolean value that denotes
    whether this particular node/letter is the 
    end of a word or not. 
    """
    def __init__(self, children, isEndOfWord):
        self.children = children
        self.isEndOfWord = isEndOfWord

class Trie(object):
    """
    Implementation of a Trie data structure.
    Supports the following operations:
        Insert(element): 
            Inserts element in to trie.
            Runtime: Average Case: O(average word length) 
        Search(element):
            Checks to see if element has been added to trie. 
            Runtime: Average Case: O(average word length)
        startsWith(prefix):
            Checks to see if there exists a word in the trie
            with a given prefix. 
            Runtime: Average Case: O(average word length)
    """
    def __init__(self):
        self.root = Node(children = {}, isEndOfWord = False)

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        # if word is already in the trie,
        # or the "word" is an empty string, do nothing!
        if (self.search(word)) or len(word) == 0:
            return
        else:
            self.insertHelper(word, self.root)
    
    def insertHelper(self, word, node):
        """
        Idea:
            To insert a word into the trie, 
            we first check to see if the first
            letter of the word is in the trie.
            If it's not, we make a node for it, 
            and recurisvely add the rest of the word.
            If it is, we navigate down to that letters
            children and recursively add the rest of the word.

            The reason this code is long and ugly is because
            there's lots of edge cases. 
            We need different logic when we've reached
            the bottom of the trie, or when we've 
            reached the end of the word, or when 
            we're trying to insert a word that's just
            a prefix of an already inserted word. 

        """
        firstLetter = word[0]
        if len(node.children) == 0 and len(word) == 1:
            # if node has no children, AND we're at the end of a word,
            # then we need to denote that the new Node is the end of a word.
            newNode = Node(children = {}, isEndOfWord = True)
            node.children[firstLetter] = newNode
        elif (len(node.children) == 0) and (len(word) > 1):
            # if node has no children, then we're at the
            # bottom of the trie. So, make a new node. 
            newNode = Node(children = {}, isEndOfWord = False)
            node.children[firstLetter] = newNode
            self.insertHelper(word[1:], node.children[firstLetter])
        elif len(word) == 1:
            # if we're only adding one letter to the trie, we do one of two things:
            # Set isEndOfWord to True for the letter, if it's already in the trie
            # Build a new node and add it to the trie.
            if firstLetter in node.children:
                node.children[firstLetter].isEndOfWord = True
            else:
                newNode = Node(children = {}, isEndOfWord = True)
                node.children[firstLetter] = newNode
        else:
            # most general case: word has several letters
            # AND the node we're looking at has children. 
            restOfWord = word[1:]
            if firstLetter in node.children:
                self.insertHelper(restOfWord, node.children[firstLetter])
            else:
                node.children[firstLetter] = Node(children = {}, isEndOfWord = False)
                self.insertHelper(restOfWord, node.children[firstLetter])
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        return self.searchHelper(word, self.root)
    

    def searchHelper(self, word, node):
        """
        Idea: 
            A word is in the trie if and only if 
            the first letter is in the trie, AND 
            the rest of the word is in the trie.
            The edge cases are pretty easy. 

            Keep in mind that node every node 
            in the trie is the end of a word, so 
            we need to check the boolean
            associated with the end of the node. 
        """
        firstLetter = word[0]
        if len(node.children) == 0 or not(firstLetter in node.children):
            return False
        elif (len(word) == 1) and (firstLetter in node.children):
            return node.children[firstLetter].isEndOfWord
        elif len(word) > 1:
            return self.searchHelper(word[1:], node.children[firstLetter])
        else:
            return False # we should never get to this, but just in case!



    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0:
            return True
        else:
            return self.startsWithHelper(prefix, self.root)
    
    def startsWithHelper(self, prefix, node):
        """
        Very similar idea to search, 
        but with slightly different handling 
        of the node.isEndOfBoolean variable. 
        """
        firstLetter = prefix[0]
        if len(node.children) == 0:
            return False
        elif len(prefix) == 1:
            return (firstLetter in node.children)
        elif len(prefix) > 1:
            restOfPrefix = prefix[1:]
            return (firstLetter in node.children and 
                   self.startsWithHelper(restOfPrefix, node.children[firstLetter]))
        else:
            return False # we should never get here, but just in case! 