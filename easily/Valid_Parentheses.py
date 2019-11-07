'''
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

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 一开始就尝试了最简单粗暴的方法，可是没想到速度这么快？
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif i == '{':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0:
                    return False
                if '(' == stack.pop():
                    continue
                else:
                    return False
            elif i == ']':
                if len(stack) == 0:
                    return False
                if '[' == stack.pop():
                    continue
                else:
                    return False
            elif i == '}':
                if len(stack) == 0:
                    return False
                if '{' == stack.pop():
                    continue
                else:
                    return False
        if len(stack):
            return False
        else:
            return True
#执行用时 :28 ms, 在所有 python3 提交中击败了99.95%的用户内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.51%的用户
