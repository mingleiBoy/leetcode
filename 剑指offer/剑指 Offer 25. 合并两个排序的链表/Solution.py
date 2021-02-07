# 剑指 Offer 25. 合并两个排序的链表
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 限制：
# 0 <= 链表长度 <= 1000
#
# 注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 双指针
# 涉及到链表的操作，一定要在纸上把过程先画出来，再写程序
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        # l2 向 l1 合并
        cur, pre = l1, None
        while cur and l2:
            # pre 和 cur 同时往后走
            if cur.val <= l2.val:
                pre = cur
                cur = cur.next
            # 插入 l2 ，调整 pre，而 cur 不动
            else:
                tmp = l2.next
                # 插入 l1 中
                if pre:
                    pre.next = l2
                    l2.next = cur
                    pre = l2
                else:
                    l1 = pre = l2
                    l2.next = cur
                l2 = tmp

        # l2 遍历结束，不管
        # l1 遍历结束，在尾部续上 l2
        if not cur:
            pre.next = l2
        return l1
