# 123. 买卖股票的最佳时机 III
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
# 
# 注意:你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例1:
# 
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
#     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
#     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
# 
# 输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# 通用解法   k = 2
# https://leetcode-cn.com/circle/article/qiAgHn/
# 时间 O(n)
# 空间 O(n)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#
#         k = 2
#         length = len(prices)
#         dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(length)]
#         # 下标是 k+1： 状态方程的定义是 最多进行 k 次交易
#         dp[0][1][0] = 0
#         dp[0][1][1] = -prices[0]
#         dp[0][2][0] = 0
#         dp[0][2][1] = -prices[0]
#         # 注意是从 1 开始，不是 0
#         for i in range(1, length):
#             # 从 k == 2 开始算，因为交易次数是慢慢减少的
#             dp[2][0] = max(dp[2][0], dp[2][1] + prices)
#             dp[2][1] = max(dp[2][1], dp[1][0] - prices)
#             dp[1][0] = max(dp[1][0], dp[1][1] + prices)
#             dp[1][1] = max(dp[1][1], dp[0][0] - prices)
#
#         print(dp)
#         return dp[-1][-1][0]

# 时间 O(n)
# 空间 O(1)
# 第 i 天的最大收益只和第 i - 1 天的最大收益相关
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        k = 2
        length = len(prices)
        # 下标是 k+1： 状态方程的定义是 最多进行 k 次交易
        dp = [[0 for _ in range(2)] for _ in range(k + 1)]
        dp[1][0] = 0
        dp[1][1] = -prices[0]
        dp[2][0] = 0
        dp[2][1] = -prices[0]
        
        # 注意是从 1 开始，不是 0
        for i in range(1, length):
            # 从 k == 2 开始算，因为交易次数是慢慢减少的
            dp[2][0] = max(dp[2][0], dp[2][1] + prices[i])
            dp[2][1] = max(dp[2][1], dp[1][0] - prices[i])
            dp[1][0] = max(dp[1][0], dp[1][1] + prices[i])
            dp[1][1] = max(dp[1][1], dp[0][0] - prices[i])

        print(dp)
        return dp[-1][0]


sln = Solution()
# p = [3, 3, 5, 0, 0, 3, 1, 4]
# p = [1, 2, 3, 4, 5]
# p = [7, 6, 4, 3, 1]
print(sln.maxProfit(p))
