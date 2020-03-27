# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack = [root]
        reverse_postorder_list = []

        while len(stack) != 0:
            p = stack.pop()
            reverse_postorder_list.append(p.val)
            if p.left: stack.append(p.left)
            if p.right: stack.append(p.right)

        return reverse_postorder_list[::-1]



