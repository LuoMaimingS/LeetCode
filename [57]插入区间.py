# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
#  在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#  示例 1:
#
#  输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
#  示例 2:
#
#  输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#  Related Topics 排序 数组
#  👍 167 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        insert_idx = 0
        while (insert_idx < n) and (intervals[insert_idx][1] < newInterval[0]):
            insert_idx += 1

        # 没有重叠且在最右
        if insert_idx == n:
            intervals.append(newInterval)
            return intervals

        # 没有重叠且在中间
        if intervals[insert_idx][0] > newInterval[1]:
            intervals.insert(insert_idx, newInterval)
            return intervals

        # 有重叠
        # 拓展左右边界
        intervals[insert_idx][0] = min(intervals[insert_idx][0], newInterval[0])
        intervals[insert_idx][1] = max(intervals[insert_idx][1], newInterval[1])
        right_boundary = intervals[insert_idx][1]

        # 合并区间
        merge_idx = insert_idx + 1
        while (merge_idx < n) and (intervals[merge_idx][0] <= right_boundary):
            right_boundary = max(right_boundary, intervals[merge_idx][1])
            intervals[insert_idx][1] = right_boundary
            del intervals[merge_idx]
            n -= 1
        return intervals

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4, 8]

    print(s.insert(intervals, newInterval))

