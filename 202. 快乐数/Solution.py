# 202. 快乐数
# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」定义为：对于一个正整数，
# 每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，
# 也可能是 无限循环 但始终变不到 1。
# 如果 可以变为 1，那么这个数就是快乐数。
#
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
#
# 示例：
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/happy-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math


class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 1:
            return n == 1

        slow = fast = n
        while slow > 1:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False

        return True

    def squareSum(self, n: int) -> int:
        sum_num = 0
        while n:
            lowest_bit = n % 10
            sum_num += lowest_bit ** 2
            n = math.floor(n / 10)
        return sum_num


s = Solution()
print(s.isHappy(65537))
