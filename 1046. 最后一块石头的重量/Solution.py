# 1046. 最后一块石头的重量
# 有一堆石头，每块石头的重量都是正整数。
# 
# 每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为x 和y，且x <= y。那么粉碎的可能结果如下：
# 
# 如果x == y，那么两块石头都会被完全粉碎；
# 如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
# 
# 示例：
# 
# 输入：[2,7,4,1,8,1]
# 输出：1
# 解释：
# 先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
# 再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
# 接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
# 最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
# 
# 提示：
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/last-stone-weight
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from heapq import heapify, heappush, heappop
from typing import List


# 排序法，这个写法比较简明扼要，看着舒服
# O(n^2logN)  还是比较高的
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         while len(stones) >= 2:
#             stones.sort()
#             stones.append(stones.pop() - stones.pop())
#         return stones[0]

# 系统api，大顶堆
# 就不自己实现了，应该也不会考
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        # python只能使用最小堆，最大堆是私有方法
        heap = [-i for i in stones]
        # 原地排序
        heapify(heap)
        while len(heap) > 1:
            heappush(heap, heappop(heap) - heappop(heap))
        return -heap[0]


sln = Solution()
target_list = [2, 7, 4, 1, 8, 1]
print(sln.lastStoneWeight(target_list))
