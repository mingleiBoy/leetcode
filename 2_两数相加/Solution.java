/**  2. 两数相加
// 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
// 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
// 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
// 示例：

// 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
// 输出：7 -> 0 -> 8
// 原因：342 + 465 = 807

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/add-two-numbers
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

class ListNode {
    int val;
    ListNode next;
    ListNode(final int x) { val = x; }
}

class Solution {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode node = new ListNode(-1);
        ListNode head = node;

        int count = 0;  // 进位
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                head.val = (l2.val + count) % 10;
                count = l2.val + count > 9 ? 1 : 0;

                l2 = l2.next;
            } else if (l2 == null) {
                head.val = (l1.val + count) % 10;
                count = l1.val + count > 9 ? 1 : 0;

                l1 = l1.next;
            } else {
                head.val = (l1.val + l2.val + count) % 10;
                count = l1.val + l2.val + count > 9 ? 1 : 0;

                l1 = l1.next;
                l2 = l2.next;
            }

            if (l1 != null || l2!= null) {
                head.next = new ListNode(-1);
                head = head.next;
            } else if (count == 1) {
                head.next = new ListNode(1);
            }
        }
        
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
        // l1.next = new ListNode(4);
        // l1.next.next = new ListNode(3); 

        ListNode l2 = new ListNode(9);
        l2.next = new ListNode(0);
        l2.next.next = new ListNode(1);
        // l2.next.next.next = new ListNode(1);

        show(addTwoNumbers(l1, l2));
    }
}