# 763. 划分字母区间
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
#
# 示例：
#
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#
# 提示：
#
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-labels
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode-solution/
from typing import List

# 贪心 + 双指针   思路很精巧
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 获取字符的最后一次出现的index
        # 字符本身是什么不重要
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition

s = Solution()
string = "a"
print(s.partitionLabels(string))
