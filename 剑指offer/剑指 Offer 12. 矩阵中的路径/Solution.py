# 剑指 Offer 12. 矩阵中的路径
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
#
# [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
#
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
#
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#
# 提示：
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


# 矩阵搜索问题首先想到 DFS （深度优先搜索）
# 配合条件过滤，减少复杂度 （剪枝）
# DFS 先想到递归 --> 起始、终止条件 --> 下次递归
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False

        # i,j 表示矩阵中的行列
        # k 表示匹配字符串中待匹配字符的位置
        # 返回值是当前位置是否匹配（节点元素相等 && 没有遍历过）
        def dfs(i, j, k) -> bool:
            # 终止条件
            # board[i][j] == '' 也包括在 board[i][j] != word[k] 里
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                # 所以 k >= len(word) 这个情况不会出现
                return True

            # 使用技巧：不用额外空间进行 checked 标记
            # 下面记得利用函数堆栈的特性将值进行还原
            board[i][j] = ''
            # 分别沿上下左右遍历
            # 用 或 连接： 只要有一个方向满足要求即可
            res = dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)
            # 注意这里： 只有上面的四个方向都遍历完，才会走到这里
            # 如果上面已经走完，证明这个节点之后的通路就有了结果，不论 true or false
            board[i][j] = word[k]
            return res

        # 这里只从左上角开始是不行的
        # [0,0]点开始就被标记了，但是若它是路径的最后一个点，就无法达成了
        # return dfs(0, 0, 0)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False
