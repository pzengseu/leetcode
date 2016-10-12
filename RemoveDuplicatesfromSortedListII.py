# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode('x')
        h.next = head

        if not head: return head

        pre = h
        current = h.next

        while current and current.next:
            next = current.next
            if next.val != current.val:
                pre = current
                current = next
            else:
                while next and next.val == current.val:
                    next = next.next
                pre.next = next
                current = next

        return h.next

