# 剑指 Offer 68 - II. 二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：
# “对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 说明:
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
# 注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 祖先：root 的左（右）子树中有节点 p，或者 root == p
# 公共祖先： root 的左右子树分别为 p和q 的祖先，或者 q 在 p的子树中（反之亦然）
# 最近公共祖先： root 的左右子树均不为公共祖先，且root为公共祖先

# 递归
# 后序遍历 (自底向上还原)
class Solution:
    # 这个递归方法的含义不够明确
    # 实际是：返回p、q的公共祖先，或者当前子树中存在 p或q
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 终止条件
        if not root or root == p or root == q:
            return root

        # 判断左右子树是否为最近公共祖先，或者找到节点p或者q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左边没有找到p和q,说明p,q在右子树，那么右子树一定存在最近公共祖先，即right的返回值
        if not left:
            return right
        if not right:
            return left

        # 如果左右子树都找到了p和q,则此时根节点必为最近公共祖先。由于此处使用到了root,故为后序遍历。
        # 其实这个就是我们要找的最终答案，但是自底返回上层后会继续遍历其他子树，浪费
        # 可以定义一个 helper，除了遍历，返回一个额外的bool值，表示是否为最终值
        return root
