class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = 0
        res = []
        i = len(a) - 1
        j = len(b) - 1

        while i>=0 or j >= 0:
            if i>=0: sum += int(a[i])
            if j>=0: sum += int(b[j])
            res.append(str(sum&1))
            sum = (sum>>1)&1
            i -= 1
            j -= 1

        if sum: res.append(str(sum))
        return ''.join(reversed(res))

print Solution().addBinary('11', '1')
