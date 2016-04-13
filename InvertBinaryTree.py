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
    else:
        print "NULL"

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Iterative Solution
        """
        if not root: return root
        pre = root
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            temp = q.get()
            if temp.left:
                q.put(temp.left)
            if temp.right:
                q.put(temp.right)
            temp.left, temp.right = temp.right, temp.left
        return pre

    def execute(self, root):
        #recursive
        if root == None: return
        if root.left != None or root.right != None:
            root.left, root.right = root.right, root.left
        self.execute(root.left)
        self.execute(root.right)


if __name__ == '__main__':
    q = Queue.Queue()
    for i in xrange(1,3):
        q.put(i)
    tree = create(q)
    tree.right = tree.left
    tree.left = None
    preOrder(tree)
    print '---'
    s = Solution()
    s.invertTree(tree)
    preOrder(tree)