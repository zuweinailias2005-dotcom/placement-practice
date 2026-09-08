root = [1,2,2,3,4,4,3]

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def mirror(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return mirror(left.left,right.right) and mirror(left.right,right.left)
        return mirror(root.left,root.right)
        