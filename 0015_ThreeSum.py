class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        num_list = sorted(nums)
        result = []
        for i in range(len(num_list)):
            a = num_list[i]
            if a > 0: break
            if i > 0 and num_list[i-1] == num_list[i]: continue
            target_sum = -a
            left, right = i + 1, len(num_list) - 1
            while left < right:
                temp_sum = num_list[left] + num_list[right]
                if temp_sum == target_sum:
                    result.append([a, num_list[left], num_list[right]])
                    while left < right and num_list[left] == num_list[left+1]: left += 1
                    while left < right and num_list[right] == num_list[right-1]: right -= 1
                    left += 1
                    right -= 1
                elif temp_sum < target_sum:
                    left += 1
                elif temp_sum > target_sum:
                    right -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))




