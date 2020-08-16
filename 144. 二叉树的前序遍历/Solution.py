# 144. 二叉树的前序遍历
# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 个人实现遍历
    # AC不过:
    #   1. 因为是栈，当成队列的 FIFO 了，LeetCode 自制用例不认真
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        tree_list = []
        tree_stack = [root]
        while tree_stack:
            root = tree_stack.pop()
            if root:
                tree_list.append(root.val)

            right_node = root.right
            if right_node:
                tree_stack.append(right_node)

            left_node = root.left
            if left_node:
                tree_stack.append(left_node)

        return tree_list

    # LeetCode 题解答案。统一的代码实现遍历前、中、后序
    # def preorderTraversal(self, root):
    #     if root is None:
    #         return []
    #     t = type(root)  # 保存树的类型
    #     out = []  # 初始化输出数组
    #     stack = [root]  # 将树压入栈中
    #     while stack:  # 循环栈
    #         root = stack.pop()  # 根节点等于出栈的节点
    #         if type(root) != t and root is not None:  # 如果此时root不为树并且不为空
    #             out.append(root)  # 将这个数加入输出数组中
    #             continue  # 结束本次循环
    #         if root:  # 如果此时root是树
    #             stack.append(root.right)  # 将右孩子压入栈
    #             stack.append(root.left)  # 将左孩子压入栈
    #             stack.append(root.val)  # 将根的值压入栈
    #     return out
