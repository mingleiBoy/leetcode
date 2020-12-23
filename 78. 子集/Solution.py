# 78. 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/subsets/solution/hui-su-si-xiang-tuan-mie-pai-lie-zu-he-zi-ji-wen-t/
from typing import List


# 方法一： 添加新元素时给所有旧集合加上这个元素
# [] -> [][1] -> [][1][2][12] -> [][1][2][12][3][13][23][123]
# 复杂度高，不用

# 方法二： 回溯法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, track = [], []

        def back_track(index: int):
            # 添加路径
            res.append(track.copy())

            for i in range(index, len(nums)):
                track.append(nums[i])
                # 更新选择
                back_track(i+1)
                track.pop()

        back_track(0)
        return res
