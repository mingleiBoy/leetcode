# 121. 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# 平平无奇解法
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n < 2:
#             return 0
#         max_profit = 0
#         low = 0
#         high = 1
#         while high < n:
#             if prices[high] < prices[low]:
#                 low = high
#             else:
#                 max_profit = max(max_profit, prices[high] - prices[low])
#             high += 1
#
#         return max_profit

# 通用解法
# https://leetcode-cn.com/circle/article/qiAgHn/
# 时间 O(n)
# 空间 O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)
        dp = [[0 for col in range(2)] for row in range(length)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        print(dp)
        return dp[-1][0]


# 优化
# 时间 O(n)
# 空间 O(1)
# 第 i 天的最大收益只和第 i - 1 天的最大收益相关
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        length = len(prices)
        profit0 = 0
        profit1 = -prices[0]
        print(profit0, profit1)
        for i in range(1, length):
            profit0 = max(profit0, profit1 + prices[i])
            profit1 = max(profit1, -prices[i])
            print(profit0, profit1)

        return profit0


sln = Solution()
p = [7, 1, 5, 3, 6, 4]
print(sln.maxProfit(p))
