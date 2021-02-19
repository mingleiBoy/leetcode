# 剑指 Offer 40. 最小的 k 个数
#
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
# 示例 1：
# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
# 示例 2：
#
# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
# 限制：
# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000
#
# 相关标签  堆 分治算法
#
# 作者：Krahets
# 链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/ohvl0d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List

# TopK 问题
# 1. 快排，背下来 （这个是快速选择）
# 2. 大根堆
# 3. 二叉搜索树（略）
# class Solution:
#     # 快排
#     # 哨兵 + 递归
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         def quickSort(array: List[int], left: int, right: int):
#             if left >= right:
#                 return
#
#             i, j, base = left, right, array[left]
#             while i < j:
#                 while i < j and array[j] >= base:
#                     j -= 1
#                 while i < j and array[i] <= base:
#                     i += 1
#                 array[i], array[j] = array[j], array[i]
#
#             # 交换哨兵和最后的游标元素
#             array[left], array[i] = array[i], array[left]
#
#             # 递归左边和右边
#             quickSort(array, left, i - 1)
#             quickSort(array, i + 1, right)
#
#         quickSort(arr, 0, len(arr) - 1)
#         return arr[:k]

class Solution:
    # 快排 + 剪枝
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):
            return arr

        def quickSort(array: List[int], left: int, right: int):
            if left >= right:
                return

            i, j, base = left, right, array[left]
            while i < j:
                while i < j and array[j] >= base:
                    j -= 1
                while i < j and array[i] <= base:
                    i += 1
                array[i], array[j] = array[j], array[i]

            # 交换哨兵和最后的游标元素
            # 至此，完成本轮的排序
            array[left], array[i] = array[i], array[left]

            # 剪枝，根据条件递归左边和右边
            # 例如：如果一轮排序后， i == j == 2，而 k == 4
            # 左侧没必要再排序，反正都是满足条件的最小的 K 个数
            if k < i:
                quickSort(array, left, i - 1)
            if k > i:
                quickSort(array, i + 1, right)

        quickSort(arr, 0, len(arr) - 1)
        return arr[:k]
