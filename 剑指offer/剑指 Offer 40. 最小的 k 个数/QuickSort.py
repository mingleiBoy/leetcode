# https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/jian-zhi-offer-40-zui-xiao-de-k-ge-shu-j-9yze/
# 快排算法，必须背下来，白纸可以无脑默写

# 二分、递归、基准数、哨兵
# 平均时间: O(NlogN)
# 空间: O(1)
# 原地排序、不稳定排序
from typing import List


class Solution:
    def quickSort(self, arr: List[int]):
        self.quickSortImpl(arr, 0, len(arr) - 1)
        print(arr)

    def quickSortImpl(self, arr: List[int], left: int, right: int):
        # 子数组长度为1时停止递归
        if left >= right:
            return

        # 哨兵划分，以 arr[left] 为基准数
        i, j, base = left, right, arr[left]
        while i < j:
            # 取最左侧作为哨兵，则一定是先从右侧开始走
            while i < j and arr[j] >= base:
                j -= 1
            while i < j and arr[i] <= base:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]

        # 互换哨兵和游标指针停留的元素
        # 注意此时 i,j 必然是相等的，且是小于哨兵的元素
        #       2 4 1 0 3 5  （哨兵是 2）
        # -->   1 0 2 4 3 5  （简单画一下流程就知道了）
        arr[left], arr[i] = arr[i], arr[left]

        self.quickSortImpl(arr, left, i - 1)
        self.quickSortImpl(arr, i + 1, right)


arr_list = [3, 4, 6, 2, 1, 8, 29, 22, 2, 5]
sln = Solution()
sln.quickSort(arr_list)
