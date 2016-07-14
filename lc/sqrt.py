"""
https://leetcode.com/problems/sqrtx/

Implement int sqrt(int x).

Compute and return the square root of x.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while True:
            mid = left + (right - left) / 2 # avoid overflow
            # make sure not to go beyond x because we just return the truncated int of the sqrt
            # avoid overflow, too
            if mid > x / mid:
                right = mid - 1
            elif mid + 1 > x / (mid + 1): # if (mid+1)^2 is greater than x and mid^2 <= x, we've found our result
                return mid
            else:
                left = mid + 1
