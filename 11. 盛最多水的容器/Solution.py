# 11. 盛最多水的容器
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
# 示例：
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 水槽的实际高度由两板中的短板决定
# 水槽面积：S(i,j) = min(h[i],h[j]) × (j−i)。
# 在每一个状态下，无论长板或短板收窄 1 格，都会导致水槽 底边宽度 -1：
# 若向内移动短板，水槽的短板 可能变大，因此水槽面积 S(i, j)S(i,j) 可能增大。
# 若向内移动长板，水槽的短板 不变或变小，下个水槽的面积 一定小于 当前水槽面积。

class Solution:
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            max_water = 0
            start = 0
            end = len(height) - 1
            while start < end:
                max_water = max(max_water, (end - start) * min(height[start], height[end]))
                if height[start] < height[end]:
                    start += 1
                else:
                    end -= 1
            return max_water
