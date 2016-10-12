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
        left, right = ListNode(None), ListNode(None)
        left_tail, right_tail = left, right

        while head:
            if head.val < x:
                left_tail.next, head = head, head.next
                left_tail, left_tail.next = left_tail.next, None
            else:
                right_tail.next, head = head, head.next
                right_tail, right_tail.next = right_tail.next, None

        left_tail.next = right.next

        return left.next