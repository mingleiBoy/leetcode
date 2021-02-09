# 剑指 Offer 57. 和为 s 的两个数字
# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
#
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]
#
# 作者：Krahets
# 链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/5832fi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List


# 题目是递增序列
# 若是普通序列，用 hashMap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return []

        # 细节可以多加一些判断，比如 num[i] > target 直接return []
        i, j = 0, n-1
        while i < j:
            cur = nums[i] + nums[j]
            if cur < target:
                i += 1
            elif cur > target:
                j -= 1
            else:
                return [nums[i], nums[j]]

        return []
