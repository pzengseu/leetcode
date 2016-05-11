import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retL = ListNode(-1)
        tail = retL
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = l1
                l1 = l1.next
            else:
                tail.next = l2
                tail = l2
                l2 = l2.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return retL.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return []
        n = len(lists)
        temp = lists
        while n > 1:
            tempLists= temp
            temp = []
            for i in xrange(n/2):
                temp.append(self.mergeTwoLists(tempLists[2*i], tempLists[2*i+1]))
            if not n % 2: temp.append(tempLists[-1])
            n = len(temp)
        return temp[0]

    def mergeKLists2(self, lists):
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = pop[1]
            curr = pop[1]
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next
