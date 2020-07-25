# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 
#  👍 679 👎 0

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        cur_p = root
        prev_val = None

        while cur_p or len(stack) != 0:
            while cur_p:
                stack.append(cur_p)
                cur_p = cur_p.left
            visited_node = stack.pop()
            if prev_val is not None:
                if prev_val >= visited_node.val:
                    return False
            prev_val = visited_node.val
            cur_p = visited_node.right
        return True
# leetcode submit region end(Prohibit modification and deletion)
