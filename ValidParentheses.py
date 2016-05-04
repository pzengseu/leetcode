import Queue

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        containChars = {'(':0, ')':1, '{':4, '}':5, '[':8, ']':9}
        stack = Queue.LifoQueue()
        for i in xrange(len(s)):
            if containChars[s[i]] % 2:
                if stack.empty() or containChars[s[i]] != containChars[stack.get()] + 1: return False
                continue
            stack.put(s[i])
        if stack.empty(): return True
        return False

print Solution().isValid("([])")