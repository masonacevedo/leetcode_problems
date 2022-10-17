import collections
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
            Problem: 
                Given a grid of 1s and 0s, 
                where each 1 represents a square mile of land,
                and each 0 represents a square mile of ocean, 
                return the size of the biggest island. 
            Solution:
                Iterate through the grid.
                If you stumble upon a zero, do nothing.
                If you stumble upon a one, then check if you've seen it before.
                    If you've seen this particular "1" before, do nothing.
                    If you haven't seen this particular "1" before, use BFS/DFS
                    to compute the size of the island, while marking pieces of 
                    land as "seen before." 
        """
        
        biggestIslandSoFar = 0
        currentIslandSize = 0
        visitedBefore = set()
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if (grid[row][col] == 1) and not((row,col) in visitedBefore):
                    
                    currentIslandSize = self.getIslandSize(row, col, grid, visitedBefore)
                    biggestIslandSoFar = max(biggestIslandSoFar, currentIslandSize)
        
        return biggestIslandSoFar
    
    def getIslandSize(self, row, col, grid, visitedBefore):
        """
        To get the size of an island, we do the following:
        Save the number of "1"s we've visited before doing BFS
        Do BFS, and mark all visited nodes as visited.
        Compare the number of visited nodes now to what 
        we saved before, and return the difference. 
        """
        queue = collections.deque()
        queue.append((row,col))
        visitedBeforeSearch = len(visitedBefore)
        while len(queue) != 0:
            
            curRow, curCol = queue.popleft()
            visitedBefore.add((curRow, curCol))

            topNeighbor = (curRow - 1, curCol)
            rightNeighbor = (curRow, curCol + 1)
            bottomNeighbor = (curRow + 1, curCol)
            leftNeighbor = (curRow, curCol - 1)
            neighbors = [
                topNeighbor, bottomNeighbor,
                leftNeighbor, rightNeighbor]
            
            for neighbor in neighbors:
                if self.coordinateInGrid(neighbor, grid)\
                    and self.isOne(neighbor, grid) \
                    and not(neighbor in visitedBefore):
                    queue.append(neighbor)
                    visitedBefore.add(neighbor)

        visitedAfterSearch = len(visitedBefore)
        return (visitedAfterSearch - visitedBeforeSearch)
    
    def isOne(self, coordinates, grid):
        row, col = coordinates
        return grid[row][col] == 1
    def coordinateInGrid(self, coordinates, grid):
        row, col = coordinates
        return (row >=0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))