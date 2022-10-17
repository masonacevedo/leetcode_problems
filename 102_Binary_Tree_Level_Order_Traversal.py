import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
            Problem:
                Traverse a binary tree in level order. 
                i.e. if the tree is:
                     a
                  b     c
                 d e   f g
                Then return the list:
                [[a], [b,c], [d,e,f,g]] 

            Solution:
                Do breadth first search, and make sure that 
                all the nodes on the same level are part of 
                the same sub list. 
        """
        if (root == None):
            return []
        
        nodesWithLevels = self.getNodesInOrderWithLevels(root)

        # Once we have nodes with Levels,
        # We simply have to construct our "answer" list.
        # This is a little annoying, but the basic idea
        # is that every "level" of the tree should be in it's own list.
        # So, every time we're at a new level, we start a new list.
        # Otherwise, we add it to the list of the level we're on.
        ans = []
        for index in range(0, len(nodesWithLevels)):
            num, currentLevel = nodesWithLevels[index]
            if index == 0:
                # start a new list
                ans.append([num])
            else:
                prevNum, prevLevel = nodesWithLevels[index-1] # note the index-1 here.
                if (currentLevel == prevLevel):
                    # add it to the list of the level we're on.
                    ans[-1].append(num)
                else:
                    # start a new list
                    ans.append([num])
        
        return ans
    
    def getNodesInOrderWithLevels(self, root):
        """
        Given the root of a BST, this function returns a list 
        of 2-element tuples, where the first thing in the tuple
        is the number in the BST, and the second thing is the 
        height/level of that number. 
        For example, given the tree:
                     6
                  3     8
                 1 4   7 9
        This function will return:
        [(6,0), (3,1), (8,1), (1,2), (4,2), (7,2), (9,2)]

        It does this by doing BFS and storing the level of 
        each element along the way. 
        """
        ans = []
        queue = collections.deque()
        queue.append((root, 0))
        
        while (len(queue) != 0):

            currentNode, levelOfCurrentNode = queue.popleft()
            ans.append((currentNode.val, levelOfCurrentNode))
            if (currentNode.left != None):
                queue.append((currentNode.left,  levelOfCurrentNode + 1))
            if (currentNode.right != None):
                queue.append((currentNode.right, levelOfCurrentNode + 1))

        return ans