# 编写一个程序，通过已填充的空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  Note: 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 482 👎 0

# leetcode submit region begin(Prohibit modification and deletion)


def isValidPut(board, row, col, val):
    # Row Check.
    val = str(val)
    if val in board[row]:
        return False

    # Column Check.
    n = len(board)
    for i in range(n):
        if board[i][col] == val:
            return False

    # Block Check.
    block_row0 = row // 3 * 3
    block_rows = [block_row0, block_row0 + 1, block_row0 + 2]
    block_col0 = col // 3 * 3
    block_cols = [block_col0, block_col0 + 1, block_col0 + 2]
    for r in block_rows:
        for c in block_cols:
            if board[r][c] == val:
                return False
    return True


def backtrack(row, col, board):
    if row == 8 and col == 9:
        return True

    next_row = row
    next_col = col
    while board[next_row][next_col] != '.':
        next_col += 1
        if next_col == 9:
            if next_row == 8:
                return True
            next_row += 1
            next_col = 0
    for num in range(1, 10):
        if isValidPut(board, next_row, next_col, num):
            board[next_row][next_col] = str(num)
            solved = backtrack(next_row, next_col, board)
            if solved:
                return True
            board[next_row][next_col] = '.'

    return False


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        backtrack(0, 0, board)
# leetcode submit region end(Prohibit modification and deletion)
