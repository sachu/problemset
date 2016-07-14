"""
https://leetcode.com/problems/unique-paths-ii/

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""


class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        endRow, endCol = rows-1, cols-1
        if rows == 0 or cols == 0 or obstacleGrid[endRow][endCol] == 1:
            return 0

        # Start counting back from the end
        obstacleGrid[endRow][endCol] = 1
        way = 1
        for col in xrange(cols-2, -1, -1):
            print way
            if obstacleGrid[endRow][col] == 1:
                obstacleGrid[endRow][col] = 0
            else:
                way &= obstacleGrid[endRow][col+1]
                obstacleGrid[endRow][col] = way

        way = 1
        for row in xrange(rows-2, -1, -1):
            if obstacleGrid[row][endCol] == 1:
                obstacleGrid[row][endCol] = 0
            else:
                way &= obstacleGrid[row+1][endCol]
                obstacleGrid[row][endCol] = way

        for row in xrange(rows-2, -1, -1):
            for col in xrange(cols-2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row+1][col] + obstacleGrid[row][col+1]

        return obstacleGrid[0][0]

# This problem is O(2^(rows + cols)). The problem is the lack of caching
# already processed computations.
class SolutionSlow(object):
    def dfs(self, obstacleGrid, position, goal):
        x, y = position
        if x >= len(obstacleGrid) or y >= len(obstacleGrid[0]) or \
            obstacleGrid[x][y] == 1:
            return 0

        if position == goal:
            return 1

        return self.dfs(obstacleGrid, (x+1, y), goal) + self.dfs(obstacleGrid, (x, y+1), goal)

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        goal = (rows-1, cols-1)
        return self.dfs(obstacleGrid, (0,0), goal)
