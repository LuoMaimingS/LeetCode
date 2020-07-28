# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 927 👎 0

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_q = [root]
        right_q = [root]

        while left_q and right_q:
            left_elem = left_q.pop(0)
            right_elem = right_q.pop(0)
            if left_elem and right_elem:
                if left_elem.val == right_elem.val:
                    left_q.append(left_elem.left)
                    left_q.append(left_elem.right)
                    right_q.append(right_elem.right)
                    right_q.append(right_elem.left)
                else:
                    return False
            elif left_elem is None and right_elem is None:
                continue
            else:
                return False

        return True


# leetcode submit region end(Prohibit modification and deletion)
