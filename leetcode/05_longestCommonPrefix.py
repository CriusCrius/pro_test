"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
    输入: ["flower", "flow", "flight"]
    输出: "fl"
示例 2:
    输入: ["dog", "racecar", "car"]
    输出: ""
    解释: 输入不存在公共前缀。
说明:
    所有输入只包含小写字母 a-z。
"""

"""
# 方法一
class Solution(object):
    def longestCommonPrefix(self, s):
        s1 = min(s)
        s2 = max(s)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
"""


# 方法二
class Solution(object):
    def longestCommonPrefix(self, s):
        if not s:
            return ""
        ss = list(map(set, zip(*s)))  # *相当于解压，用zip返回一个二维列表，map中用set对该二位列表去重，最后转为一个列表
        print("ss ==== ", ss)
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) != 1:
                break
            res = res + x[0]
        return res


if __name__ == '__main__':
    s = ["flower", "flow", "flight"]
    sol = Solution()
    print("res === ", sol.longestCommonPrefix(s))
