import collections


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Problem:
            Given a grid/matrix of 1s and 0s, 
            find the shortest path from the top-left
            corner to the bottom-right corner,
            under the restriction that you may only
            pass through entries of the grid/matrix
            that are zero. 
            Return the number of nodes in that path. 
            If there is no such path, return -1. 
        Solution:
            Do BFS, starting from the top-left,
            until you reach the bottom-right. Keep
            track of how many steps it took to 
            get from the top-left to bottom-right, and 
            return that. 

            Note that we don't need to 
            do djikstra's algorithm or anything like
            that, because this problem is basically
            a graph where all the edges have equal weight.
            In fact, djikstra's algorithm can be understood
            to be a generalization of BFS. 
        """
        queue = collections.deque()
        visitedBefore = set()
        
        # we should make sure that the top left corner and 
        # bottom right corner are valid places to travel through
        # before we even start the algorithm.
        if (grid[0][0] == 0) and (grid[len(grid)-1][len(grid[0])-1] == 0):    
            queue.append(((0,0),1))
            visitedBefore.add((0,0))
        else:
            return -1
        
        while len(queue) != 0:

            coordinates, bestDist = queue.popleft()
            currentRow, currentCol = coordinates
            if (currentRow == len(grid)-1) and (currentCol == len(grid[0])-1):
                visitedBefore.add((currentRow, currentCol))
                break

            topNeighbor = (currentRow-1, currentCol)
            topRightNeighbor = (currentRow - 1, currentCol + 1)
            rightNeigbor = (currentRow, currentCol + 1)
            bottomRightNeighbor = (currentRow + 1, currentCol + 1)
            bottomNeighbor = (currentRow + 1, currentCol)
            bottomLeftNeigbor = (currentRow+1, currentCol-1)
            leftNeighbor = (currentRow, currentCol-1)
            topLeftNeighbor = (currentRow-1,currentCol-1)
            potentialNeighbors = [
                topNeighbor, topRightNeighbor, 
                rightNeigbor, bottomRightNeighbor, 
                bottomNeighbor, bottomLeftNeigbor, 
                leftNeighbor, topLeftNeighbor]
    
            for neighbor in potentialNeighbors:
                neighborRow, neighborCol = neighbor
                if self.inGrid(neighbor,grid) and \
                    grid[neighborRow][neighborCol] == 0 and \
                    not(neighbor in visitedBefore):
                    # if neighbor is in the grid, is a 0, and 
                    # hasn't been visited before, we add it to 
                    # the queue. 
                    queue.append((neighbor, bestDist + 1))
                    visitedBefore.add(neighbor)
        
        # if bottomRight corner has been visited, 
        # return the distance we found.
        if (len(grid)-1, len(grid[0])-1) in visitedBefore:
            return bestDist
        else: # otherwise, return -1. 
            return -1

            
    def inGrid(self, rowColTuple, grid):
        row, col = rowColTuple
        return (row >=0) and (row < len(grid)) and (col >= 0) and (col < len(grid[0]))