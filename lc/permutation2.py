"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def dfs(self, curr, remaining):
        if not remaining:
            return [curr]

        res, seen = [], set()
        for i in xrange(len(remaining)):
            num = remaining.pop(i)
            if num in seen:
                remaining.insert(i, num)  # backtrack
                continue
            seen.add(num)
            res.extend(self.dfs(curr + [num], remaining))
            remaining.insert(i, num)
        return res

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.dfs([], nums)
