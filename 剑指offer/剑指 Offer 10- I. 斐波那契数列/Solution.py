# 剑指 Offer 10- I. 斐波那契数列
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
# 输入：n = 2
# 输出：1
#
# 示例 2：
# 输入：n = 5
# 输出：5
#
# 0 <= n <= 100
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 用其他语言运算中可能存在大数越界的问题，即超过 int64 范围
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        res, pre = 0, [0, 1]
        for i in range(2, n+1):
            res = (pre[0] + pre[1]) % 1000000007
            pre[0], pre[1] = pre[1], res
        return res % 1000000007

