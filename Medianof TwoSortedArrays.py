class Solution(object):
    def findKth(self, nums1, nums2, k):
        p = q = 0
        for i in xrange(k-1):
            if p >= len(nums1):
                q += 1
            elif q >= len(nums2):
                p += 1
            elif nums1[p] > nums2[q]:
                q += 1
            else: p += 1
        if p >= len(nums1):
            return nums2[q]
        elif q >= len(nums2):
            return nums1[p]
        else:
            return min(nums1[p], nums2[q])

    def findKth2(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKth2(nums2, nums1)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p1 = min(len(nums1), k/2)
        p2 = k - p1
        if nums1[p1 - 1] < nums2[p2 - 1]:
            return self.findKth2(nums1[p1:], nums2, k - p1)
        elif nums1[p1 - 1] > nums2[p2 - 1]:
            return self.findKth2(nums1, nums2[p2:], k - p2)
        else: return nums1[p1 - 1]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        total = length1 + length2
        if total%2 == 0:
            return (self.findKth(nums1, nums2, total/2) + self.findKth(nums1, nums2, total/2+1))/2.0
        else:
            return self.findKth(nums1, nums2, total/2+1)

s = Solution()
print s.findMedianSortedArrays([], [2, 3])

