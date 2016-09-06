class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        isUsed = [False] * (n + 1)
        data = [1] * n
        for i in xrange(1, n):
            data[i] = data[i - 1] * i

        res = ''
        k -= 1
        for i in range(n)[::-1]:
            rank = k / data[i]
            j = 0
            while j <= rank:
                if isUsed[j]: rank += 1
                j += 1
            isUsed[rank] = True
            res += str(j)
            k = k % data[i]

        return res

print Solution().getPermutation(3, 6)



