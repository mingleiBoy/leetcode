# 剑指 Offer 29. 顺时针打印矩阵
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
# 限制：
#
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100
# 注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
#
# 相关标签
# 数组
#
# 作者：Krahets
# 链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5vfh9g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List


# 转为边界相遇问题
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        left, right, top, bottom, res = 0, len(matrix[0])-1, 0, len(matrix)-1, []
        while True:
            # 向右
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            # 向下
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            # 向左
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            # 向上
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return res
