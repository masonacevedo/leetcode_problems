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
        Idea here is pretty simple:
        Do breadth first search, and make sure that 
        all the nodes on the same level are part of 
        the same sub list. 
        """
        if (root == None):
            return []
        preAns = []
        
        queue = collections.deque()
        queue.append([root, 0])
        
        while (len(queue) != 0):
            currentNode, levelOfCurrentNode = queue.popleft()
            
            if (len(preAns) == 0):
                preAns.append([currentNode.val, levelOfCurrentNode])
            else:
                # If the current Node is on the same
                # level as the last thing in the list,
                # then add it in the same sublist. If not,
                # then make it it's own list.
                if (levelOfCurrentNode == preAns[-1][-1]):
                    preAns.append([currentNode.val, levelOfCurrentNode])
                else:
                    preAns.append([currentNode.val, levelOfCurrentNode])
                # preAns.append(currentNode.val)
            if (currentNode.left != None):
                queue.append([currentNode.left,  levelOfCurrentNode + 1])
            if (currentNode.right != None):
                queue.append([currentNode.right, levelOfCurrentNode + 1])
            
        ans = []
        for index in range(0, len(preAns)):
            num, level = preAns[index]
            if index == 0:
                ans.append([num])
            else:
                prevNum, prevLevel = preAns[index-1]
                if (level == prevLevel):
                    ans[-1].append(num)
                else:
                    ans.append([num])
        
        return ans