# 剑指 Offer 28. 对称的二叉树
# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# 示例 1：
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
# 示例 2：
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 限制：
# 0 <= 节点个数 <= 1000
#
# 注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 在于想清楚如何判断对称性
# 递归时传入一对节点
# 只要判断好所有的成对节点就可以了
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def recursive(node_l: TreeNode, node_r: TreeNode) -> bool:
            if not node_l and not node_r:
                return True
            if not node_l or not node_r or node_l.val != node_r.val:
                return False
            return recursive(node_l.left, node_r.right) and recursive(node_l.right, node_r.left)

        return recursive(root.left, root.right)