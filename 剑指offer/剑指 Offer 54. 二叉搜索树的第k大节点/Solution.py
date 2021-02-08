# 剑指 Offer 54. 二叉搜索树的第k大节点
# 给定一棵二叉搜索树，请找出其中第k大的节点。
#
# 限制：
# 1 ≤ k ≤ 二叉搜索树元素个数
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉搜索树的中序遍历(左根右)就是递增序列
# 中序遍历（右根左）就是递减序列
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = 0

        # 当前节点下是否已经找到第k大节点
        def dfs(node: TreeNode) -> bool:
            if not node:
                return False

            nonlocal res
            nonlocal k

            right = dfs(node.right)
            if right:
                return True

            # 注意: K是当前的第k大 **节点**
            if k == 0:
                res = node.val
                return True
            k -= 1

            left = dfs(node.left)
            if left:
                return True

            return False

        dfs(root)
        return res

