# 剑指 Offer 11. 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
#
# 示例 1：
#
# 输入：[3,4,5,1,2]
# 输出：1
# 示例 2：
#
# 输入：[2,2,2,0,1]
# 输出：0
# 注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 排序数组的查找问题首先考虑使用 二分法 解决，其可将 遍历法 的 线性级别 时间复杂度降低至 对数级别
from typing import List

'''
为什么 right-- 不会对结果产生影响
    - 产生影响的条件： 删除的元素为唯一最小元素
    - 执行条件：numbers[right] == numbers[mid]
    - 由于 mid = (right + left) / 2 < right ==> mid < right
    - 故必须存在两个相等的值，都为最小值，矛盾
'''
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers)-1
        while left < right:
            # mid = left + (right - left) / 2
            mid = (left + right) / 2
            if numbers[mid] > numbers[right]:
                # 此时肯定不是最小值
                # 从 mid 到 right 不是递增的，肯定是有分割点存在
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                # mid 到 right 是递增的，肯定没有分割点
                # 分割点可能是 mid，所以不能 right = mid-1
                right = mid
            else:
                right -= 1

        return numbers[left]
