"""
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater
permutation of numbers. If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in
the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        Iterate starting from the right-most digit. If we encounter a smaller left neighbor X,
        swap X with the smallest number on its right that is still greater than X. Then sort
        the remaining numbers.

        1234: Start at 4. 3 is smaller than 4, so swap 3 with the smallest number in [4] that
              is greater than 3. The remaining is the sorted order of [3]
        1243: 4 is greater than 2. Swap 2 with the smallest number in [3, 4] that is greater than 2.
              The remaining is the sorted order of [2, 4]
        1324: 4 is greater than 2.
        1342: 4 is greater than 3, swap 3 with the smallest number in [2, 4] that is greater than 3.
              Remainder is sorted order of [2, 3]
        1423: 3 is greater than 2.
        1432: 4 is greater than 1, swap 1 with smallest number in [2, 3, 4] that is greater than 1.
              Remainder is sorted order of [1, 3, 4]
        2134

        """
        if not nums:
            return

        modified = False
        for i in xrange(len(nums)-2, -1, -1):
            nums_i = nums[i]
            if nums_i < nums[i+1]:
                modified = True
                right_nums = nums[i+1:]
                replacement = min([n for n in right_nums if n > nums_i])
                right_nums.remove(replacement)
                nums[i] = replacement

                right_nums = sorted(right_nums + [nums_i])
                for j in xrange(len(right_nums)):
                    nums[i+1+j] = right_nums[j]
                break

        if not modified:
            # e.g. nums is 4321, so reverse
            nums.reverse()
