# 剑指 Offer 09. 用两个栈实现队列
# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# A是一个辅助stack
# B才是模仿的队列
# 两次翻转 stack == queue
# 只有执行 deleteHead 的方法的时候 B 才会同步最新的数据
class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())

        return self.B.pop()
