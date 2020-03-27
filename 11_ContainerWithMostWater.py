class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max = 0
        if n < 2: return 0
        left, right = 0, n - 1
        while right > left:
            area = min(height[left], height[right]) * (right - left)
            if area > max: max = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max
