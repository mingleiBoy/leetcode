# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 迭代
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if not l1 and not l2:
    #         return None
    #     if l1 and not l2:
    #         return l1
    #     if l2 and not l1:
    #         return l2
    #
    #     root = None
    #     head = None
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             if not root:
    #                 root = l1
    #                 head = root
    #             else:
    #                 head.next = l1
    #                 head = head.next
    #             l1 = l1.next
    #         else:
    #             if not root:
    #                 root = l2
    #                 head = root
    #             else:
    #                 head.next = l2
    #                 head = head.next
    #             l2 = l2.next
    #
    #     if l1 and not l2:
    #         head.next = l1
    #     elif not l1 and l2:
    #         head.next = l2
    #
    #     return root

    # 递归
    # https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/

    # 终止条件：当某个链表为空时，表示我们对链表已合并完成。
    # 如何递归：我们判断 l1 和 l2 头结点哪个更小，然后较小结点的 next 指针指向其余结点的合并结果。（调用递归）

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2  # 终止条件，直到某个链表为空
        if not l2:
            return l1

        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
