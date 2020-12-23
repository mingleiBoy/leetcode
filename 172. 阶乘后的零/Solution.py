# 172. 阶乘后的零
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
#
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 示例 2:
#
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为O(log n)。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 兼容 leetcode 负数用例
        flag = 1 if n >= 0 else 0
        n = abs(n)
        res = 0
        # 看所有乘法因子中可以分解出 5 的个数
        # 隔 5 个数有 1个5                       5的个数： n/5
        # 隔 25 个数另外有 1个5 (5*5)             5的个数： n/5 + n/25
        # 隔 125 个数还另外有 1个5 (5*5*5)        5的个数： n/5 + n/25 + n/125
        while n > 0:
            res += n // 5

            # 相当于 n/25 n/125 ...
            n //= 5

        return res if flag > 0 else -res


sln = Solution()
num = 123
print(sln.trailingZeroes(num))
