import collections


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # bestDist = float("inf")
        queue = collections.deque()
        visitedBefore = set()
        
        # we should make sure that the top left corner and 
        # bottom right corner are valid places to travel through
        # before we even start the algorithm.
        if (grid[0][0] == 0) and (grid[len(grid)-1][len(grid[0])-1] == 0):
            
            # the first two zeros denote the row and column,
            # the final zero denotes the number of distances
            # in the path from the origin to that coordinate
            queue.append(((0,0),1))
            visitedBefore.add((0,0))
        else:
            return -1
        
        while len(queue) != 0:
            # it's not obvious, 
            # but whenever we reach an element for
            # the first time 
            # print("queue:", queue)
            coordinates, bestDist = queue.popleft()
            currentRow, currentCol = coordinates
            if (currentRow == len(grid)-1) and (currentCol == len(grid[0])-1):
                visitedBefore.add((currentRow, currentCol))
                break

            # top neighbor
            topN = (currentRow-1, currentCol)
            # top right neighbor
            topRightN = (currentRow - 1, currentCol + 1)
            # etc...
            rightN = (currentRow, currentCol + 1)
            bottomRightN = (currentRow + 1, currentCol + 1)
            bottomN = (currentRow + 1, currentCol)
            bottomLeftN = (currentRow+1, currentCol-1)
            leftN = (currentRow, currentCol-1)
            topLeftN = (currentRow-1,currentCol-1)
            potentialNeighbors = [topN, topRightN, rightN, bottomRightN, bottomN, bottomLeftN, leftN, topLeftN]
            for neighbor in potentialNeighbors:
                neighborRow, neighborCol = neighbor
                if self.inGrid(neighbor,grid) and (grid[neighborRow][neighborCol] == 0) and not(neighbor in visitedBefore):
                    queue.append((neighbor, bestDist + 1))
                    visitedBefore.add(neighbor)
        
        if (len(grid)-1, len(grid[0])-1) in visitedBefore:
            return bestDist
        else:
            return -1

            
            

    def inGrid(self, rowColTuple, grid):
        row, col = rowColTuple
        return (row >=0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))

grid = [[0,1],[1,0]]

mySol = Solution()

ans = mySol.shortestPathBinaryMatrix(grid)
print("ans:", ans)