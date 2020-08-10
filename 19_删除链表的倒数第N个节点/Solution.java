/** 19_删除链表的倒数第N个节点
// 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

// 示例：
// 给定一个链表: 1->2->3->4->5, 和 n = 2.
// 当删除了倒数第二个节点后，链表变为 1->2->3->5.

// 说明：
// 给定的 n 保证是有效的。

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(final int x) { val = x; }
}

class Solution {
    public static ListNode removeNthFromEnd(ListNode head, int n) {
        if (n < 1) n = 1;
        
        ListNode node = head;
        ListNode slowNode = head;
        for (int i = 0; i < n; i++) {
            if (head == null) break;
            head = head.next;
        }

        if (head == null) {
            // n == head.length 遍历到最后了
            ListNode nextNode = node.next;
            node = null;
            return nextNode;
        }

        while (head.next != null) {
            head = head.next;
            slowNode = slowNode.next;
        }

        ListNode nextNode = slowNode.next;
        slowNode.next = nextNode.next;
        nextNode = null;

        return node;
    }

    private static void show(ListNode node) {
        while (node != null) {
            System.out.println(node.val);
            node = node.next;
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3); 

        int n = 0;
        show(removeNthFromEnd(l1, n));
    }
}