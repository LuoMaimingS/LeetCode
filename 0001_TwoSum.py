# 一遍哈希法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_dic: return [hash_dic[diff], i]
            else: hash_dic[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
