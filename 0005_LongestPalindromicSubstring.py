class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(s, left, right):
            l, r = left, right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        if len(s) == 0: return ""
        max_len = 0
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand_around_center(s, i, i)
            len2 = expand_around_center(s, i, i + 1)
            temp_len = max(len1, len2)
            if temp_len > max_len:
                max_len = temp_len
                start, end = i - (temp_len - 1) // 2, i + temp_len // 2
        return s[start:end + 1]


# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         def is_palindromic_str(s):
#             n = len(s)
#             if n <= 1: return True
#             i, j = 0, n - 1
#             while j >= i + 1:
#                 if s[i] != s[j]:
#                     return False
#                 i += 1
#                 j -= 1
#             return True
#
#         n = len(s)
#         if n == 0: return ""
#         elif n == 1: return s
#         for i in range(n, 1, -1):
#             for j in range(n - i + 1):
#                 if is_palindromic_str(s[j:j + i]): return s[j:j + i]
#
#         return s[0]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('cbb'))
