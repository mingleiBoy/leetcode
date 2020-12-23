# 73. 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
#
# 输入:
# [
#  [1,1,1],
#  [1,0,1],
#  [1,1,1]
# ]
# 输出:
# [
#  [1,0,1],
#  [0,0,0],
#  [1,0,1]
# ]
# 示例2:
#
# 输入:
# [
#  [0,1,2,0],
#  [3,4,5,2],
#  [1,3,1,5]
# ]
# 输出:
# [
#  [0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]
# ]
# 进阶:
#
# 一个直接的解决方案是使用 O(mn)的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m+n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/set-matrix-zeroes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/set-matrix-zeroes/solution/o1kong-jian-by-powcai/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        # 用原 matrix 的第一行和第一列存数据，思路牛逼
        col0_has_zero, row0_has_zero = False, False
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            if matrix[row][0] == 0:
                col0_has_zero = True
                break

        for col in range(n):
            if matrix[0][col] == 0:
                row0_has_zero = True
                break

        # 从内层开始找，找到的时候就把最外层的值设好了
        # 所以查找和赋值都不用考虑 m = 0 和 n = 0
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0

                    # AC 不过，因为这个break
                    # 当找到某列有 0 时，要继续找，因为还要将其它行置0
                    # break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if col0_has_zero:
            for i in range(m):
                matrix[i][0] = 0

        if row0_has_zero:
            for i in range(n):
                matrix[0][i] = 0


sln = Solution()
mat = [[3, 5, 5, 6, 9, 1, 4, 5, 0, 5], [2, 7, 9, 5, 9, 5, 4, 9, 6, 8], [6, 0, 7, 8, 1, 0, 1, 6, 8, 1],
       [7, 2, 6, 5, 8, 5, 6, 5, 0, 6], [2, 3, 3, 1, 0, 4, 6, 5, 3, 5], [5, 9, 7, 3, 8, 8, 5, 1, 4, 3],
       [2, 4, 7, 9, 9, 8, 4, 7, 3, 7], [3, 5, 2, 8, 8, 2, 2, 4, 9, 8]]
sln.setZeroes(mat)
print(mat)
