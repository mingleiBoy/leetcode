/** 61_旋转链表
// 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

// 示例 1:

// 输入: 1->2->3->4->5->NULL, k = 2
// 输出: 4->5->1->2->3->NULL
// 解释:
// 向右旋转 1 步: 5->1->2->3->4->NULL
// 向右旋转 2 步: 4->5->1->2->3->NULL
// 示例 2:

// 输入: 0->1->2->NULL, k = 4
// 输出: 2->0->1->NULL
// 解释:
// 向右旋转 1 步: 2->0->1->NULL
// 向右旋转 2 步: 1->2->0->NULL
// 向右旋转 3 步: 0->1->2->NULL
// 向右旋转 4 步: 2->0->1->NULL

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/rotate-list
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class ListNode {
    int val;
    ListNode next;
    ListNode(final int x) { val = x; }
}

class Solution {
    public static ListNode rotateRight(ListNode head, int k) {
        if (head == null) return null;
        if (k == 0) return head;
        
        ListNode root = head;
        ListNode tail = head;
        int N = 0;
        while (head != null) {
            N++;
            if (head.next != null) tail = head.next;
            head = head.next;
        }
        head = root;

        if (k % N == 0) return root;

        int sliceIndex = N - k % N - 1;
        for (int i = 0; i < sliceIndex; i++) {
            if (head.next == null) return root;
            head = head.next;
        }

        tail.next = root;
        root = head.next; 
        head.next = null;

        return root;
    }

    private static void show(ListNode node) {
        while (node != null) {
            System.out.println(node.val);
            node = node.next;
        }
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(3); 
        l1.next.next.next = new ListNode(4); 
        l1.next.next.next.next = new ListNode(5); 

        int k = 5;
        show(rotateRight(l1, k));
    }
}