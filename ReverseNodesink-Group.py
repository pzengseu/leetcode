# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        n = 0
        curr = head
        while curr:
            n += 1
            if n >= k: break
            curr = curr.next
        if k > n: return head
        curr = head
        node = None
        for i in xrange(k):
            nxt = curr.next
            curr.next = node
            node = curr
            curr = nxt
        head.next = self.reverseKGroup(curr, k)

        return node

    def reverseKGroup2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        vals = []
        h = head
        while h:
            vals.append(h.val)
            h = h.next
        print vals
        h = head
        for i in xrange(len(vals)/k):
            for j in xrange(k):
                h.val = vals[i*k:(i+1)*k][::-1][j]
                h = h.next
        return head

    def reverseKGroup3(self, head, k):
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        if n < k:
            return head

        pre = ListNode(-1)
        ret = pre
        node = ListNode(-1)
        rem = ListNode(-1)

        for i in xrange(n / k):
            node = None
            rem = head
            for j in xrange(k):
                nxt = head.next
                head.next = node
                node = head
                head = nxt
            pre.next = node
            rem.next = head
            pre = rem

        return ret.next
