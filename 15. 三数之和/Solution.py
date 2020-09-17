# 15. 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        three_lists = []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return three_lists
            # 这里很骚，滤重
            if i > 0 and nums[i-1] == nums[i]:
                continue

            start = i + 1
            end = n - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                elif nums[i] + nums[start] + nums[end] == 0:
                    three_lists.append([nums[i], nums[start], nums[end]])
                    # 这里也很骚，滤重
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                else:
                    start += 1

        return three_lists


