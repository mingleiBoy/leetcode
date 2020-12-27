# 205. 同构字符串
# 给定两个字符串s和t，判断它们是否是同构的。
#
# 如果s中的字符可以被替换得到t，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
#
# 输入: s = "egg", t = "add"
# 输出: true
# 示例 2:
#
# 输入: s = "foo", t = "bar"
# 输出: false
# 示例 3:
#
# 输入: s = "paper", t = "title"
# 输出: true
# 说明:
# 你可以假设s和 t 具有相同的长度。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/isomorphic-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True

        hash_map = {}
        hash_map_revert = {}
        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]
            if not hash_map.get(ch_s):
                if ch_t in hash_map_revert:
                    return False
                else:
                    hash_map[ch_s] = ch_t
                    hash_map_revert[ch_t] = ch_s
            elif hash_map[ch_s] != ch_t:
                return False

        return True


sln = Solution()
str_s = "ab"
str_t = "cc"
print(sln.isIsomorphic(str_s, str_t))
