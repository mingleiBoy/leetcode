# 945. 使数组唯一的最小增量
# 给定整数数组 A，每次 move 操作将会选择任意A[i]，并将其递增1。
#
# 返回使 A中的每个值都是唯一的最少操作次数。
#
# 示例 1:
#
# 输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
# 示例 2:
#
# 输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
# 提示：
#
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/solution/ji-shu-onxian-xing-tan-ce-fa-onpai-xu-onlogn-yi-ya/
from typing import List

# 两种方法： 1. 排序法（略）  2. 线性探测 + 路径压缩（比较巧妙）
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0

        n = len(A)
        # 80000: 最大值是40000，最多有40000个数。最坏是 80000 个"槽"
        # 空间换时间
        # 正常是每个槽的 idx == value 的，模拟 hashMap
        # 线性探测就是解冲突
        # 路径压缩为了大量节约时间
        track_list = [-1 for _ in range(80000)]

        def track(pos: int) -> int:
            if track_list[pos] == -1:
                track_list[pos] = pos
                return pos

            # 递归巧妙的将 "路径" 上的结点都赋值为目标值
            b = track(pos + 1)
            track_list[pos] = b
            return b

        res = 0
        for a in A:
            res += track(a) - a
        return res
