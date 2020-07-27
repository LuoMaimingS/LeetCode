# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。 
# 
#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下： 
# 
#  L   C   I   R
# E T O E S I I G
# E   D   H   N
#  
# 
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。 
# 
#  请你实现这个将字符串进行指定行数变换的函数： 
# 
#  string convert(string s, int numRows); 
# 
#  示例 1: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#  
# 
#  示例 2: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G 
#  Related Topics 字符串 
#  👍 760 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if numRows == 1 or numRows > len(s):
            return s
        res = ""
        n = numRows
        for i in range(n):
            if i == 0 or i == n - 1:
                gap = [2*n-2]
            else:
                gap = [2*n-2 - 2*i, 2*i]
            cur_idx = i
            res += s[cur_idx]
            gap_idx = 0
            divisor = len(gap)
            while 1:
                cur_idx = cur_idx + gap[gap_idx % divisor]
                if cur_idx < len(s):
                    res += s[cur_idx]
                    gap_idx += 1
                else:
                    break
        return res

# leetcode submit region end(Prohibit modification and deletion)
