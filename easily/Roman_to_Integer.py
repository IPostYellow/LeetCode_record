'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 最low的暴力循环法
class Solution:
    def romanToInt(self, s: str) -> int:
        List = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        pr_list = [1, 5, 10, 50, 100, 500, 1000]
        temp = list(s)
        sum = 0
        T = 0  # 用来判断是否该跳过了
        for i in range(len(temp)):
            if T == 0:
                print(sum)
                if i < len(temp) - 1:
                    if List.index(temp[i + 1]) > List.index(temp[i]):
                        sum += pr_list[List.index(temp[i + 1])] - pr_list[List.index(temp[i])]
                        T = 1
                    else:
                        sum += pr_list[List.index(temp[i])]
                elif i == len(temp) - 1:
                    sum += pr_list[List.index(temp[i])]
            else:
                T -= 1
        return sum


# 执行用时 :80 ms, 在所有 python3 提交中击败了35.85%的用户内存消耗 :14.1 MB, 在所有 python3 提交中击败了5.25%的用户
# 改进的字典映射而且灵活使用加减可以减少多次判断
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            if (i < len(s) - 1) and (roman_dict[s[i + 1]] > roman_dict[s[i]]):
                sum -= roman_dict[s[i]]
            else:
                sum += roman_dict[s[i]]
        return sum

#执行用时 :56 ms, 在所有 python3 提交中击败了93.49%的用户内存消耗 :14.1 MB, 在所有 python3 提交中击败了5.25%的用户

