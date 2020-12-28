# 122. 买卖股票的最佳时机 II
# 给定一个数组，它的第i 个元素是一支给定股票第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:
#
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
#     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例3:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


# 通用解法   k为正无穷
# https://leetcode-cn.com/circle/article/qiAgHn/
# 时间 O(n)
# 空间 O(n)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#
#         length = len(prices)
#         dp = [[0 for _ in range(2)] for _ in range(length)]
#         dp[0][0] = 0
#         dp[0][1] = -prices[0]
#         # 注意是从 1 开始，不是 0
#         for i in range(1, length):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
#
#         print(dp)
#         return dp[-1][0]


# 时间 O(n)
# 空间 O(1)
# 这个解法提供了获得最大收益的贪心策略：
# 可能的情况下，在每个局部最小值买入股票，然后在之后遇到的第一个局部最大值卖出股票。
# 这个做法等价于找到股票价格数组中的递增子数组，
# 对于每个递增子数组，在开始位置买入并在结束位置卖出。
# 可以看到，这和累计收益是相同的，只要这样的操作的收益为正。

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)

        profit0 = 0
        profit1 = -prices[0]

        # 注意是从 1 开始，不是 0
        for i in range(1, length):
            new_profit0 = max(profit0, profit1 + prices[i])
            new_profit1 = max(profit1, profit0 - prices[i])
            profit0 = new_profit0
            profit1 = new_profit1
            print(profit0, profit1)

        return profit0


sln = Solution()
p = [7, 1, 5, 3, 6, 4]
# p = [1, 2, 3, 4, 5]
print(sln.maxProfit(p))
