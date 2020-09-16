# 1277. 统计全为 1 的正方形子矩阵
# 示例 1：
#
# 输入：matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 输出：15
# 解释：
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
# 示例 2：
#
# 输入：matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, column = len(matrix), len(matrix[0])
        dp = [[0] * column for _ in range(row)]
        ans = 0
        for i in range(row):
            for j in range(column):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                ans += dp[i][j]
        return ans
