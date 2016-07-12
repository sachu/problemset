"""
https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix
in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []

        if len(matrix) == 0:
            return res

        row_begin, row_end = 0, len(matrix)-1
        col_begin, col_end = 0, len(matrix[0])-1

        while row_begin <= row_end and col_begin <= col_end:
            # right
            for col in xrange(col_begin, col_end+1):
                res.append(matrix[row_begin][col])
            row_begin += 1

            # down
            for row in xrange(row_begin, row_end+1):
                res.append(matrix[row][col_end])
            col_end -= 1

            # left
            # without this check, we could be double-adding items
            if row_begin <= row_end:
                for col in xrange(col_end, col_begin-1, -1):
                    res.append(matrix[row_end][col])
                row_end -= 1

            # up
            if col_begin <= col_end:
                for row in xrange(row_end, row_begin-1, -1):
                    res.append(matrix[row][col_begin])
                col_begin += 1

        return res
