"""
https://leetcode.com/problems/walls-and-gates/

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you
may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it
should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""


class Solution(object):
    def bfs(self, rooms, x, y, dist):
        rows, cols = len(rooms), len(rooms[0])
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return

        if dist > 0 and rooms[x][y] <= dist: # already processed a shorter distance
            return

        rooms[x][y] = dist
        self.bfs(rooms, x+1, y, dist+1)
        self.bfs(rooms, x-1, y, dist+1)
        self.bfs(rooms, x, y+1, dist+1)
        self.bfs(rooms, x, y-1, dist+1)

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        for x in xrange(rows):
            for y in xrange(cols):
                if rooms[x][y] == 0: # gate
                    self.bfs(rooms, x, y, 0)
