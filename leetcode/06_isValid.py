"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
    注意空字符串可被认为是有效字符串。

示例 1:
    输入: "()"
    输出: true
示例 2:
    输入: "()[]{}"
    输出: true
示例 3:
    输入: "(]"
    输出: false
示例 4:
    输入: "([)]"
    输出: false
示例 5:
    输入: "{[]}"
    输出: true
"""


class Solution(object):
    def isValid(self, strs):
        if len(strs) % 2 != 0:
            return False
        while "[]" in strs or "{}" in strs or "()" in strs:
            strs = strs.replace("{}", "")
            strs = strs.replace("[]", "")
            strs = strs.replace("()", "")
        if len(strs):
            return False
        return True


# 使用栈完成
class Solution2(object):
    def isValid(self, strs):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for s in strs:
            if s in mapping:
                top_element = stack.pop() if stack else '*'
                if mapping[s] != top_element:
                    return False
            else:
                stack.append(s)
        return not stack


if __name__ == '__main__':
    a = "{[]}"
    b = "([)]"
    c = "()[]{}"
    d = "(){}["
    e = ""
    sol = Solution2()
    print(sol.isValid(e))
