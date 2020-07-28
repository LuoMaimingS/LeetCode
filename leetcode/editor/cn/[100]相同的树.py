# 给定两个二叉树，编写一个函数来检验它们是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  示例 1: 
# 
#  输入:       1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# 
# 输出: true 
# 
#  示例 2: 
# 
#  输入:      1          1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# 输出: false
#  
# 
#  示例 3: 
# 
#  输入:       1         1
#           / \       / \
#          2   1     1   2
# 
#         [1,2,1],   [1,1,2]
# 
# 输出: false
#  
#  Related Topics 树 深度优先搜索 
#  👍 407 👎 0
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        left_q = [p]
        right_q = [q]

        while left_q and right_q:
            left_elem = left_q.pop(0)
            right_elem = right_q.pop(0)
            if left_elem and right_elem:
                if left_elem.val == right_elem.val:
                    left_q.append(left_elem.left)
                    left_q.append(left_elem.right)
                    right_q.append(right_elem.left)
                    right_q.append(right_elem.right)
                else:
                    return False
            elif left_elem is None and right_elem is None:
                continue
            else:
                return False

        return True
        
# leetcode submit region end(Prohibit modification and deletion)
