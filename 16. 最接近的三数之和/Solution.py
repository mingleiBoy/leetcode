# 16. 最接近的三数之和
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#  
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
#
# 提示：
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        min_diff = float("inf")
        ans = 0
        # 递增排序
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = n - 1
            while start < end:
                three_sum = nums[i] + nums[start] + nums[end]
                if three_sum == target:
                    return target
                if abs(three_sum - target) < abs(min_diff):
                    min_diff = three_sum - target
                    ans = three_sum

                if three_sum < target:
                    start += 1
                elif three_sum > target:
                    end -= 1

        return ans
