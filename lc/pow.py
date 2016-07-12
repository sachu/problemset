# https://leetcode.com/problems/powx-n/
# Implement pow(x, n).


class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            n = abs(n)
            x = 1. / x

        if (n % 2) == 0:
            return pow(x * x, n / 2)
        return x * pow(x * x, n / 2)
