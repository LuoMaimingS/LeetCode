# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。 
# 
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  示例 1: 
# 
#  输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#  
# 
#  示例 2: 
# 
#  输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 
# 。
#  
#  Related Topics 动态规划 
#  👍 255 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import numpy as np

MIN_VAL = -16777216


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if k > int(days / 2):
            # infinite trading times.
            dp = -np.ones((days + 1, 2))
            dp[0, 0] = 0
            dp[0, 1] = MIN_VAL

            # 买入的时候计算（减少）可交易次数
            for i in range(1, days + 1):
                cur_price = prices[i-1]
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + cur_price)
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - cur_price)

            max_profit = int(np.max(dp[days, :]))
            return max_profit

        dp = -np.ones((days + 1, k + 1, 2))
        dp[0, :, 0] = 0
        dp[0, :, 1] = MIN_VAL

        # 买入的时候计算（减少）可交易次数
        for i in range(1, days + 1):
            for j in range(k + 1):
                cur_price = prices[i - 1]
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + cur_price)
                if j < k:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j+1][0] - cur_price)
                else:
                    dp[i][j][1] = MIN_VAL

        max_profit = int(np.max(dp[days, :, :]))
        return max_profit


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    pass