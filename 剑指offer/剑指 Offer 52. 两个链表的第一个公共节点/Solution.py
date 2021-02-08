# 剑指 Offer 52. 两个链表的第一个公共节点
#
# 输入两个链表，找出它们的第一个公共节点。
#
# 注意：
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
# 本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        l1, l2 = headA, headB
        # 当A链表走到尽头，给 l1 续上B链表
        # 同理，给l2续上A链表

        # a: A链表从头结点开始的不同部分长度
        # b: B链表从头结点开始的不同部分长度
        # d: 两个链表的相同部分长度

        # 当有交点时
        # 链表A走到交点的路径长度是： a + d + b
        # 链表B走到交点的路径长度是: b + d + a (与A路径相等)
        # 所以此时 l1 必然等于 l2，为两个链表的第一次相遇

        # 当没有交点时
        # 链表A走到 a + b 时，链表B必然走到 b + a
        # 此时 l1 == l2 == null 也会正常跳出循环。
        # 可以理解为公共节点为空节点
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
