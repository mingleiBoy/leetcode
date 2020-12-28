# 188. 买卖股票的最佳时机 IV
# 给定一个整数数组prices ，它的第 i 个元素prices[i] 是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1：
# 
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 示例 2：
# 
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
#
# 提示：
# 
# 0 <= k <= 109
# 0 <= prices.length <= 1000
# 0 <= prices[i] <= 1000
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# 通用解法
# https://leetcode-cn.com/circle/article/qiAgHn/
# 时间 O(kn)
# 空间 O(kn)
# 有收益的交易的数量最多为 n / 2，故而 k > n/2 时，可以等效成 k == +无穷
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k < 1 or not prices:
            return 0

        length = len(prices)
        if k >= length / 2:
            return self.maxProfitKIsInfinity(prices)

        dp = [[[0 for _ in range(2)] for _ in range(k + 2)] for _ in range(length)]
        for i in range(1, k + 2):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]

        for i in range(1, length):
            for j in range(k + 1, 0, -1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][k][0]

    def maxProfitKIsInfinity(self, prices: List[int]) -> int:
        # 122 题
        length = len(prices)
        profit0 = 0
        profit1 = -prices[0]
        for i in range(1, length):
            tmp_profit0 = max(profit0, profit1 + prices[i])
            tmp_profit1 = max(profit1, profit0 - prices[i])

            profit0 = tmp_profit0
            profit1 = tmp_profit1

        return profit0


sln = Solution()
k_k = 1
p = [3, 2, 6, 5, 0, 3]
print(sln.maxProfit(k_k, p))
