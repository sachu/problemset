"""
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# O(k log(k))
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        min_heap = PriorityQueue()
        for node in lists:
            if node: min_heap.put((node.val, node))
        while min_heap.qsize() > 0:
            curr.next = min_heap.get()[1]
            curr = curr.next
            if curr.next: min_heap.put((curr.next.val, curr.next))
        return dummy.next

"""
Exceeds the time limit!
Each min scan is O(k). Worst case is O(k^2)
"""
class SolutionSlow(object):
    def minNode(self, nodes):
        # http://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
        return min(enumerate(nodes), key=lambda pair: pair[1].val)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = filter(lambda listNode : listNode, lists)
        if not lists:
            return None

        listIdx, head = self.minNode(lists)
        curr = head
        lists[listIdx] = curr.next
        if not lists[listIdx]:
            lists.pop(listIdx)

        while lists:
            listIdx, curr.next = self.minNode(lists)
            curr = curr.next
            lists[listIdx] = curr.next
            if not lists[listIdx]:
                lists.pop(listIdx)

        return head

"""
https://discuss.leetcode.com/topic/23140/108ms-python-solution-with-heapq-and-avoid-changing-heap-size/2
def mergeKLists(self, lists):
    from heapq import heappush, heappop, heapreplace, heapify
    dummy = curr = ListNode(0)
    h = [(n.val, n) for n in lists if n]
    heapify(h)
    while h:
        v, n = h[0]
        if n.next is None:
            heappop(h)
        else:
            # Pop and return the smallest item from the heap, and also push the new item
            # heappushpop(a, x) will push x onto a before popping the smallest value
            heapreplace(h, (n.next.val, n.next))
        curr.next = n
        curr = curr.next

    return dummy.next
"""