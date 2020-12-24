# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
# 示例2:
#
# 输入: "()[]{}"
# 输出: true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def isCompare(target_ch: str) -> bool:
            if not stack:
                return False

            current_ch = stack[-1]
            if target_ch == '}':
                return current_ch == '{'
            elif target_ch == "]":
                return current_ch == '['
            elif target_ch == ')':
                return current_ch == '('

            return False

        for ch in s:
            if isCompare(ch):
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


sln = Solution()
str_text = ""
print(sln.isValid(str_text))
