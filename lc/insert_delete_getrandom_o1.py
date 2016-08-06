"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same
probability of being returned.
Example:
"""


import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {} # key is val, value is position in self.vals
        self.vals = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False

        self.vals.append(val)
        self.pos[val] = len(self.vals)-1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        pos = self.pos.get(val, None)
        if pos is None:
            return False

        self.vals.pop(pos)
        del self.pos[val]

        # avoid removal of last element, which would lead to off-by-1 error for pos
        if self.vals and pos < len(self.vals):
            replacement = self.vals.pop()
            self.vals.insert(pos, replacement)
            self.pos[replacement] = pos

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.vals:
            return None

        random_pos = random.randint(0, len(self.vals)-1)
        return self.vals[random_pos]
