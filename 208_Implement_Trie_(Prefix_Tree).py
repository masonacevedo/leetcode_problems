class Node():
    def __init__(self, children, isEndOfWord):
        self.children = children
        self.isEndOfWord = isEndOfWord

    def __str__(self):
        output = "children:"
        output += str(self.children)
        return output

class Trie(object):

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
        if (len(node.children) == 0) and (len(word) > 1):
            node.children[word[0]] = Node(children = {}, isEndOfWord = False)
            self.insertHelper(word[1:], node.children[word[0]])
        elif (len(node.children) == 0) and (len(word) == 1):
            node.children[word[0]] = Node(children = {}, isEndOfWord = True)
        
        # if we get here,
        # node.children is not empty!
        elif len(word) == 1:
            if word[0] in node.children:
                node.children[word[0]].isEndOfWord = True
            else:
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
        # print("word:", word)
        # print("node:", str(node))
        # print()
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
obj.insert("aaa")
obj.insert("aab")
obj.insert("aac")
obj.insert("aad")
obj.insert("aa")
obj.insert("ab")
obj.insert("ac")
obj.insert("ad")

print("obj.startsWith('aaa'):", obj.startsWith('aaa'))

# print("obj.startsWith('a'):", obj.startsWith('a'))
# print("obj.startsWith('ab'):", obj.startsWith('ab'))
# print("obj.startsWith('ac'):", obj.startsWith('ac'))
# print("obj.startsWith('ad'):", obj.startsWith('ad'))
# print()

# print("obj.startsWith('aa'):", obj.startsWith('aa'))
# print("obj.startsWith('aab'):", obj.startsWith('aab'))
# print("obj.startsWith('aac'):", obj.startsWith('aac'))
# print("obj.startsWith('aad'):", obj.startsWith('aad'))
# print()

# print("obj.startsWith('aaaa'):", obj.startsWith('aaaa'))
# print("obj.startsWith('aaab'):", obj.startsWith('aaab'))
# print("obj.startsWith('aaac'):", obj.startsWith('aaac'))
# print("obj.startsWith('aaad'):", obj.startsWith('aaad'))
# print()
# print("Beginning of Search Tests:")
# print()

# print("obj.search('a')", obj.search("a"))
# print("obj.search('aa')", obj.search("aa"))
# print("obj.search('aaa')", obj.search("aaa"))
# print()

# print("obj.search('ab')", obj.search("ab"))
# print("obj.search('ac')", obj.search("ac"))
# print("obj.search('ad')", obj.search("ad"))
# print()

# print("obj.search('aab'):", obj.search('aab'))
# print("obj.search('aac'):", obj.search('aac'))
# print("obj.search('aad'):", obj.search('aad'))



# print("obj.search(apple):", obj.search("apple"))
# print("obj.search(app):  ", obj.search("app"))
# print("obj.startsWith(a):    ", obj.startsWith("a"))
# print("obj.startsWith(ap):   ", obj.startsWith("ap"))
# print("obj.startsWith(app):  ", obj.startsWith("app"))
# print("obj.startsWith(appl): ", obj.startsWith("appl"))
# print("obj.startsWith(apple):", obj.startsWith("apple"))
# print("obj.startsWith(ab)", obj.startsWith("abc"))


# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)