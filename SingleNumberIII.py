import operator

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, filter(lambda x:x&xor&-xor, nums))
        return [ans, xor^ans]

s=Solution()
print s.singleNumber([1, 2, 1, 3, 2, 5])