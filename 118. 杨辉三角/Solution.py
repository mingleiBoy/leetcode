"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        dp = [[1] for _ in range(numRows)]

        for row in range(1, numRows):
            dp[row] = [1 for _ in range(row + 1)]
            for column in range(1, row):
                dp[row][column] = dp[row - 1][column - 1] + dp[row - 1][column]

        return dp


s = Solution()
num = 5
print(s.generate(num))
