# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。 
# 
#  找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。 
# 
#  示例: 
# 
#  X X X X
# X O O X
# X X O X
# X O X X
#  
# 
#  运行你的函数后，矩阵变为： 
# 
#  X X X X
# X X X X
# X X X X
# X O X X
#  
# 
#  解释: 
# 
#  被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被
# 填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 268 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import numpy as np


def backtrack(board, row, col, flags):
    if flags[row][col] == 1:
        # Already Marked. Connected To Edge.
        return

    flags[row][col] = 1
    row_end = len(board) - 1
    col_end = len(board[0]) - 1
    # 上， 下， 左， 右
    if (row - 1) >= 0 and board[row - 1][col] == 'O':
        backtrack(board, row - 1, col, flags)
    if (row + 1) <= row_end and board[row + 1][col] == 'O':
        backtrack(board, row + 1, col, flags)
    if (col - 1) >= 0 and board[row][col - 1] == 'O':
        backtrack(board, row, col - 1, flags)
    if (col + 1) <= col_end and board[row][col + 1] == 'O':
        backtrack(board, row, col + 1, flags)


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m = len(board)
        if m <= 2:
            return
        n = len(board[0])
        if n <= 2:
            return

        flags_matrix = np.zeros((m, n))
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    backtrack(board, i, j, flags_matrix)
        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    backtrack(board, i, j, flags_matrix)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and flags_matrix[i][j] == 0:
                    board[i][j] = 'X'


# leetcode submit region end(Prohibit modification and deletion)