import java.util.ArrayList;
import java.util.List;

/**
 * 94. 二叉树的中序遍历
 * 
 * // 给定一个二叉树，返回它的中序 遍历。 // 示例:
 * 
 * // 输入: [1,null,2,3] // 1 // \ // 2 // / // 3
 * 
 * // 输出: [1,3,2]
 * 
 * // 来源：力扣（LeetCode） //
 * 链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal //
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 * 
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public static List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) return new ArrayList<Integer>();

        List<Integer> list = new ArrayList<Integer>();
        inorderTraversalImpl(list, root);
        return list;
    }

    private static void inorderTraversalImpl(List<Integer> list, TreeNode root) {
        if (root == null) return;
        
        inorderTraversalImpl(list, root.left);
        list.add(root.val);
        inorderTraversalImpl(list, root.right);
    }

    private static void show(List<Integer> list) {
        if (list == null || list.size() == 0) {
            System.out.println("list is null.");
            return;
        }

        for (Integer integer : list) {
            System.out.println(integer);
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode l1 = new TreeNode(2);
        TreeNode l2 = new TreeNode(3);
        
        root.right = l1;
        l1.left = l2;
        show(inorderTraversal(root));
    }
}