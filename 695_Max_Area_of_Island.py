import collections
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
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
        
        queue = collections.deque()
        queue.append((row,col))
        visitedBeforeSearch = len(visitedBefore)
        print("visitedBefore:", visitedBefore)
        while len(queue) != 0:
            
            curRow, curCol = queue.popleft()
            visitedBefore.add((curRow, curCol))
            # if top neighbor exists, is a 1, and hasn't been visited before, add it to queue!
            if (self.coordinateInGrid(curRow - 1, curCol, grid)) and (grid[curRow-1][curCol] == 1) and not((curRow-1, curCol) in visitedBefore):
                queue.append((curRow-1, curCol))
                visitedBefore.add((curRow-1, curCol))

            if (self.coordinateInGrid(curRow + 1, curCol, grid)) and (grid[curRow+1][curCol] == 1) and not((curRow+1, curCol) in visitedBefore):
                queue.append((curRow+1, curCol))
                visitedBefore.add((curRow +1, curCol))

            if (self.coordinateInGrid(curRow, curCol-1, grid)) and (grid[curRow][curCol-1] == 1) and not((curRow, curCol-1) in visitedBefore):
                queue.append((curRow, curCol-1))
                visitedBefore.add((curRow, curCol-1))

            if (self.coordinateInGrid(curRow, curCol+1, grid)) and (grid[curRow][curCol+1] == 1) and not((curRow, curCol+1) in visitedBefore):
                queue.append((curRow, curCol+1))
                visitedBefore.add((curRow, curCol+1))
        print("visitedBefore:", visitedBefore)
        visitedAfterSearch = len(visitedBefore)
        return visitedAfterSearch - visitedBeforeSearch
    
    def coordinateInGrid(self, row, col, grid):
        return (row >=0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))

grid = [[0,1]]

mySol = Solution()
ans = mySol.maxAreaOfIsland(grid)
print("ans:", ans)