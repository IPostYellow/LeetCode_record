'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321
Example 2:
Input: -123
Output: -321
Example 3:
Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=list(str(x))
            x.reverse()
            x=''.join(x)
            x=int(x)
            if (x>2**31-1):
                return 0
            else:
                return x
        else:
            x=list(str(x))
            x=x[1:]
            x.reverse()
            x=''.join(x)
            result='-'+x
            result=int(result)
            if result<-2**31:
                return 0
            else:
                return result
#执行用时 :44 ms 在所有 python3 提交中击败了85.13%的用户内存消耗 :13.7 MB, 在所有 python3 提交中击败了5.21%的用户
#由于这个的效果比较好了，所以便没有多解了。其实用for循环暴力解肯定更慢，就不尝试了
