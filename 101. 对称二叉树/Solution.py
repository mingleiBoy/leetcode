# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# 二叉树 [1,2,2,3,null,null,3] 是对称的。
#     1
#    / \
#   2   2
#  /     \
# 3       3

# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#  
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/symmetric-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 官方答案，递归。
    # https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode-solution/
    #
    # 如果一个树的左子树与右子树镜像对称，那么这个树是对称的。
    #   因此，该问题可以转化为：两个树在什么情况下互为镜像？
    # 如果同时满足下面的条件，两个树互为镜像：
    #   1. 它们的两个根结点具有相同的值
    #   2. 每个树的右子树都与另一个树的左子树镜像对称

    def check(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        # 稍优化写法
        # if not root:
        #     return True
        #
        # return self.check(root.left, root.right)

        return self.check(root, root)
