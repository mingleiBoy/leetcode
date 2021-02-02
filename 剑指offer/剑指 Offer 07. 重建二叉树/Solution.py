# 剑指 Offer 07. 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
#
# 限制：
#
# 0 <= 节点个数 <= 5000
#
# 注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 应该背下来的题
# 遇到二叉树的问题，首先想到递归
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildTreeHelper(root, left, right) -> TreeNode:
            # 先写终止条件
            if left > right:
                return None

            node = TreeNode(preorder[root])
            # 在中序列表中可以获取到 root 的位置
            index = dic[preorder[root]]
            node.left = buildTreeHelper(root+1, left, index-1)
            node.right = buildTreeHelper(index-left+root+1, index+1, right)
            return node

        n, dic = len(preorder), {}
        for i in range(n):
            dic[inorder[i]] = i
        return buildTreeHelper(0, 0, n-1)
