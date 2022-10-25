class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        Problem: 
            Consider an m x n grid 
            of squares, with a robot in
            the top left corner. Suppose
            the robot is trying to reach
            the bottom-right corner, and can 
            only move right or down.
            How many unimque paths are there
            from the top-left corner to the bottom-right?
        Solution:
            This is a pretty straightforward
            recursive problem with a dynamic programming
            solution. Namely, note that we have the 
            following recurrence relationship:
            ans(m,n) = ans(m, n-1) + ans(m-1, n)

            For base cases, note that we have:
            ans(1, n) = 1  and  ans(m, 1) = 1

            With this recursive relationship
            in mind, buildig the DPTable 
            is straightforward. 
        """
        DPTable = []
        
        for row in range(0, m):
            DPTable.append([1])
        
        for col in range(0,n):
            DPTable[0].append(1)
        
        for row in range(1, m):
            for col in range(1,n):
                pathsFromAbove = DPTable[row-1][col]
                pathsFromLeft = DPTable[row][col-1]
                totalPaths = pathsFromAbove + pathsFromLeft
                DPTable[row].append(totalPaths)
        
        return DPTable[m-1][n-1]