import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        idea:
        Iterate through the grid.
        If you stumble upon a zero, do nothing.
        If you stumble upon a one, then check if you've seen it before.
            If you've seen this particular "1" before, do nothing.
            If you haven't seen this particular "1" before, add 1 to the island count.
            Then, conduct  BFS or DFS to find all the other "1"s that this particular 
            "1" is connected to. While you conduct the BFS/DFS, mark the other 1's you
            see along the way as visited, for future reference. 
        """
        visitedBefore = set()
        islandCount = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if (grid[row][col] == "1") and not((row,col) in visitedBefore):
                    self.BFS(row, col, grid, visitedBefore)
                    # print("i finished BFS:")
                    islandCount += 1
        
        return islandCount

    def BFS(self, row, col, grid, visitedBefore):
        
        queue = collections.deque()
        queue.append((row,col))

        count = 0
        while len(queue) != 0:
            # print("len(queue):", len(queue))
            curRow, curCol = queue.popleft()
            # visitedBefore.add((curRow, curCol))
            # if top neighbor exists, is a 1, and hasn't been visited before, add it to queue!
            if (self.coordinateInGrid(curRow - 1, curCol, grid)) and (grid[curRow-1][curCol] == "1") and not((curRow-1, curCol) in visitedBefore):
                queue.append((curRow-1, curCol))
                visitedBefore.add((curRow-1, curCol))
            if (self.coordinateInGrid(curRow + 1, curCol, grid)) and (grid[curRow+1][curCol] == "1") and not((curRow+1, curCol) in visitedBefore):
                queue.append((curRow+1, curCol))
                visitedBefore.add((curRow +1, curCol))
                # print("curRow-1, curCol:", (curRow-1, curCol))
            if (self.coordinateInGrid(curRow, curCol-1, grid)) and (grid[curRow][curCol-1] == "1") and not((curRow, curCol-1) in visitedBefore):
                queue.append((curRow, curCol-1))
                visitedBefore.add((curRow, curCol-1))
                # print("curRow-1, curCol:", (curRow-1, curCol))
            if (self.coordinateInGrid(curRow, curCol+1, grid)) and (grid[curRow][curCol+1] == "1") and not((curRow, curCol+1) in visitedBefore):
                queue.append((curRow, curCol+1))
                visitedBefore.add((curRow, curCol+1))
                # print("curRow-1, curCol:", (curRow-1, curCol))
            
            count += 1
            # print("visitedBefore:", visitedBefore)
            

    def coordinateInGrid(self, row, col, grid):
        return (row >=0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))

grid = [
["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]

mySol = Solution()
ans = mySol.numIslands(grid)
print("ans:", ans)