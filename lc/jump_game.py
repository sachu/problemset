"""
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index
of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        if not nums:
            return True
        end = len(nums) - 1
        reach = nums[0]
        i = 1
        while i <= reach < end:
            reach = max(reach, i + nums[i])
            i += 1
        return reach >= end


class SolutionRecursive(object):
    def dfs(self, nums, idx, seen):
        if idx >= len(nums) - 1:
            return True

        if idx in seen:
            return False
        seen.add(idx)

        for steps in xrange(nums[idx], 0, -1):
            if self.dfs(nums, idx + steps, seen):
                return True
        return False

    def canJump(self, nums):
        return self.dfs(nums, 0, set())
