# 98. 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# AC不过：没充分理解题目，对于初始思路迷之坚持。设计的递归函数不合理。
# https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yi-zhang-tu-rang-ni-ming-bai-shang-xia-jie-zui-da-/
class Solution:
    def helper(self, root: TreeNode, min_val, max_val) -> bool:
        if not root:
            return True

        # 如果当前节点值符合规定，继续进行之后的递归
        if max_val > root.val > min_val:
            pass
        else:   # 如果不符合规定，之间返回 False
            return False

        # 对左子树进行递归，此时最大值应该为当前节点值
        if not self.helper(root.left, min_val, root.val):
            return False
        # 对右子树进行递归，此时最小值应该为当前节点值
        if not self.helper(root.right, root.val, max_val):
            return False
        # 如果成功避开所有坑，恭喜，这个当前节点下的子树是一个二叉搜索树
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("-inf"), float("inf"))


# main
root_node = TreeNode(2)
root_node.left = TreeNode(1)
root_node.right = TreeNode(0)

s = Solution()
print(s.isValidBST(root_node))
