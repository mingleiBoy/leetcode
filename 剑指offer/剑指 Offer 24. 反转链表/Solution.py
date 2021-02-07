# 剑指 Offer 24. 反转链表
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#  
# 限制：
# 0 <= 节点个数 <= 5000
#
# 注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 递归
# 重点：设计递归函数，包括作用，参数，返回值
# 对递归的过程很不熟练
# 还有就是和迭代的思维过程搞混
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         def recursive(cur: ListNode, pre: ListNode) -> ListNode:
#             # 终止条件
#             if not cur:
#                 return pre
#             res = recursive(cur.next, cur)
#             cur.next = pre
#             return res
#
#         return recursive(head, None)

# 迭代
# 好处是空间复杂度是 O(1)，迭代是 O(n)
# 有个细节是初始化 pre 为 None，可以保证头结点翻转后 node.next == null
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp

        return pre
