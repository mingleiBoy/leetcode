# 剑指 Offer 30. 包含 min 函数的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.min();   --> 返回 -2.
#
# 提示：
# 各函数的调用总次数不超过 20000 次
#
# 注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
#
# 相关标签
# 栈  设计
#
# 作者：Krahets
# 链接：https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/50bp33/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        # 非严格递减，避免连续弹出重复值
        if not self.B or x <= self.B[-1]:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
