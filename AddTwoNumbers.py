# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val) + self.next.__str__()

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = 0
        res = l1
        while l1 and l2:
            l1.val = l1.val + l2.val + temp
            temp = l1.val / 10
            l1.val %= 10
            pre = l1
            l1 = l1.next
            l2 = l2.next
        while l1:
            if not temp:
                break
            t = l1.val + temp
            temp = t/10
            pre = l1
            l1.val = t%10
            l1 = l1.next
        if not pre.next: pre.next = l2
        while l2:
            if not temp:
                break
            t = l2.val + temp
            temp = t/10
            l2.val = t%10
            pre = l2
            l2 = l2.next
        if temp:
            pre.next = ListNode(temp)
        return res

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    print res
