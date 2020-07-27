# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5: 
# 
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false 
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 1417 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
def backtrack(rest_str, pattern):
    if (pattern == ' ' and rest_str == ' ') or (rest_str == ' ' and pattern[1] == '*' and pattern[2] == ' '):
        return True
    if pattern == ' ' and rest_str != ' ':
        return False
    if pattern != ' ' and rest_str == ' ':
        if len(pattern) >= 3:
            if pattern[1] == '*':
                return backtrack(rest_str, pattern[2:])

    if pattern[1] not in ['+', '*']:
        pat = pattern[0]
        if pat == rest_str[0] or (pat[0] == '.' and rest_str[0] != ' '):
            return backtrack(rest_str[1:], pattern[1:])
        else:
            return False
    else:
        pat = pattern[0:2]
        if pat[1] == '+':
            if (pat[0] == rest_str[0]) or (pat[0] == '.' and rest_str[0] != ' '):
                pattern[1] = '*'
                return backtrack(rest_str[1:], pattern)
            else:
                return False
        else:
            if len(pattern) > 5:
                if pattern[0:2] == pattern[2:4]:
                    return backtrack(rest_str, pattern[2:])
            if pat[0] == rest_str[0] or pat[0] == '.':
                use_this_pat = backtrack(rest_str[1:], pattern)
                if use_this_pat:
                    return True
                abandon_this_pat = backtrack(rest_str, pattern[2:])
                if abandon_this_pat:
                    return True
                return False
            else:
                return backtrack(rest_str, pattern[2:])


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        res = backtrack(s + ' ', p + ' ')
        return res

# leetcode submit region end(Prohibit modification and deletion)