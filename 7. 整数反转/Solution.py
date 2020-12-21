# 7. 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例1:
#
# 输入: 123
# 输出: 321
# 示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为[−2^31, 2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-integer
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/reverse-integer/solution/pythondan-chu-he-tui-ru-shu-zi-yi-chu-qian-jin-xin/

class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        # (1 << 31) - 1 注意优先级
        boundary = (1 << 31) - 1 if x > 0 else 1 << 31
        res = 0

        while abs_x != 0:
            res = res * 10 + abs_x % 10
            if res > boundary:
                return 0
            abs_x //= 10

        return res if x > 0 else -res


s = Solution()
print(s.reverse(1463847412))
