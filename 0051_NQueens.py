from copy import deepcopy


class Board:
    def __init__(self, n):
        self.n = n
        self.chess = []
        for i in range(n):
            self.chess.append('.' * n)

    def get_rep_list(self):
        return deepcopy(self.chess)

    def put(self, i, j):
        if self.is_valid(i, j):
            self.chess[i] = self.chess[i][:j] + 'Q' + self.chess[i][j+1:]
            return True
        return False

    def take_away(self, i, j):
        self.chess[i] = self.chess[i][:j] + '.' + self.chess[i][j + 1:]

    def is_valid(self, i, j):
        # column check
        for k in range(self.n):
            if self.chess[k][j] == 'Q':
                return False

        p, q = i, j
        while (p >= 0) and (0 <= q < self.n):
            if self.chess[p][q] == 'Q':
                return False
            p -= 1
            q += 1

        p, q = i, j
        while (p >= 0) and (0 <= q < self.n):
            if self.chess[p][q] == 'Q':
                return False
            p -= 1
            q -= 1

        return True


def backtrack(board, row, result_list):
    n = board.n
    if row == n:
        # 成功
        result_list.append(board.get_rep_list())
        return

    for i in range(n):
        valid = board.put(row, i)
        if not valid:
            continue
        backtrack(board, row + 1, result_list)
        board.take_away(row, i)

    return result_list


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = Board(n)
        result = []
        backtrack(board, 0, result)
        return result

