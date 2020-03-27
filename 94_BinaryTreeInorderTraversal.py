# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        inorder_list = []
        p = root

        while p or len(stack) != 0:
            while p:
                stack.append(p)
                p = p.left
            temp_p = stack.pop()
            inorder_list.append(temp_p.val)
            p = temp_p.right
        return inorder_list
