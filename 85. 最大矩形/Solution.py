# 85. 最大矩形
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 图不好画，看链接吧 -_-
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximal-rectangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 抄答案
# https://leetcode-cn.com/problems/maximal-rectangle/solution/yu-zhao-zui-da-ju-xing-na-ti-yi-yang-by-powcai/
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        row = len(matrix)
        col = len(matrix[0])
        height = [0] * (col + 2)
        res = 0
        for i in range(row):
            stack = []
            for j in range(col + 2):
                if 1 <= j <= col:
                    if matrix[i][j - 1] == "1":
                        height[j] += 1
                    else:
                        height[j] = 0
                while stack and height[stack[-1]] > height[j]:
                    cur = stack.pop()
                    res = max(res, (j - stack[-1] - 1) * height[cur])
                stack.append(j)
        return res

