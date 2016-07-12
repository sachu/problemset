"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations
in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, 0, target, res, [])
        return res

    def dfs(self, candidates, startIdx, target, res, currPath):
        if target < 0:
            return
        if target == 0:
            res.append(currPath)
            return

        seen = set()
        for i in xrange(startIdx, len(candidates)):
            num = candidates[i]
            # Avoid duplicate combinations.
            # e.g. currPath = [1]. Now we want to extend this currPath. If num is 1, we
            # try out [1,1]. But if the next num is also 1, we don't need to process it.
            if num in seen:
                continue
            seen.add(num)
            self.dfs(candidates, i+1, target-num, res, currPath + [num])
