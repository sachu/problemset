"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a digit string, return all possible letter combinations that the number could represent.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):

    mapping = {
        "0" : [' '],
        "1" : ['*'],
        "2" : ['a', 'b', 'c'],
        "3" : ['d', 'e', 'f'],
        "4" : ['g', 'h', 'i'],
        "5" : ['j', 'k', 'l'],
        "6" : ['m', 'n', 'o'],
        "7" : ['p', 'q', 'r', 's'],
        "8" : ['t', 'u', 'v'],
        "9" : ['w', 'x', 'y', 'z'],
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        front, rest = digits[0], digits[1:]
        front_chars = self.mapping[front]

        remaining_combos = self.letterCombinations(rest)
        if not remaining_combos:
            return list(front_chars)

        combos = []
        for ch in front_chars:
            combos.extend([ch + r_combo for r_combo in remaining_combos])
        return combos
