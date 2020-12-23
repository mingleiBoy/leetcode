# 384. 打乱数组
# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
#
# 实现 Solution class:
#
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shuffle-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://gaohaoyang.github.io/2016/10/16/shuffle-algorithm/

# Fisher–Yates shuffle 洗牌算法
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.array = list(nums)
        self.origin_array = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = list(self.origin_array)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.origin_array)
        for i in range(n):
            random_idx = random.randrange(i, n)
            self.array[i], self.array[random_idx] = self.array[random_idx], self.array[i]

        return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
