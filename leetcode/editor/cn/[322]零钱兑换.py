# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。 
# 
#  
# 
#  示例 1: 
# 
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1 
# 
#  示例 2: 
# 
#  输入: coins = [2], amount = 3
# 输出: -1 
# 
#  
# 
#  说明: 
# 你可以认为每种硬币的数量是无限的。 
#  Related Topics 动态规划 
#  👍 718 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


def backtrack(coins, amount, used_coins, min_coins):
    print(amount, used_coins, min_coins)
    if amount <= 0:
        if amount == 0:
            min_coins = min(min_coins, used_coins)
        return min_coins

    for coin in coins:
        min_coins = backtrack(coins, amount - coin, used_coins + 1, min_coins)

    return min_coins


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        min_coins = backtrack(coins, amount, 0, 2147483648)
        if min_coins == 2147483648:
            return -1
        return min_coins

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    a = s.coinChange([1, 2, 5], 100)
    print(a)
