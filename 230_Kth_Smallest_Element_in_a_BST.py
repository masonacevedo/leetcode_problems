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
        Problem:
            Given the root of a binary search tree,
            and some integer k, return the kth
            smallest element in the tree.
        Solution:
            Perform in-order-traversal
            and return the kth thing you reach. 
        """
        return self.kthSmallestHelper(root, k, [])
    
    def kthSmallestHelper(self, currentNode, k, listSoFar):
        """
        This isn't particularly pretty code, but it basically works as follows:
        Perform an in-order-traversal of the tree, and every time you 
        find the next largest node, add it to the in-order-list of tree values
        that we're building. Once the list has size k, return the last element
        of the list. 
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