# 剑指 Offer 58 - II. 左旋转字符串
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
#
#  
#
# 示例 1：
#
# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"
#
# 相关标签   字符串
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


'''
补一个 三次翻转 的方法，适用于 C++ 这种字符串可变的

abcdefg  k = 2

1. 整体翻转： gfedcba
2. 前部翻转： cdefg
3. 后部翻转:  cdefgab 

class Solution {
public:
    string reverseLeftWords(string s, int n) {
        reverseString(s, 0, n - 1);
        reverseString(s, n, s.size() - 1);
        reverseString(s, 0, s.size() - 1);
        return s;
    }

双指针翻转
private:
    void reverseString(string& s, int i, int j) {
        while(i < j) swap(s[i++], s[j--]);
    }
};

'''
