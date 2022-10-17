# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        Problem: 
            Given two binary search trees,
            return True if all their values 
            and structure are the same,
            and return False otherwise.
        Solution:
            Two trees are the same 
            if and only if:
            1. Their root values are the same.
            2. Their left subtrees are the same.
            3. Their right subtrees are the same.
            This is very nice to implement recursively.
        """
        # Base cases. 
        if (p == None) and (q == None):
            return True
        elif (p == None) or (q == None): # one of p or q is None BUT the other isn't none. 
            return False

        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)