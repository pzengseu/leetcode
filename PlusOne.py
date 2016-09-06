class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return []

        result = []
        carry = 1
        digits = [0] + digits

        while digits and carry:
            digit = digits[-1] + carry
            result = [digit%10] + result
            carry = digit / 10
            digits = digits[:-1]

        return digits[1:] + result

    def plusOne2(self, digits):
        if not digits: return []

        digits = [0] + digits
        i = [i for i, d in enumerate(digits) if d < 9][-1]
        return digits[(0<i):i] + [digits[i]+1] + [0]*(len(digits) - i - 1)
