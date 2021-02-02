# 找出数组中重复的数字。
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例 1：
#
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
#
#
# 限制：
#
# 2 <= n <= 100000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# 原地置换 时间 O(n)  空间 O(1)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            m = nums[i]
            if i != m:
                if nums[i] == nums[m]:
                    return nums[i]
                else:
                    # 先把 m 对应的index还原，没有管 i 处
                    # 如果list没有重复元素，最后是会所有位置还原的
                    nums[i], nums[m] = nums[m], nums[i]

        return -1
