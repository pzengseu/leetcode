class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0': return '0'
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)

        num1 = list(reversed(num1))
        num2 = list(reversed(num2))

        for i in xrange(m):
            multiFlag = 0
            addFlag = 0
            for j in xrange(n):
                t1 = int(num1[i]) * int(num2[j]) + multiFlag
                multiFlag = t1 / 10
                t2 = res[i+j] + t1 % 10 + addFlag
                addFlag = t2 / 10
                res[i + j] = t2 % 10

            res[i+n] = res[i+n] + multiFlag + addFlag

        res.reverse()
        if res[0] == 0: res=res[1:]
        res=map(str, res)
        return ''.join(res)