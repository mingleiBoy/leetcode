"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        if not row or not column:
            return 0

        for i in range(row):
            for j in range(column):
                cur_val = grid[i][j]
                if i > 0 and j > 0:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + cur_val
                elif not i:
                    grid[i][j] = grid[i][j - 1] + cur_val
                elif not j:
                    grid[i][j] = grid[i - 1][j] + cur_val

        return grid[-1][-1]


"""
    # 原地 dp
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        if not row or not column:
            return 0

        for i in range(row):
            for j in range(column):
                cur_val = grid[i][j]
                # 这里是个小坑，若是用上面的写法，会计算错误。猜为什么？
                if i == j == 0:
                    continue
                elif not i:
                    grid[i][j] = grid[i][j - 1] + cur_val
                elif not j:
                    grid[i][j] = grid[i - 1][j] + cur_val
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + cur_val

        return grid[-1][-1]
"""
