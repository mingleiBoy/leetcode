# 54. 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/spiral-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/  评论区
# https://leetcode-cn.com/problems/spiral-matrix-ii/solution/spiral-matrix-ii-mo-ni-fa-she-ding-bian-jie-qing-x/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        res = [0 for _ in range(m * n)]

        left, right, top, bottom = 0, n-1, 0, m-1
        count = 0
        while count < m * n:
            for i in range(left, right + 1):
                res[count] = matrix[top][i]
                count += 1
            top += 1
            if count >= m * n:
                break

            for i in range(top, bottom + 1):
                res[count] = matrix[i][right]
                count += 1
            right -= 1
            if count >= m * n:
                break

            for i in range(right, left - 1, -1):
                res[count] = matrix[bottom][i]
                count += 1
            bottom -= 1
            if count >= m * n:
                break

            for i in range(bottom, top - 1, -1):
                res[count] = matrix[i][left]
                count += 1
            left += 1

        return res


sln = Solution()
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sln.spiralOrder(mat))
