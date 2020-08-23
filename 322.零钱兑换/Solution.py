# 322. 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
#  
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-xiang-jie-jin-jie

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not list or not len(coins) or amount < 0:
            return -1

        dp = [amount + 1] * (amount + 1)
        # 显然目标金额为 0 时，所需硬币数量为 0；
        dp[0] = 0

        for i in range(0, len(dp)):
            for coin in coins:
                # 当目标金额小于 0 时，无解，返回 - 1：
                if i - coin < 0:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # python 三元写法，等价于：
        # if dp[amount] != amount + 1:
        #     return dp[amount]
        # else:
        #     return -1

        return dp[amount] if dp[amount] != amount + 1 else -1


coins = [1, 2, 5]
amount = 3
s = Solution()
print(s.coinChange(coins, amount))
