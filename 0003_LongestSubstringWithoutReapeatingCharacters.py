class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        look_up_set = set()
        cur_len = 0
        max_len = 0
        left = 0
        for i in range(len(s)):
            if s[i] in look_up_set:
                while s[i] in look_up_set:
                    look_up_set.remove(s[left])
                    left += 1
                    cur_len -= 1
            look_up_set.add(s[i])
            cur_len = len(look_up_set)
            if cur_len > max_len: max_len = cur_len
        return max_len


