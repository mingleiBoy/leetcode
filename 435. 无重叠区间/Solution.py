# 435. 无重叠区间
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
#
# 注意:
#
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
# 示例 1:
#
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
#
# 输出: 1
#
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 示例 2:
#
# 输入: [ [1,2], [1,2], [1,2] ]
#
# 输出: 2
#
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 示例 3:
#
# 输入: [ [1,2], [2,3] ]
#
# 输出: 0
#
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/non-overlapping-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        print(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] == start:
                count += 1
                print("step 1 -- i :", i, " count: ", count)
                end = min(end, intervals[i][1])
            else:
                if intervals[i][0] < end:
                    count += 1
                    print("step 2 -- i :", i, " count: ", count)
                start = intervals[i][0]

        return count


sln = Solution()
# target_list = [[1, 2], [2, 3], [3, 4], [1, 3]]
# target_list = [[1, 2], [1, 2], [1, 2]]
target_list = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
print(sln.eraseOverlapIntervals(target_list))
