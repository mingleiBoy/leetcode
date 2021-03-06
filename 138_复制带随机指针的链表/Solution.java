import java.util.HashMap;

/** 138. 复制带随机指针的链表
// 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
// 要求返回这个链表的 深拷贝。 

// 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
// val：一个表示 Node.val 的整数。
// random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

// 示例 1：
// 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
// 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

// 输入：head = [[3,null],[3,0],[3,null]]
// 输出：[[3,null],[3,0],[3,null]]

// 示例 4：
// 输入：head = []
// 输出：[]
// 解释：给定的链表为空（空指针），因此返回 null。

// 提示：
// -10000 <= Node.val <= 10000
// Node.random 为空（null）或指向链表中的节点。
// 节点数目不超过 1000 。

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/copy-list-with-random-pointer
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}

class Solution {
    public static Node copyRandomList(Node head) {
        if (head == null) return null;

        Node root = head;
        int N = 0;
        HashMap<Node, Integer> hash = new HashMap<Node, Integer>();
        while (head != null) {
            hash.put(head, Integer.valueOf(N++));
            head = head.next;
        }
        head = root;
        
        Node[] nodeList = new Node[N];
        for (int i = 0; i < N; i++) {
            nodeList[i] = new Node(head.val);
            head = head.next;
            if (i == 0) continue;
            nodeList[i-1].next = nodeList[i];
        }
        head = root;

        for (int i = 0; i < N; i++) {
            Node node = nodeList[i];
            Integer randomIndex = hash.get(head.random);
            head = head.next;
            if (randomIndex != null) {
                node.random = nodeList[randomIndex.intValue()];
            }
        }

        return nodeList[0];
    }

    private static void show(Node node) {
        while (node != null) {
            System.out.println(node.val);
            node = node.next;
        }
    }

    public static void main(String[] args) {
        Node l0 = new Node(7);
        Node l1 = new Node(13);
        Node l2 = new Node(11);
        Node l3 = new Node(10);
        Node l4 = new Node(1);

        l0.next = l1;
        l0.random = null;

        l1.next = l2;
        l1.random = l0;

        l2.next = l3;
        l2.random = l4;
        
        l3.next = l4;
        l3.random = l2;

        l4.next = null;
        l4.random = l0;

        Node head = l0;
        show(copyRandomList(head));
    }
}