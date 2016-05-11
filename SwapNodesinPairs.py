# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head
        curr = h
        a = ListNode(-1)
        b = ListNode(-1)
        while curr.next and curr.next.next:
            a = curr.next
            b = curr.next.next
            a.next = b.next
            b.next = a
            curr.next = b
            curr = a
        return h.next

    def swapPairs(self, head):
        if not head: return None
        if not head.next: return head

        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head

        return temp
