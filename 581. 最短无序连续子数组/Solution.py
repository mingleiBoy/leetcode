# 581. 最短无序连续子数组
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 说明 :
#
# 输入的数组长度范围在[1, 10,000]。
# 输入的数组可能包含重复元素，所以升序的意思是<=。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# 方法一：双指针，分三段，找边界
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/si-lu-qing-xi-ming-liao-kan-bu-dong-bu-cun-zai-de-/
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         start, end = 0, -1
#         max_num = nums[start]
#         min_num = nums[end]
#
#         for i in range(len(nums)):
#             # 从左到右，找 max 和 end
#             if nums[i] < max_num:
#                 end = i
#             else:
#                 max_num = nums[i]
#
#             # 从右到左，找 min 和 start
#             if nums[-i-1] > min_num:
#                 start = len(nums) - 1 - i
#             else:
#                 min_num = nums[-i-1]
#
#         return end - start + 1

# 方法二：先排序，再找左右两端不同
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sort_nums = sorted(nums)
        n = len(nums)
        start, end = -1, -1
        for i in range(n):
            if start == -1 and nums[i] != sort_nums[i]:
                start = i

            if end == -1 and nums[-i - 1] != sort_nums[-i - 1]:
                end = n - i - 1

        return 0 if start == -1 or end == -1 else end - start + 1


sln = Solution()
num_list = [2, 1, 6, 4, 8, 10, 9, 15, 11]
print(sln.findUnsortedSubarray(num_list))
