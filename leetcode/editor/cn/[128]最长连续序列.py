# 给定一个未排序的整数数组，找出最长连续序列的长度。 
# 
#  要求算法的时间复杂度为 O(n)。 
# 
#  示例: 
# 
#  输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。 
#  Related Topics 并查集 数组 
#  👍 471 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set(nums)
        max_length = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                cur_num = nums[i]
                cur_length = 1
                while cur_num + 1 in hashset:
                    cur_length += 1
                    cur_num += 1
                max_length = max(max_length, cur_length)
        return max_length

# leetcode submit region end(Prohibit modification and deletion)
