class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        a = abs(x)
        max_v, min_v = (1 << 31) - 1, -(1 << 31)
        while a != 0:
            digit = a % 10
            if result > max_v // 10 or (result == max_v // 10 and digit > 7): return 0
            if result < -abs(min_v) // 10 or (result == -abs(min_v) // 10 and digit < 8): return 0
            a = a // 10
            result = result * 10 + digit
        if x < 0: result = -result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-2147483412))
