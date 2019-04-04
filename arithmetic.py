#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Datetime : 19-4-3 下午5:16
# @Author : min
# @Site : 
# @function :  算法


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        题目: 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
        示例 1:
            输入: 123
            输出: 321
        示例 2:
            输入: -123
            输出: -321
        示例 3:
            输入: 120
            输出: 21
        注意:
            假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
        """
        if x == 0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2**31 < x < 2**31-1:
            return x
        return 0

    def romanToInt(self, s):
        """
        :param s:
        :return:
        罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
            字符          数值
            I             1
            V             5
            X             10
            L             50
            C             100
            D             500
            M             1000
        例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

        通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
        给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

        示例 1:
            输入: "III"
            输出: 3
        示例 2:
            输入: "IV"
            输出: 4
        示例 3:
            输入: "IX"
            输出: 9
        示例 4:
            输入: "LVIII"
            输出: 58
            解释: L = 50, V= 5, III = 3.
        示例 5:
            输入: "MCMXCIV"
            输出: 1994
            解释: M = 1000, CM = 900, XC = 90, IV = 4.
        """
        s = s.replace("CM", "+900").replace("CD", "+400").replace("XC", "+90").replace("XL", "+40").replace("IX", "+9").replace(
            "IV", "+4")
        s = s.replace("I", "+1").replace("V", "+5").replace("X", "+10").replace("L", "+50").replace("C", "+100").replace("D", "+500").replace(
            "M", "+1000")
        return sum(int(x) for x in ("0" + s).split("+"))

    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1


if __name__ == '__main__':
    a = Solution()
    # print(a.reverse(12231))
    # print a.romanToInt1('LIVVV')
    print a.longestCommonPrefix(["fowrerasdfasdfsdfsadffd", "fowsdjkhfkj", "flight"])