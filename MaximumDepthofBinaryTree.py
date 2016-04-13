# Definition for a binary tree node.
import Queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def create(lists):
    root = None
    if lists.empty():
        return root
    root = TreeNode(lists.get())
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        if not lists.empty():
            l = TreeNode(lists.get())
            node.left = l
            q.put(l)
        if not lists.empty():
            r = TreeNode(lists.get())
            node.right = r
            q.put(r)
    return root

def preOrder(tree):
    if tree:
        print tree.val
        preOrder(tree.left)
        preOrder(tree.right)

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dps2(root)

    def dps(self, root, m):
        if root.left == None and root.right == None: return m
        if root.left == None and root.right != None: return self.dps(root.right, m+1)
        if root.left != None and root.right == None: return self.dps(root.left, m+1)
        return max(self.dps(root.right, m+1),self.dps(root.left, m+1))

    def dps2(self, root):
        if root == None: return 0
        return 1 + max(self.dps2(root.left), self.dps2(root.right))

    def bps(self, root):
        if root == None: return 0
        q = Queue.Queue()
        q.put(root)
        nCount = 1
        nDepth = 0

        while(q):
            node = q.get()
            nCount -= 1

            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)

            if nCount == 0:
                nDepth += 1
                nCount = q.qsize()

        return nDepth

if __name__ == '__main__':
    q = Queue.Queue()
    for i in xrange(6):
        q.put(i)
    tree = create(q)
    # preOrder(tree)

    s = Solution()
    print s.maxDepth(tree)