import collections
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
            Problem: 
                Given a grid of 1s and 0s, 
                where each 1 represents a square mile of land,
                and each 0 represents a square mile of ocean, 
                return the number of islands in the grid. 
            Idea:
                Iterate through the grid.
                If you stumble upon a zero, do nothing.
                If you stumble upon a one, then check if you've seen it before.
                    If you've seen this particular "1" before, do nothing.
                    If you haven't seen this particular "1" before, add 1 to the island count.
                    Then, conduct  BFS or DFS to find all the other "1"s that this particular 
                    "1" is connected to. While you conduct the BFS/DFS, mark the other 1's you
                    see along the way as visited, so you know not to BFS them later. 
        """
        visitedBefore = set()
        islandCount = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if (grid[row][col] == "1") and not((row,col) in visitedBefore):
                    self.BFS(row, col, grid, visitedBefore)
                    islandCount += 1
        
        return islandCount

    def BFS(self, row, col, grid, visitedBefore):
        """
        Implements BFS, starting from a specific location on 
        grid. Specifically, it starts from the "1" located at 
        position (row, col) (this position is guaranteed to be a "1"
        because of the conditions under which this function is called.)
        and marks all the "1"s connected to it as visited. 
        """

        queue = collections.deque()
        queue.append((row,col))
        while len(queue) != 0:
            curRow, curCol = queue.popleft()

            # Get all the neighbors of the current element
            topNeighbor = (curRow - 1, curCol)
            rightNeighbor = (curRow, curCol + 1)
            bottomNeighbor = (curRow + 1, curCol)
            leftNeighbor = (curRow, curCol - 1)
            neighbors = [topNeighbor, rightNeighbor, leftNeighbor, bottomNeighbor]

            # For each neighbor, check if it's even in the grid,
            # if it's a piece of land, and hasn't been visited before.
            # If all three are satisfied, add it to the queue and mark as visited.
            for neighbor in neighbors:
                if self.coordinateInGrid(neighbor, grid) and \
                        self.isOne(neighbor, grid) and \
                        not(neighbor in visitedBefore):
                    queue.append(neighbor)
                    visitedBefore.add(neighbor)

    def coordinateInGrid(self, coordinates, grid):
        row, col = coordinates
        return (row >=0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))

    def isOne(self, coordinates, grid):
        row, col = coordinates
        return grid[row][col] == "1"

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