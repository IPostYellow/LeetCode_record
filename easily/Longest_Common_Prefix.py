'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


#最直接的做法，循环前缀进行比较
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        p = 0  #p=0表示出现了不存在的项
        if strs == []:
            return result
        for i in range(len(strs[0]) + 1):
            temp = strs[0][:i]
            for j in strs:
                if len(temp) > len(j):
                    return result
                if temp == j[:i]:
                    p = 1
                else:
                    p = 0
                    return result
            if p == 1:
                result = temp
        return result
#执行用时 :52 ms, 在所有 python3 提交中击败了56.94%的用户内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.53%的用户
