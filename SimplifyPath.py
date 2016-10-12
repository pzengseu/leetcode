import Queue

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = Queue.LifoQueue()
        dir = path.split('/')
        skip = set(('..', '', '.'))
        res = ''

        for s in dir:
            if s not in skip:
                stack.put(s)
            elif s == '..' and not stack.empty():
                stack.get()

        while not stack.empty():
            res = '/' + stack.get() + res

        return res if res else '/'

print Solution().simplifyPath("/a/./b/../../c/")
