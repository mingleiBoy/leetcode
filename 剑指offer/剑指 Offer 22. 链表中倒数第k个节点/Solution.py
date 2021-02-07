# 剑指 Offer 22. 链表中倒数第k个节点
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 2 个节点是值为 4 的节点。
#
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
# 返回链表 4->5.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 双指针大法
# 独立 AC，不错
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 1:
            return None

        fast = slow = head
        for i in range(k):
            fast = fast.next
            if not fast:
                return slow

        while fast:
            slow = slow.next
            fast = fast.next

        return slow
