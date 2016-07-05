"""
https://leetcode.com/problems/3sum-closest/

Given an array S of n integers, find three integers in S such that the sum is closest to a given
number, target. Return the sum of the three integers. You may assume that each input would have
exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def three_sum_closest(nums, target):
    nums.sort()
    length = len(nums)
    closest = float('inf')
    for i in xrange(length - 2):
        left = nums[i]
        j, k = i + 1, length - 1
        while j < k:
            mid, right = nums[j], nums[k]
            sum_ = left + mid + right
            if abs(target - sum_) < abs(target - closest):
                closest = sum_
            if sum_ < target:
                j += 1
            else:
                k -= 1
    return closest
