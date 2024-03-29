'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
输入: 121
输出: true
示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:
你能不将整数转为字符串来解决这个问题吗？

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true
Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        p=str(x)
        print(p)
        temp=list(p)
        temp.reverse()
        temp=''.join(temp)
        print(temp)
        if temp==p:
            return True
        else:
            return False
# p=Solution()
# print(p.isPalindrome(-121))
#执行用时 :84 ms, 在所有 python3 提交中击败了70.03%的用户内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.01%的用户
#考虑到负数肯定不是回文数，那么加一句if判断可以大大提高速度
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            p=str(x)
            temp=list(p)
            temp.reverse()
            temp=''.join(temp)
            print(temp)
            print(p)
            if temp==p:
                return True
            else:
                return False
#执行用时 :72 ms, 在所有 python3 提交中击败了90.69%的用户内存消耗 :13.9 MB, 在所有 python3 提交中击败了5.01%的用户
# 不转换成字符串来进行判断
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            p = x
            y = 0
            while (x != 0):
                temp = x - (x // 10) * 10
                x = x // 10
                y = y * 10 + temp
            return y == p

# 执行用时 :84 ms, 在所有 python3 提交中击败了69.74%的用户内存消耗 :14.1 MB, 在所有 python3 提交中击败了5.01%的用户
