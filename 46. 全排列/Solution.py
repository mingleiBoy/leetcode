# 46. 全排列
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/hui-su-suan-fa-xiang-jie-xiu-ding-ban
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, track = [], []
        self.back_track(res, track, nums)
        return res

    def back_track(self, res: List[List[int]], track: List[int], nums: List[int]):
        if len(track) == len(nums):
            res.append(track.copy())
            return

        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.back_track(res, track, nums)
            track.pop()


sln = Solution()
num_list = [1, 2, 3]
final_res = sln.permute(num_list)
print(final_res)
