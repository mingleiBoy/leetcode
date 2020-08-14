/** 206. 反转链表
// 反转一个单链表。

// 示例:

// 输入: 1->2->3->4->5->NULL
// 输出: 5->4->3->2->1->NULL
// 进阶:
// 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/reverse-linked-list
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(final int x) { val = x; }
}

class Solution {
    // 递归
    // public static ListNode reverseList(ListNode head) {
    //     if (head == null || head.next == null) return head;

    //     ListNode[] nodes = new ListNode[1];
    //     reverseListImpl(nodes, head);
    //     return nodes[0];
    // }

    // private static ListNode reverseListImpl(ListNode[] nodes, ListNode head) {
    //     if (head.next == null) {
    //         nodes[0] = head;
    //         return head;        
    //     }

    //     ListNode next = reverseListImpl(nodes, head.next);
    //     next.next = head;
    //     head.next = null;
        
    //     return head;
    // }

    // 迭代
    public static ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        
        ListNode father = head;
        ListNode child = head.next;
        while (child != null) {
            ListNode nextChild = child.next;
            child.next = father;

            father = child;
            child = nextChild;
        }
        head.next = null;
        return father;
    }

    private static void show(ListNode node) {
        while (node != null) {
            System.out.println(node.val);
            node = node.next;
        }
    }

    public static void main(String[] args) {
        ListNode l0 = new ListNode(1);
        ListNode l1 = new ListNode(2);
        ListNode l2 = new ListNode(3);
        ListNode l3 = new ListNode(4);
        ListNode l4 = new ListNode(5);

        l0.next = l1;
        l1.next = l2;
        l2.next = l3;
        l3.next = l4;

        ListNode head = l0;
        show(reverseList(head));
    }
}