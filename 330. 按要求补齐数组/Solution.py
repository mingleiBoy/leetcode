# 330. 按要求补齐数组
# 给定一个已排序的正整数数组 nums，和一个正整数n 。从[1, n]区间内选取任意个数字补充到nums中，使得[1, n]区间内的任何数字都可以用nums中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。
# 
# 示例1:
# 
# 输入: nums = [1,3], n = 6
# 输出: 1 
# 解释:
# 根据 nums里现有的组合[1], [3], [1,3]，可以得出1, 3, 4。
# 现在如果我们将2添加到nums 中，组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
# 其和可以表示数字1, 2, 3, 4, 5, 6，能够覆盖[1, 6]区间里所有的数。
# 所以我们最少需要添加一个数字。
# 示例 2:
# 
# 输入: nums = [1,5,10], n = 20
# 输出: 2
# 解释: 我们需要添加[2, 4]。
# 示例3:
# 
# 输入: nums = [1,2,2], n = 5
# 输出: 0
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/patching-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/patching-array/solution/an-yao-qiu-bu-qi-shu-zu-by-leetcode-solu-klp1/
# https://leetcode-cn.com/problems/patching-array/solution/patching-array-tan-lan-suan-fa-by-jyd/
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        max_range = 1
        i = 0
        # 对于正整数 xx，
        # 如果区间 [1,x-1] 内的所有数字都已经被覆盖，且 xx 在数组中，
        # 则区间 [1,2x-1] 内的所有数字也都被覆盖

        # 为什么这里是 <= 而不是 < ?
        # max_range 可能是 2x，而条件是 2x-1 < n
        while max_range <= n:
            if i < len(nums) and nums[i] <= max_range:
                max_range += nums[i]
                i += 1
            else:
                max_range *= 2
                count += 1

        return count
