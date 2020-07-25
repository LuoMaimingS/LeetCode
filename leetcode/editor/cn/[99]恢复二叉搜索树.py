# 二叉搜索树中的两个节点被错误地交换。 
# 
#  请在不改变其结构的情况下，恢复这棵树。 
# 
#  示例 1: 
# 
#  输入: [1,3,null,null,2]
# 
#    1
#   /
#  3
#   \
#    2
# 
# 输出: [3,1,null,null,2]
# 
#    3
#   /
#  1
#   \
#    2
#  
# 
#  示例 2: 
# 
#  输入: [3,1,4,null,null,2]
# 
#   3
#  / \
# 1   4
#    /
#   2
# 
# 输出: [2,1,4,null,null,3]
# 
#   2
#  / \
# 1   4
#    /
#   3 
# 
#  进阶: 
# 
#  
#  使用 O(n) 空间复杂度的解法很容易实现。 
#  你能想出一个只使用常数空间的解决方案吗？ 
#  
#  Related Topics 树 深度优先搜索 
#  👍 252 👎 0
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        cur_p = root
        prev_node = None
        node_x = None
        node_y = None

        while cur_p or len(stack) != 0:
            while cur_p:
                stack.append(cur_p)
                cur_p = cur_p.left
            visited_node = stack.pop()
            if prev_node is not None:
                if prev_node.val >= visited_node.val:
                    node_y = visited_node
                    if node_x is None:
                        node_x = prev_node
            prev_node = visited_node
            cur_p = visited_node.right

        temp_val = node_x.val
        node_x.val = node_y.val
        node_y.val = temp_val
        
# leetcode submit region end(Prohibit modification and deletion)
