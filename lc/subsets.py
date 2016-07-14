"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def dfs(self, nums, curr, start, size):
        if size == 0:
            return [curr]
        res = []
        for i in xrange(start, len(nums)-size+1):
            res.extend(self.dfs(nums, curr + [nums[i]], i+1, size-1))
        return res

    def subsets(self, nums):
        if not nums:
            return [[]]
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[], nums]
        for size in xrange(1, len(nums)):
            res.extend(self.dfs(nums, [], 0, size))
        return res
