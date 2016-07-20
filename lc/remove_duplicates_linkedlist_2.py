"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct
numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    # find the first element that doesn't have a duplicate
    def findNonDuplicate(self, node):
        while node and node.next and node.next.val == node.val:
            dupe_val = node.val
            while node and node.val == dupe_val:
                node = node.next
        return node

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curr = head = self.findNonDuplicate(head)
        while curr:
            curr.next = self.findNonDuplicate(curr.next)
            curr = curr.next
        return head
