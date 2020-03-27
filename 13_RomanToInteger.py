class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))


# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if not s: return 0
#         roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         value = 0
#         prev_char = None
#         for char in s:
#             value += roman_dic[char]
#             if prev_char and roman_dic[prev_char] < roman_dic[char]:
#                 value -= 2 * roman_dic[prev_char]
#             prev_char = char
#         return value



