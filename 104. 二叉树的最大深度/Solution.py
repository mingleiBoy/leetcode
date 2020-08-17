# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 凭实力递归 AC ，有点入门的意思了
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_height = 0

        def helper(head: TreeNode) -> int:
            nonlocal max_height
            if not head:
                return 0

            height = 1 + max(helper(head.left), helper(head.right))
            max_height = max(height, max_height)
            return height

        helper(root)
        return max_height
