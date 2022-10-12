class Node():
    def __init__(self, children, isEndOfWord):
        self.children = children
        self.isEndOfAWord = isEndOfWord

class Trie(object):

    def __init__(self):
        self.root = Node(children = {}, isEndOfWord = False)

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if (self.search(word)) or len(word) == 0:
            return
        else:
            self.insertHelper(word, self.root)
    
    def insertHelper(self, word, node):
        if (len(node.children) == 0) and (len(word) > 1):
            node.children[word[0]] = Node(children = {}, isEndOfWord = False)
        elif (len(node.children) == 0) and (len(word) == 1):
            node.children[word[0]] = Node(children = {}, isEndOfWord = True)
        
        # if we get here,
        # node.children is not empty!
        elif len(word) == 1:
            node.children[word[0]] = Node(children = {}, isEndOfWord = True)
        else:
            if word[0] in node.children:
                self.insertHelper(word[1:], node.children[word[0]])
            else:
                node.children[word[0]] = Node(children = {}, isEndOfWord = False)
                self.insertHelper(word[1:], node.children[word[0]])
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        return self.searchHelper(word, self.root)
    

    def searchHelper(self, word, node):
        firstLetter = word[0]
        if len(node.children) == 0 or not(firstLetter in node.children):
            return False
        elif (len(word) == 1) and (firstLetter in node.children):
            return Node.children[firstLetter].isEndOfWord
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
        firstLetter = prefix[0]
        if len(node.children) == 0:
            return False
        elif len(prefix) == 1:
            return (firstLetter in node.children)
        elif len(prefix) > 1:
            return (firstLetter in node.children) and (self.startsWithHelper(prefix[1:], node.children[firstLetter]))
        else:
            return False # we should never get here, but just in case! 
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print("obj.search(app):  ", obj.search("app"))
print("obj.search(apple):", obj.search("apple"))
print("obj.prefix(a):    ", obj.prefix("a"))
print("obj.prefix(ap):   ", obj.prefix("ap"))
print("obj.prefix(app):  ", obj.prefix("app"))
print("obj.prefix(appl): ", obj.prefix("appl"))
print("obj.prefix(apple):", obj.prefix("apple"))
print("obj.prefix(ab)", obj.prefix("ab"))


# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)