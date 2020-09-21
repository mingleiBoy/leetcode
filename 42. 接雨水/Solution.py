# 42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0

        max_height = max(height)
        max_index = height.index(max_height)

        water = 0
        cur_height = height[0]
        for i in range(1, max_index):
            if height[i] < cur_height:
                water += cur_height - height[i]
            else:
                cur_height = height[i]

        cur_height = height[-1]
        for i in range(n-1, max_index, -1):
            if height[i] < cur_height:
                water += cur_height - height[i]
            else:
                cur_height = height[i]

        return water


s = Solution()
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
print(s.trap(heights))
