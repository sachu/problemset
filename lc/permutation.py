"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def dfs(self, curr, remaining):
        if not remaining:
            return [curr]

        permutations = []
        for idx in xrange(len(remaining)):
            num = remaining.pop(idx)
            new_curr = curr + [num]
            permutations.extend(self.dfs(new_curr, remaining))
            remaining.insert(idx, num)
        return permutations

    def permute(self, nums):
        return self.dfs([], nums)
