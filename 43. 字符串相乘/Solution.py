# 43. 字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/multiply-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/multiply-strings/solution/you-hua-ban-shu-shi-da-bai-994-by-breezean/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m = len(num1)
        n = len(num2)
        res = [0 for _ in range(m + n)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                sum_num = res[i + j + 1] + int(num1[i]) * int(num2[j])
                # 直接取余，进位下面处理
                res[i+j+1] = sum_num % 10
                # 处理 i+j+1 的进位
                res[i+j] += sum_num // 10

        res_str = ''
        for i in range(m+n):
            if res_str == '' and int(res[i]) == 0:
                continue
            res_str += str(res[i])

        return res_str


sln = Solution()
numA = '123'
numB = '456'
print(sln.multiply(numA, numB))
