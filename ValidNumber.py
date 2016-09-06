import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not len(s): return False

        if s.find('e') == -1:
            return self.check(s, True)
        else:
            return self.check(s[:s.index('e')], True) and self.check(s[(s.index('e')+1):], False)

    def check(self, s, point):
        if len(s) < 1: return False
        i = 0
        num = False
        if s[i] == '+' or s[i] == '-':
            i += 1
        if i == len(s): return False

        while i < len(s) and '0'<=s[i]<='9':
            i += 1
            num = True

        if i < len(s) and point == False:
            return False

        if i < len(s) and s[i] == '.':
            num2 = False
            i += 1
            while i < len(s) and '0'<=s[i]<='9':
                i += 1
                num2 = True

            if num == False and num2 == False:
                return False

        return i == len(s)

    def isNumber2(self, s):
        s = s.strip()
        pat = r'^[+|-]?(\d+\.\d+|\d+\.?|\.\d+)([eE][+|-]?\d+)?$'
        if re.search(pat, s): return True
        else: return False
print Solution().isNumber2('1 ')