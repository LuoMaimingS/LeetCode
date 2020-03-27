import re


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        return max(min(int(*re.findall('^[+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)


# class Solution(object):
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         if not str: return 0
#         result = 0
#         sign = 1
#         searching = False
#         max_v, min_v = (1 << 31) - 1, -(1 << 31)
#         for s in str:
#             if s == ' ':
#                 if searching: break
#                 else: continue
#             elif s in ['+', '-']:
#                 if searching: break
#                 searching = True
#                 sign = 0 if s == '-' else 1
#             elif 48 <= ord(s) <= 57:
#                 searching = True
#                 result = result * 10 + ord(s) - 48
#                 if sign == 1 and result > max_v:
#                     return max_v
#                 elif sign == 0 and -result < min_v:
#                     return min_v
#             elif not searching:
#                 return 0
#             elif searching:
#                 break
#         if sign == 0: result = -result
#         return result


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi('42'))
    print(s.myAtoi('   -42'))
    print(s.myAtoi('4193 with words'))
    print(s.myAtoi('words and 987'))
    print(s.myAtoi('   +0 123'))

