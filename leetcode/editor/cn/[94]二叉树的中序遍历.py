# 给定一个二叉树，返回它的中序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 591 👎 0

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        cur_p = root
        traversal_list = []

        while (cur_p is not None) or (len(stack) > 0):
            while cur_p is not None:
                stack.append(cur_p)
                cur_p = cur_p.left
            cur_p = stack[-1]
            del stack[-1]
            traversal_list.append(cur_p.val)
            cur_p = cur_p.right
        return traversal_list


# leetcode submit region end(Prohibit modification and deletion)
