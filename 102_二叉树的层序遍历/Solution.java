import java.util.ArrayList;
import java.util.List;

/**
 * 102. 二叉树的层序遍历
// 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

// 示例：
// 二叉树：[3,9,20,null,null,15,7],

//     3
//    / \
//   9  20
//     /  \
//    15   7
// 返回其层次遍历结果：

// [
//   [3],
//   [9,20],
//   [15,7]
// ]

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public static List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<List<Integer>>();
        }

        List<List<Integer>> allList = new ArrayList<>();

        List<Integer> intList = new ArrayList<>();
        addValue(intList, root);

        List<TreeNode> nodeList = new ArrayList<TreeNode>();
        nodeList.add(root);
        
        
        while (!nodeList.isEmpty()) {
            List<Integer> nextLevelIntList = new ArrayList<>();
            List<TreeNode> nextLevelNodeList = new ArrayList<>();
            for (TreeNode treeNode : nodeList) {
                addValue(nextLevelIntList, treeNode.left);
                addValue(nextLevelIntList, treeNode.right);

                addNode(nextLevelNodeList, treeNode.left);
                addNode(nextLevelNodeList, treeNode.right);
            }
            allList.add(intList);
            intList = nextLevelIntList;
            nodeList = nextLevelNodeList;
        }

        return allList;
    }

    private static void addValue(List<Integer> list, TreeNode node) {
        if (list == null || node == null) return;
        list.add(node.val);
    }

    private static void addNode(List<TreeNode> list, TreeNode node) {
        if (list == null || node == null) return;
        list.add(node);
    }

    private static void showLevel(List<List<Integer>> list) {
        for (List<Integer> levelList : list) {
            show(levelList);
            System.out.println("---------");
        }
    }

    private static void show(List<Integer> list) {
        if (list == null || list.size() == 0) {
            System.out.println("list is null.");
            return;
        }

        for (Integer integer : list) {
            System.out.print(integer + "  ");
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        TreeNode l1 = new TreeNode(9);
        TreeNode l2 = new TreeNode(20);
        TreeNode l3 = new TreeNode(1111);
        TreeNode l4 = new TreeNode(1222);
        TreeNode l5 = new TreeNode(15);
        TreeNode l6 = new TreeNode(7);

        root.left = l1;
        root.right = l2;
        l1.left = l3;
        l1.right = l4;
        l2.left = l5;
        l2.right = l6;
        showLevel(levelOrder(root));
    }
}