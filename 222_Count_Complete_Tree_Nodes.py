# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Problem:
            Given a complete tree, count the total number of nodes in the tree.
            Must run faster than O(n) time.
        
        Solution:
            We are given a complete tree, which gives us a lot of information.
            We know that a complete tree only has nodes missing on the bottom
            level. So, all we have to do is figure out how many nodes are on the
            bottom level, then add the total number of nodes on previous levels 
            (which is 2^(height-1)-1), and we'll have our answer. 

            The hard part is, how do we figure out the number of 
            nodes on the bottom level quickly? Note that the 
            "straightforward" thing to do, i.e. iterate
            along the bottom level of the tree until 
            it stops is, in the worst case, O(n), because
            ~n/2 of the nodes in the tree can be on that bottom
            level.

            So, to figure out the number of nodes on the 
            bottom level quickly, we use binary search!

            Suppose the tree has height H.
            Consider the path to the (H-1)th level of the tree 
            given by L,L,L...,L. This takes us to the LEFTMost 
            element on the H-1 level. Similarly, the path
            R,R,R,R.... R gets us to the rightmost path on the 
            H-1 level. In the "general" case, we'll be able
            to tell that the leftmost path is too far to the
            left of the tree because the nodes on the H-1 level
            have children. On the other hand, the rightmost nodes
            on the H-1 level have no children, so we know those 
            are too far to the right. 

            We know that LLL...L is too far left, and RRR...R is 
            too far right. So, find the path between those that is 
            right in the middle. Then, we can look at
            the H-1 level node on that middle path, and check if 
            it has children. If it has two children, it's too far 
            to the left. If it has no children, it's too far to
            the right. If it has just 1 child, we're in just
            the right place! This is how we do the binary search.

            Finally, once this process terminates, and we have 
            identified the node on the H-1 level whose children
            are the right-most nodes on the H level, we can 
            simply look at the position of the node in the tree,
            and see how many nodes are on that bottom level. 

            Finally, notice that the path to 
            the leftmost element on the bottom 
            layer is always LLLL..LLL. The 
            element immediately to it's right 
            is given by LLLL...LLR. The element 
            to it's right is:
            LLLL....LRL.
            In general, we have the following 
            pattern:
            LLL...LLL
            LLL...LLR
            LLL...LRL
            LLL...LRR
            LLL...RLL
            LLL...RLR
            LLL...RRL
            LLL...RRR

            Each path just corresponds to a number
            in binary! So the rightmost path can be
            thought of as the binary number
            111...111
            and the leftmost path can be thought
            of as 
            000...000
            and this makes it extremely easy 
            to find the path exactly in the middle of them! 
        """
        # base cases
        if root is None:
            return 0
        elif (root.left is None) and (root.right is None):
            return 1
        elif (root.left is not None) and (root.right is None):
            return 2
        
        # If our complete tree has a full bottom level,
        # it's easy to compute the number of nodes.
        lHeight = self.getLeftHeight(root)
        rHeight = self.getRightHeight(root)
        if lHeight == rHeight:
            return ((2**lHeight)-1)
        
        rightPath = (2**(rHeight-1))-1
        leftPath = 0

        previousLevelsCount = (2**rHeight)-1
        

        # this could technically be 
        # while (True):
        # but just in case we get a bad input...
        count = 0
        while count < 1000:
            count += 1


            middlePath = (leftPath + rightPath)//2
            middlePathString = self.pathToString(middlePath, rHeight - 1)
            node = self.navigate(root, middlePathString)

            if (node.left is None) and (node.right is None):
                immediateLeftPath = middlePath - 1
                immediateLeftString = self.pathToString(immediateLeftPath, rHeight - 1)
                imLeftNode = self.navigate(root, immediateLeftString)

                if (imLeftNode.left is not None) and (imLeftNode.right is not None):
                    currentLevelCount = 2*(immediateLeftPath+1)
                    return previousLevelsCount + currentLevelCount
                else:
                    rightPath = middlePath
            
            elif (node.left is not None) and (node.right is not None):
                immediateRightPath = middlePath + 1
                immediateRightString = self.pathToString(immediateRightPath, rHeight - 1)
                imRightNode = self.navigate(root, immediateRightString)
                if (imRightNode.left is None) and (imRightNode.right is None):
                    currentLevelCount = 2*(immediateRightPath)
                    return previousLevelsCount + currentLevelCount
                else:
                    leftPath = middlePath+1
            
            elif (node.left is not None) and (node.right is None):
                currentLevelCount = (2*middlePath) + 1
                return previousLevelsCount + currentLevelCount
        

    def pathToString(self, num, targetLength):
        """
        Given a base 10 number (num), this function
        converts it to a binary string with a
        certain amount of leading zeros in the 
        front, as specified by targetLength. 
        """
        s = bin(num)[2:]
        s = "0"*(targetLength-len(s)) + s
        return s

    def navigate(self, root, path):
        """
        Given a path, a series of 0s and 1s, which 
        corresponds to Lefts and Rights, this 
        function navigates down some binary tree 
        to the bottom, as specified by the path.
        """
        currentNode = root
        for step in path:
            if step == "0":
                currentNode = currentNode.left
            elif step == "1":
                currentNode = currentNode.right
        return currentNode


    # These functions aren't super DRY, but
    # they're pretty clean and simple enough...
    def getLeftHeight(self,root):
        """
        Given the root of a tree, this function
        navigates down the left side of the
        tree and retuns the height it finds.
        """
        if root.left is None:
            return 1
        else:
            return 1 + self.getLeftHeight(root.left)

    def getRightHeight(self,root):
        """
        Given the root of a tree, this function
        navigates down the right side of the
        tree and retuns the height it finds.
        """
        if root.right is None:
            return 1
        else:
            return 1 + self.getRightHeight(root.right)