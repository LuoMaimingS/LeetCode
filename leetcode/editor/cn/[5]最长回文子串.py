# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2483 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


def maxSubP(s, cent_left, cent_right):
    left = cent_left
    right = cent_right
    while (left >= 0) and (right < len(s)):
        if s[left] == s[right]:
            left -= 1
            right += 1
        else:
            return left + 1, right - 1
    if left < 0 or right >= len(s):
        return left + 1, right - 1
    else:
        return left, right


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_length = 0
        begin = 0
        end = 0
        for i in range(n):
            left1, right1 = maxSubP(s, i, i)
            if i == n - 1:
                left2, right2 = 0, -1
            else:
                left2, right2 = maxSubP(s, i, i + 1)
            if right2 - left2 + 1 > max_length:
                max_length = right2 - left2 + 1
                begin, end = left2, right2
            if right1 - left1 + 1 > max_length:
                max_length = right1 - left1 + 1
                begin, end = left1, right1
        return s[begin:end+1]

# leetcode submit region end(Prohibit modification and deletion)
