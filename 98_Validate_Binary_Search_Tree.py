# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Problem: 
            Given the root of a binary tree,
            return True if the tree is a valid
            binary search tree, and false 
            otherwise.
        Solution:
            To check if the tree is valid, 
            we recursively check if the left
            and right trees are valid. 

            To do this, we pass lists that 
            denote the set of elements that 
            everything in the tree should be less
            than or greater than. For example,
            consider:
                   5
                3     7    
               1 4   6 8
            When we make the recursive call on the 
            subtree with root 3, we pass in a 5
            and tell it "the entire tree should be 
            less than 5". Similarly, when we make the
            recursive call on the subtree with root 7,
            we pass in the 5 and say "the entire tree
            should be greater than 5." 
        """
        return self.isValidBSTHelper(root, [], [])
        

    def isValidBSTHelper(self, node, greaterAncestors, lesserAncestors):
        """
        Note that greaterAncestors is a list of ancestors
        that are supposed to be greater than the current node.

        Similarly, lesserAncestors is a list of ancestors that
        are supposed to be lesser than the current node. 
        """

        # verify the node meets the 
        # requirements of it's ancestors
        for parent in greaterAncestors:
            if node.val >= parent:
                return False
        
        for parent in lesserAncestors:
            if node.val <= parent:
                return False

        # recursively check the left and 
        # right subtrees, if they exist.
        if node.left != None:
            greaterAncestors.append(node.val)
            leftTreeValid = self.isValidBSTHelper(node.left, greaterAncestors, lesserAncestors)
            greaterAncestors.pop()
        else:
            leftTreeValid = True
        
        if node.right != None:
            lesserAncestors.append(node.val)
            rightTreeValid = self.isValidBSTHelper(node.right, greaterAncestors, lesserAncestors)
            lesserAncestors.pop()
        else:
            rightTreeValid = True
        
        return (leftTreeValid and rightTreeValid)