"""
https://leetcode.com/problems/3sum/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []
    nums.sort()  # sorting allows us to easily avoid duplicate triplets
    length = len(nums)

    # O(n^2)
    for i in xrange(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # already processed, avoid duplicate triplets
        left = nums[i]
        target = -left  # left + mid + right = 0

        j = i + 1
        k = length - 1
        while j < k:
            if j > i + 1 and nums[j] == nums[j - 1]:  # similar check to above, avoid duplicates
                j += 1
                continue
            if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                k -= 1
                continue

            mid, right = nums[j], nums[k]
            pair_sum = mid + right
            if pair_sum == target:
                ans.append([left, mid, right])
                j += 1
                k -= 1
            elif pair_sum < target:
                j += 1
            else:
                k -= 1
    return ans


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
