# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 572 👎 0
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [(0, root)]
        res = [[]]

        while q:
            cur_elem = q.pop(0)
            cur_level = cur_elem[0]
            cur_node = cur_elem[1]
            if len(res) > cur_level:
                res[cur_level].append(cur_node.val)
            else:
                res.append([cur_node.val])
            if cur_node.left:
                q.append((cur_level + 1, cur_node.left))
            if cur_node.right:
                q.append((cur_level + 1, cur_node.right))

        return res


# leetcode submit region end(Prohibit modification and deletion)
