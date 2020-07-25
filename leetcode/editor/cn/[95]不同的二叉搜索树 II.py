# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。 
# 
#  
# 
#  示例： 
# 
#  输入：3
# 输出：
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 8 
#  
#  Related Topics 树 动态规划 
#  👍 574 👎 0


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
def generateSubTree(left, right):
    if left == right:
        return [TreeNode(val=left)]
    ret_trees = []

    for i in range(left, right + 1):
        left_subtrees = []
        right_subtrees = []
        if i > left:
            left_subtrees = generateSubTree(left, i - 1)
        if i < right:
            right_subtrees = generateSubTree(i + 1, right)
        if len(left_subtrees) == 0 and len(right_subtrees) != 0:
            for right_sub in right_subtrees:
                cur_node = TreeNode(val=i, right=right_sub)
                ret_trees.append(cur_node)
        elif len(left_subtrees) != 0 and len(right_subtrees) == 0:
            for left_sub in left_subtrees:
                cur_node = TreeNode(val=i, left=left_sub)
                ret_trees.append(cur_node)
        else:
            for left_sub in left_subtrees:
                for right_sub in right_subtrees:
                    cur_node = TreeNode(val=i, left=left_sub, right=right_sub)
                    ret_trees.append(cur_node)

    return ret_trees


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ret = generateSubTree(1, n)
        return ret


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    s.generateTrees(3)
