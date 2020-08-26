"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

题解
https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
"""


class Solution:
    """
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start + max_len]
    """

    def longestPalindrome(self, s: str) -> str:
        # 中心扩散
        size = len(s)
        if size < 2:
            return s

        max_len = 1

        for i in range(size):
            palindrome_odd, odd_len = self.center_spread(s, size, i, i)
            palindrome_even, even_len = self.center_spread(s, size, i, i + 1)

            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    # return: 回文子串, 子串长度
    def center_spread(self, s, size, left, right) -> (str, int):
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1

        # s[i:j] 左闭右开  即s[0:2] == s[0] + s[1]
        return s[i + 1:j], j - i - 1

solution = Solution()
s = 'babad'
print(solution.longestPalindrome(s))

