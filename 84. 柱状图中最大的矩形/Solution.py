# 84. 柱状图中最大的矩形
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
# 看网站吧
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# # 1. 暴力法
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         if not heights:
#             return 0
#
#         n = len(heights)
#         res = 0
#         for i in range(n):
#             current_height = heights[i]
#             # 向左找
#             left = i
#             while left >= 0:
#                 if current_height > heights[left]:
#                     break
#                 left -= 1
#
#             # 向右找
#             right = i
#             while right < n:
#                 if current_height > heights[right]:
#                     break
#                 right += 1
#
#             # right - left - 1 这种的就要积累了
#             current_area = (right - left - 1) * current_height
#             res = max(res, current_area)
#             print("i = ", i, "left = ", left, "right = ", right, "area = ", current_area, "res = ", res)
#
#         return res

# 2. 单向栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


sln = Solution()
h_list = [2, 1, 5, 6, 2, 3]
print(sln.largestRectangleArea(h_list))
