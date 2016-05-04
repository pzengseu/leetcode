#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = head
        totalNums = 0
        while head:
            totalNums += 1
            head = head.next

        head = h.next
        pre = h
        if n == totalNums:
            return h.next
        i = 1
        while head:
            if i == totalNums - n:
                pre.next = head.next
                return h
            i += 1
            pre = head
            head = head.next

    def removeNthFromEnd2(self, head, n):
        newHead = ListNode(-1)
        newHead.next = head
        point1 = newHead
        point2 = newHead
        for i in xrange(n):
            point2 = point2.next
        while point2.next:
            point2 = point2.next
            point1 = point1.next
        point1.next = point1.next.next
        return newHead.next

    def remove(self, node, n):
        if node.next == None: return 1
        level = self.remove(node.next, n) + 1
        if level == n+1:
            node.next = node.next.next
        return level

    def removeNthFormEnd3(self, head, n):
        newHead = ListNode(-1)
        newHead.next = head
        self.remove(newHead, n)
        return newHead.next