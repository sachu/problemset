"""
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionLong(object):

    # Return kth node from start
    def findKth(self, start, k):
        if not start:
            return None

        # assumes k > 0
        kth = start
        for _ in xrange(k-1):
            if kth.next:
                kth = kth.next
            else:
                return None
        return kth

    def reverse(self, start, end):
        # assumes start != end
        prev, curr = start, start.next

        while True:
            next_ = curr.next
            curr.next = prev
            if curr == end:
                break
            prev, curr = curr, next_

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head

        curr, new_head, trail = head, None, None

        while True:
            kth = self.findKth(curr, k)
            if not kth:
                break

            next_ = kth.next # next_ symbolizes the start of the next segment to possibly reverse
            self.reverse(curr, kth)
            if not new_head:
                new_head = kth

            curr.next = next_ # in case the next segment doesn't need to be reversed
            if trail:
                # e.g. 1 2 3 4, k = 2
                # link 1 to 4 between 2->1 and 4->3
                trail.next = kth
            trail = curr
            curr = next_

        if not new_head:
            return head

        return new_head
