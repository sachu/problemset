"""
https://leetcode.com/problems/partition-list/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes
greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1, head2 = ListNode(None), ListNode(None)
        curr1, curr2 = head1, head2

        curr = head
        while curr:
            if curr.val < x:
                curr1.next = curr
                curr = curr.next
                curr1 = curr1.next
                curr1.next = None
            else:
                curr2.next = curr
                curr = curr.next
                curr2 = curr2.next
                curr2.next = None

        # Connect the two segments
        if head1.next:
            curr1.next = head2.next
            return head1.next

        return head2.next
