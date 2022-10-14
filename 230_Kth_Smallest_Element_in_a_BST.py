# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.kthSmallestHelper(root, k, [])
    
    def kthSmallestHelper(self, currentNode, k, listSoFar):
        """
        This isn't particularly pretty code, but it basically works as follows:
        Perform an in-order-traversal of the tree, and every time you 
        find the next largest node, add it to the in-order-list of tree values
        that we're building. Every time you add an element to the list,
        check to see if the length of the list is k. If so, then return
        the last element in the list. 
        """
        if len(listSoFar) == k:
            return listSoFar[-1]
        else:
            if (currentNode.left != None):
                self.kthSmallestHelper(currentNode.left, k, listSoFar)

            if (len(listSoFar) == k):
                return listSoFar[-1]

            listSoFar.append(currentNode.val)

            if (len(listSoFar) == k):
                return listSoFar[-1]

            if (currentNode.right != None):
                self.kthSmallestHelper(currentNode.right, k, listSoFar)

            if (len(listSoFar) == k):
                return listSoFar[-1]

