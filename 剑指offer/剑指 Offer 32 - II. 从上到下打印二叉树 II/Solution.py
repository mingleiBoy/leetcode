# 剑指 Offer 32 - II. 从上到下打印二叉树 II
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#
# 提示：
#
# 节点总数 <= 1000
# 注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 层序遍历 (BFS)  队列
# PS: 深度遍历 (DFS)  栈(函数调用默认提供)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
