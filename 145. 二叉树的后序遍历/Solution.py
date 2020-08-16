# 145. 二叉树的后序遍历
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        val_list = []
        stack = [root]
        node_type = type(TreeNode)
        while stack:
            root = stack.pop()
            if type(root) != node_type and root:
                val_list.append(root.val)

            if root:
                stack.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return val_list
