"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

class Solution(object):
    def rotate(self, matrix):
        """
        Clockwise rotation:
            1. Reverse column-wise
            2. Swap symmetry over the diagonal
        Counter-clockwise rotation:
            1. Reverse row-wise
            2. Swap symmetry over the diagonal
        """
        def swap(mat, i, j, k, l):
            tmp = mat[i][j]
            mat[i][j] = mat[k][l]
            mat[k][l] = tmp

        rows, cols = len(matrix), len(matrix[0])

        # Reverse column-wise
        for col in xrange(cols):
            for row in xrange(rows/2):
                swap(matrix, row, col, rows-1-row, col)

        # Swap symmetry over the diagonal
        for i in xrange(rows):
            for j in xrange(i+1, cols):
                swap(matrix, i, j, j, i)
