# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
#  示例:
#
#  输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  Related Topics 树 动态规划
#  👍 721 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


def countSubTree(left, right):
    if left == right:
        return 1
    total_count = 0

    for i in range(left, right + 1):
        left_count = 1
        right_count = 1
        if i > left:
            left_count = countSubTree(left, i - 1)
        if i < right:
            right_count = countSubTree(i + 1, right)
        total_count += left_count * right_count
    return total_count


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return countSubTree(1, n)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    s.numTrees(3)
