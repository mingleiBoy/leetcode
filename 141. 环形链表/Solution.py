# 141. 环形链表
# 给定一个链表，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。
# 注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环，则返回 true 。 否则，返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = fast = head
        while slow:
            slow = slow.next
            # 快指针先走一步
            fast = fast.next
            if not fast or not fast.next:
                return False
            # 快指针再走一步，速度也就是慢指针的2倍，有环就一定能套圈
            fast = fast.next
            if fast == slow:
                return True

        return False


nodeA = ListNode(3)
nodeB = ListNode(2)
nodeC = ListNode(0)
nodeD = ListNode(-4)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeB

s = Solution()
print(s.hasCycle(nodeA))

