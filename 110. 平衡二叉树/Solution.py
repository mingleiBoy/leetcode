# 110. 平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。

# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:

# 给定二叉树 [1,2,2,3,3,null,null,4,4]

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/balanced-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# AC不过:
#   1. 理解错平衡二叉树定义，初始算法是计算最长高度和最短高度差


class Solution:
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        if not root:
            return True, -1

        left_is_balanced, left_height = self.isBalancedHelper(root.left)
        if not left_is_balanced:
            return False, -1

        right_is_balanced, right_height = self.isBalancedHelper(root.right)
        if not right_is_balanced:
            return False, -1

        return abs(left_height - right_height) < 2, 1 + max(left_height, right_height)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]
