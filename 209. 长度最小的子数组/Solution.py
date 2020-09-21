# 209. 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#  
# 进阶：
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            if n == 1 and nums[0] >= s:
                return 1
            return 0

        start, end, min_length, cur_sum = 0, 1, 0, nums[0]
        while end < n:
            if nums[start] >= s or nums[end] >= s:
                return 1
            if cur_sum + nums[end] < s:
                cur_sum += nums[end]
                end += 1
            else:
                if min_length == 0:
                    min_length = end - start + 1
                else:
                    min_length = min(min_length, end - start + 1)
                cur_sum -= nums[start]
                start += 1
        return min_length
