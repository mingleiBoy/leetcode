# 剑指 Offer 55 - II. 平衡二叉树
# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
#
# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#
# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。
#
# 限制：
#
# 0 <= 树的结点个数 <= 10000
# 注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 利用树的最大深度来做，配合剪枝的技巧
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 检测当前节点为根节点的最大深度
        # 很灵魂：0表示空节点，-1表示当前树包含不平衡的子树，剪枝用
        def recursive(node: TreeNode) -> int:
            if not node:
                return 0

            left = recursive(node.left)
            if left == -1:
                # 直接返回，剪枝
                return -1

            right = recursive(node.right)
            if right == -1:
                return -1

            return -1 if abs(left - right) > 1 else max(left, right) + 1

        return recursive(root) != -1
